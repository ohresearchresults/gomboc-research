# material-0907ccd6f2a8

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# ACTUAL_E17_DEGREE5_MINIMAL_FOUR_POLAR_ARROWS_V1

Coordinator theorem and exact continuous construction. This closes the actual-realization gap of [internal-source-reference], not the C34 layer. Bounds34<=Cmin<=622 and every canonical registry count remain unchanged. No external theorem or numerical optimization is a proof input.

## Statement
For EVERY epsilon in(0,1/1000], the nine rational halfspaces below define an actual uniformly filled convex polyhedron with(V,E,F)=(10,17,9), a true degree-five apex, and a minimally infeasible four-arrow consecutive path on its TRUE incident polar pentagon relative to its OWN volume centroid. All four WEAK selected arrows are impossible under any common physical SPD N. Every proper subset is strictly feasible under an explicitly constructed SPD on this SAME body and SAME own centroid. In particular, neither two consecutive quadrilateral tests nor all three-arrow local tests suffice even in actual own-COM E17 geometry.

This does not assert U1, S1,110 or FULL253. The four endpoint witness metrics have strict(S,U,H)=(2,2,2),(3,2,3),(3,2,3),(2,2,2), all weak000 and68/68 true edge primitives nonzero. Thus the example does not yet show that four-arrow processing is necessary after imposing the entire global U1 cone. Census is asserted at epsilon=1/1000; the CONTINUOUS theorem concerns true lattice, actual COM and minimal local four-arrow obstruction, not a whole-interval complete census.

## Exact body and combinatorics
Set p=((0,0),(2,0),(2,4),(-2,5),(-3,3)),s=(-1/12,23/9). Five side supports n_i=(p_i-s,1),b_i=1,i0..4, and base n5=(0,0,-3),b5=1 define a pentagonal pyramid with apexA=(0,0,1). Let x=1-n0.X,y=1-n1.X,z=1-n5.X be nonnegative local support slacks at the base corner F0/F1/F5. Add three planes
x+y+z>=epsilon;
x+2y+3z>=2epsilon;
x+4y+5z>=3epsilon.
The first is an ordinary corner cut. The next two pass through one already-created neighbor each. The removed corner is replaced by the FIVE local points epsilon times(0,1,0),(0,0,1),(1/2,0,1/2),(1,1/2,0),(3,0,0). The cuts remain away from the apex. This yields increments(+4,+7,+3) over the pentagonal pyramid.

At epsilon1/1000, lexicographically ordered actual rational vertices are
(-48/89,-48/89,-1/3),(-48/113,24/113,-1/3),(-1/2000,-96003/184000,-1/3),(0,-11997/23000,-333/1000),(0,0,1),(1/4000,-191901/368000,-1999/6000),(1/4000,-191853/368000,-1/3),(3/2000,-3831/7360,-1/3),(48/283,192/283,-1/3),(16/25,0,-1/3).
True oriented maximal faces, labels0..8:
(0,2,3,4),(3,5,7,9,4),(9,8,4),(8,1,4),(4,1,0),(1,8,9,7,6,2,0),(2,5,3),(2,6,5),(5,6,7).
Apex is vertex4, incident exactly to F0..F4. Each consecutive pair Fi,F(i+1 mod5) meets along one actual apex edge. No integration diagonal is counted mechanically.

All84 possible support triples are treated exactly. Each nonsingular triple gives an affine vertex function v0+epsilon*v1. Its nine affine support inequalities are intersected with(0,1/1000]. Every feasible triple covers that ENTIRE interval, and all others have empty intersection. Exactly10 distinct affine vertex functions survive. Strict nonincidences hold throughout. Hence the continuum lattice proof is not sampling at the endpoint.

## Actual mass and pole calculation
Use an interior-positive tetrahedral boundary fan and, separately, a fan from the actual apex including flat cells. Their volumes and first moments agree exactly at the endpoint. Across the entire interval the apex fan gives the exact polynomials
Vol(e)=624556032/1636525325-(7/368)e^3;
Mx(e)=-3574600568832/116444136494189375-(11/2944)e^4;
My(e)=-2059770018816/21425721114930845+(21/2116)e^3-(1425/270848)e^4;
Mz(e)=(7/1104)e^3-(11/8832)e^4.
Here Mx,My,Mz are FIRST VOLUME MOMENTS, not coordinates of the centroid or entries of the physical metric. Set g=(Mx,My,Mz)/Vol and q_i=n_i/(b_i-n_i.g). All real heights are positive. No free reference point or transported density is used.

Since q_i.(A-g)=1 for side poles0..4, set a=A-g and
B=[[1,0,0],[0,1,0],[-a_x/a_z,-a_y/a_z,1/a_z]].
Then q_i=B(P_i,1), where P_i=(q_ix,q_iy). These P_i form a strictly convex pentagon. Let e_i=P_(i+1)-P_i,i0..3. Form positive zero-displacement circuits
r1=(cross(e1,e3),cross(e3,e0),0,cross(e0,e1));
r2=(cross(e2,e3),0,cross(e3,e0),cross(e0,e2));
lambda=r1/2+r2.
All four lambda are strictly positive. Set Q=-sum lambda_i sym(P_i e_i^T). Then Q is positive definite. Writing A2 for B's first two columns yields the EXACT stress identity
sum lambda_i sym(q_i(q_(i+1)-q_i)^T)=-A2 Q A2^T.
The right side is nonzero negative semidefinite of rank two. Its pairing with EVERY N>0 is strictly negative. Thus not all four D_i=q_i^T N(q_(i+1)-q_i) can be nonnegative, including weak-arrow walls.

## Continuous strict subsystem witnesses
Use the four original rational matrices
N0=[[1,0,-20],[0,1,1],[-20,1,402]],
N1=[[2,-2,2],[-2,4,-19],[2,-19,147]],
N2=[[12,0,1],[0,2,1],[1,1,1]],
N3=[[1,0,1],[0,1,9],[1,9,83]].
T=[[1,0,-s_x],[0,1,-s_y],[0,0,1]],L=B*T; define Nactual_j=L^-T Nj L^-1, and Mactual_j=Nactual_j^-1. Each Nj is SPD. For every epsilon in the entire interval, its omitted arrow j is negative and the other three arrows are strictly positive. This also supplies all smaller proper subsets.

The complete code proves continuum positivity by inclusion-preserving EXACT rational interval arithmetic on epsilon in[0,1/1000], applied to the explicitly generated mass polynomials, heights, pole coordinates, circuit weights, Q11,detQ and the sixteen witness evaluations. Intervals are not floating tolerances. In particular Q11>19.9484 and detQ>348.11 uniformly; every retained witness arrow>1.0004. The actual unrounded rational endpoints are used in assertions; reported intervals are outward rounded only for legibility. The zero endpoint is the original pyramid, not10/17/9; it may be included in the metric interval calculation but is excluded from the continuum lattice claim.

This is a continuous actual countercontrol to completeness of three-arrow gates, not an unsuccessful candidate promoted to110. Small additional actual shape perturbations preserve the strict stress/subsystem margins when the genuine degree-five incidence and common own-centroid poles are retained; no numerical radius for those additional perturbations is asserted.

## Recovery and evidence
Complete standalone source below: actual_pentagon.py14547bytes SHA256b4c5e7c6bfd80199e6aafa0da64242921d9a52f1a2df1173e5b7e3ec79cd972a.
Regenerated actual_pentagon_report.json101762bytes SHA2569be02a1754e4ab8b8b6152861fc2c6f3e507fe012d6ef94f75fdcbff535d193b.
CPython3.13.5 observed; code requires>=3.10 and only stdlib. No solver, seed or external data is used. Save code UTF-8/LF with finalLF. Run python -S actual_pentagon.py. Copy ONLY this source into a new directory and run the same command for cold reconstruction. Both ordinary and cold runs were executed by the coordinator with matching report pins. This is not claimed to be an independently implemented verification or proof-assistant formalization.
Markers:
ACTUAL_E17_TRUE_DEGREE5_PENTAGON_ALL_PROPER_SUBSYSTEMS_STRICT_PASS
ACTUAL_E17_ENTIRE_CUT_INTERVAL_0_LT_EPS_LE_1_1000_PASS
The report contains all rational supports,vertices,faces,trueedges,two mass fans,owncentroid,poles,weights,stress,physical reciprocal metrics,complete endpoint census and continuous interval certificates.

```python
"""Actual uniform 10/17/9 realization of a minimal four-arrow polar path.
CPython >=3.10, stdlib, exact rational arithmetic, assertions enabled.
Run: python -S actual_pentagon.py
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys

P=((0,0),(2,0),(2,4),(-2,5),(-3,3))
SHIFT=(F(-1,12),F(23,9))
EPS=F(1,1000)
OLD_METRICS=(
 ((1,0,-20),(0,1,1),(-20,1,402)),
 ((2,-2,2),(-2,4,-19),(2,-19,147)),
 ((12,0,1),(0,2,1),(1,1,1)),
 ((1,0,1),(0,1,9),(1,9,83)))

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(c,a): return tuple(c*x for x in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def cross2(a,b): return a[0]*b[1]-a[1]*b[0]
def cross3(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(A):
 if len(A)==1: return A[0][0]
 return sum(((-1)**j*A[0][j]*det(tuple(tuple(r[k] for k in range(len(A)) if k!=j) for r in A[1:])) for j in range(len(A))),F(0))
def tr(A): return tuple(zip(*A))
def mm(A,B): return tuple(tuple(dot(a,b) for b in tr(B)) for a in A)
def mv(A,v): return tuple(dot(r,v) for r in A)
def inv(A):
 n=len(A); d=det(A); assert d
 return tuple(tuple(F((-1)**(i+j))*det(tuple(tuple(A[r][c] for c in range(n) if c!=i) for r in range(n) if r!=j))/d for j in range(n)) for i in range(n))
def form(A,a,b): return dot(a,mv(A,b))
def minors(A): return tuple(det(tuple(tuple(A[i][j] for j in range(k)) for i in range(k))) for k in range(1,len(A)+1))
def sym_outer(a,b): return tuple(tuple((a[i]*b[j]+a[j]*b[i])/2 for j in range(len(a))) for i in range(len(a)))
def matadd(A,B): return tuple(tuple(x+y for x,y in zip(a,b)) for a,b in zip(A,B))
def matscale(c,A): return tuple(scale(c,a) for a in A)

def hull_order(ids,verts,normal):
 # Projection omitting a nonzero normal coordinate is injective on the face.
 drop=next(i for i in range(3) if normal[i])
 keep=[i for i in range(3) if i!=drop]
 xy={v:tuple(verts[v][i] for i in keep) for v in ids}
 ordered=sorted(ids,key=xy.get)
 def half(items):
  out=[]
  for v in items:
   while len(out)>1 and cross2(sub(xy[out[-1]],xy[out[-2]]),sub(xy[v],xy[out[-1]]))<=0: out.pop()
   out.append(v)
  return out
 cycle=half(ordered)[:-1]+half(ordered[::-1])[:-1]
 assert set(cycle)==set(ids) and len(cycle)==len(ids)
 a,b,c=(verts[i] for i in cycle[:3])
 if dot(cross3(sub(b,a),sub(c,a)),normal)<0: cycle.reverse()
 return tuple(cycle)

def geometry(normals,offsets):
 vertices=set()
 for inds in combinations(range(len(normals)),3):
  A=tuple(normals[i] for i in inds)
  if not det(A): continue
  v=mv(inv(A),tuple(offsets[i] for i in inds))
  if all(dot(n,v)<=b for n,b in zip(normals,offsets)): vertices.add(v)
 vertices=tuple(sorted(vertices))
 faces=[]
 for n,b in zip(normals,offsets):
  ids=[i for i,v in enumerate(vertices) if dot(n,v)==b]
  assert len(ids)>=3
  faces.append(hull_order(ids,vertices,n))
 edges={tuple(sorted((f[i],f[(i+1)%len(f)]))) for f in faces for i in range(len(f))}
 assert all(sum(a in f and b in f for f in faces)==2 for a,b in edges)
 o=tuple(sum(v[j] for v in vertices)/len(vertices) for j in range(3))
 assert all(dot(n,o)<b for n,b in zip(normals,offsets))
 volume=F(0); moment=(F(0),)*3; cells=[]
 for fi,f in enumerate(faces):
  for k in range(1,len(f)-1):
   inds=(f[0],f[k],f[k+1]); a,b,c=(vertices[i] for i in inds)
   w=det((sub(a,o),sub(b,o),sub(c,o)))/6; assert w>0
   center=scale(F(1,4),add(o,add(a,add(b,c))))
   volume+=w; moment=add(moment,scale(w,center))
   cells.append((fi,inds,w,center))
 g=scale(1/volume,moment)
 poles=tuple(scale(1/(b-dot(n,g)),n) for n,b in zip(normals,offsets))
 assert all(b-dot(n,g)>0 for n,b in zip(normals,offsets))
 # Different genuine fan, from the degree-five apex. Flat fan cells are kept.
 apex=(F(0),F(0),F(1)); vol2=F(0); mom2=(F(0),)*3; fan2=[]
 for fi,f in enumerate(faces):
  for k in range(1,len(f)-1):
   inds=(f[0],f[k],f[k+1]); a,b,c=(vertices[i] for i in inds)
   w=det((sub(a,apex),sub(b,apex),sub(c,apex)))/6; assert w>=0
   center=scale(F(1,4),add(apex,add(a,add(b,c))))
   vol2+=w; mom2=add(mom2,scale(w,center)); fan2.append((fi,inds,w,center))
 assert vol2==volume and mom2==moment
 return vertices,tuple(faces),tuple(sorted(edges)),volume,g,poles,cells,fan2

def census(vertices,faces,edges,g,poles,N):
 M=inv(N); assert min(minors(N))>0 and min(minors(M))>0
 x=tuple(sub(v,g) for v in vertices)
 adj=[set() for _ in vertices]; dual=[set() for _ in faces]; pairs=[]
 for a,b in edges:
  adj[a].add(b);adj[b].add(a)
  i,j=tuple(k for k,f in enumerate(faces) if a in f and b in f)
  dual[i].add(j);dual[j].add(i);pairs.append((a,b,i,j))
 dp={(a,b):form(M,x[a],sub(x[b],x[a])) for a in range(len(x)) for b in adj[a]}
 dq={(i,j):form(N,poles[i],sub(poles[j],poles[i])) for i in range(len(poles)) for j in dual[i]}
 zero=sum(v==0 for v in tuple(dp.values())+tuple(dq.values()))
 assert zero==0
 U=[i for i in range(len(x)) if all(dp[i,j]<0 for j in adj[i])]
 S=[i for i in range(len(poles)) if all(dq[i,j]<0 for j in dual[i])]
 H=[(a,b) for a,b,i,j in pairs if max(dp[a,b],dp[b,a],dq[i,j],dq[j,i])<0]
 assert len(S)+len(U)-len(H)==2
 return dict(S=S,U=U,H=H,weak=[0,0,0],zero_primitives=zero,
  primal_arrows=[[a,b,v] for (a,b),v in sorted(dp.items())],
  dual_arrows=[[i,j,v] for (i,j),v in sorted(dq.items())],N=N,M=M)

# Exact polynomial and interval arithmetic for the complete cut-size interval.
def padd(p,q):
 return tuple((p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0) for i in range(max(len(p),len(q))))
def pscale(c,p): return tuple(c*x for x in p)
def pmul(p,q):
 r=[F(0)]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  for j,b in enumerate(q): r[i+j]+=a*b
 return tuple(r)
def peval(p,t):
 v=F(0)
 for c in reversed(p): v=v*t+c
 return v
class I:
 def __init__(self,lo,hi=None):
  self.lo=F(lo);self.hi=F(lo if hi is None else hi);assert self.lo<=self.hi
 def __add__(self,b):
  if not isinstance(b,I):b=I(b)
  return I(self.lo+b.lo,self.hi+b.hi)
 __radd__=__add__
 def __neg__(self):return I(-self.hi,-self.lo)
 def __sub__(self,b):return self+-b if isinstance(b,I) else self+I(-b)
 def __rsub__(self,b):return I(b)+-self
 def __mul__(self,b):
  if not isinstance(b,I):b=I(b)
  v=[self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi]
  return I(min(v),max(v))
 __rmul__=__mul__
 def __truediv__(self,b):
  if not isinstance(b,I):b=I(b)
  assert b.lo>0 or b.hi<0
  return self*I(1/b.hi,1/b.lo)
 def __rtruediv__(self,b):return I(b)/self
 def coarse(self):
  # Outward-rounded display; unrounded rationals are used by every assertion.
  den=10**12
  return (F((self.lo*den).__floor__(),den),F((self.hi*den).__ceil__(),den))

def family(normals,offsets,V,faces,apex,T):
 N=len(normals)
 b0=(F(1),)*6+(F(3),F(6),F(10))
 b1=(F(0),)*6+(F(-1),F(-2),F(-3))
 assert tuple(b0[i]+EPS*b1[i] for i in range(N))==tuple(offsets)
 forms=set(); exclusion_intervals=[]
 for inds in combinations(range(N),3):
  A=tuple(normals[i] for i in inds)
  if not det(A):continue
  Ai=inv(A);v0=mv(Ai,tuple(b0[i] for i in inds));v1=mv(Ai,tuple(b1[i] for i in inds))
  low=F(0);high=EPS
  for n,c,d in zip(normals,b0,b1):
   a=c-dot(n,v0);b=d-dot(n,v1)
   if b>0:low=max(low,-a/b)
   elif b<0:high=min(high,-a/b)
   elif a<0: high=F(-1)
  if high<low or high<=0:
   exclusion_intervals.append((inds,low,high));continue
  # Every feasible triple has EXACTLY the whole physical interval (0, EPS].
  assert low<=0 and high==EPS
  forms.add((v0,v1))
 assert len(forms)==10
 Vforms=[]
 for v in V:
  matches=[f for f in forms if add(f[0],scale(EPS,f[1]))==v]
  assert len(matches)==1;Vforms.append(matches[0])
 # All face memberships and strict nonincidences remain fixed for 0<epsilon<=EPS.
 for i,(n,c,d) in enumerate(zip(normals,b0,b1)):
  for j,(v0,v1) in enumerate(Vforms):
   a=c-dot(n,v0);b=d-dot(n,v1)
   if j in faces[i]: assert a==b==0
   else: assert a>=0 and a+EPS*b>0
 apex0,apex1=Vforms[apex];assert apex1==(0,0,0)
 volume=(F(0),);moments=[(F(0),)]*3
 from itertools import permutations
 for f in faces:
  for k in range(1,len(f)-1):
   ids=(f[0],f[k],f[k+1])
   rows=[tuple((Vforms[j][0][c]-apex0[c],Vforms[j][1][c]) for c in range(3)) for j in ids]
   wp=(F(0),)
   for perm in permutations(range(3)):
    sign=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
    wp=padd(wp,pscale(F(sign,6),pmul(pmul(rows[0][perm[0]],rows[1][perm[1]]),rows[2][perm[2]])))
   volume=padd(volume,wp)
   for c in range(3):
    cp=(F(apex0[c]+sum(Vforms[j][0][c] for j in ids),4),F(sum(Vforms[j][1][c] for j in ids),4))
    moments[c]=padd(moments[c],pmul(wp,cp))
 assert len(volume)==4 and all(len(p)==5 for p in moments)
 assert volume[1]==volume[2]==0 and all(p[1]==p[2]==0 for p in moments)
 baseline=geometry(tuple(normals[:6]),tuple(offsets[:6]))
 assert volume[0]==baseline[3] and tuple(p[0] for p in moments)==scale(baseline[3],baseline[4])
 assert peval(volume,EPS)>0
 e=I(0,EPS);volI=peval(volume,e);assert volI.lo>0
 gI=tuple(peval(p,e)/volI for p in moments)
 heights=tuple(1-dot(n,gI) for n in normals[:5]);assert min(h.lo for h in heights)>0
 planar=tuple((n[0]/h,n[1]/h) for n,h in zip(normals,heights))
 E=tuple(sub(planar[i+1],planar[i]) for i in range(4))
 r1=(cross2(E[1],E[3]),cross2(E[3],E[0]),I(0),cross2(E[0],E[1]))
 r2=(cross2(E[2],E[3]),I(0),cross2(E[3],E[0]),cross2(E[0],E[2]))
 lam=add(scale(F(1,2),r1),r2);assert min(z.lo for z in lam)>0
 Q=((I(0),I(0)),(I(0),I(0)))
 for i in range(4):Q=matadd(Q,matscale(-lam[i],sym_outer(planar[i],E[i])))
 detQ=Q[0][0]*Q[1][1]-Q[0][1]*Q[1][0]
 assert Q[0][0].lo>0 and detQ.lo>0
 Ti=inv(T);qc=tuple(p+(I(1),) for p in planar);witness_bounds=[]
 for omitted,old in enumerate(OLD_METRICS):
  N=mm(mm(tr(Ti),old),Ti)
  D=tuple(form(N,qc[i],sub(qc[i+1],qc[i])) for i in range(4))
  assert all(D[i].lo>0 for i in range(4) if i!=omitted) and D[omitted].hi<0
  witness_bounds.append(tuple(x.coarse() for x in D))
 return dict(interval=[0,EPS],zero_endpoint_is_pyramid=True,vertex_affine_forms=Vforms,
  excluded_triple_intervals=exclusion_intervals,volume_polynomial=volume,
  moment_polynomials=moments,centroid_bounds=tuple(x.coarse() for x in gI),
  pole_height_bounds=tuple(x.coarse() for x in heights),weight_bounds=tuple(x.coarse() for x in lam),
  stress_bounds=tuple(tuple(x.coarse() for x in r) for r in Q),determinant_bound=detQ.coarse(),
  proper_subsystem_arrow_bounds=witness_bounds)

def main():
 assert __debug__ and sys.version_info>=(3,10)
 normals=[(F(x)-SHIFT[0],F(y)-SHIFT[1],F(1)) for x,y in P]+[(F(0),F(0),F(-3))]
 offsets=[F(1)]*6
 # One generic and two neighbor-passing cuts at the base corner F0/F1/F5.
 corner_planes=(normals[0],normals[1],normals[5])
 for coeff,k in (((1,1,1),1),((1,2,3),2),((1,4,5),3)):
  normals.append(tuple(sum(F(coeff[i])*corner_planes[i][j] for i in range(3)) for j in range(3)))
  offsets.append(sum(coeff)-k*EPS)
 V,faces,edges,vol,g,q,cells,fan2=geometry(tuple(normals),tuple(offsets))
 assert (len(V),len(edges),len(faces))==(10,17,9)
 apex=V.index((F(0),F(0),F(1)))
 assert [i for i,f in enumerate(faces) if apex in f]==list(range(5))
 assert sum(apex in e for e in edges)==5
 for i in range(5):
  edge=set(faces[i])&set(faces[(i+1)%5]);assert len(edge)==2 and apex in edge and tuple(sorted(edge)) in edges
 # Exact local corner description, independent of the global vertex enumeration.
 old_corner=mv(inv(corner_planes),(F(1),F(1),F(1)))
 local_new=((0,1,0),(0,0,1),(F(1,2),0,F(1,2)),(1,F(1,2),0),(3,0,0))
 inv_corner=inv(corner_planes)
 corner_new=tuple(mv(inv_corner,tuple(1-EPS*z for z in p)) for p in local_new)
 assert old_corner not in V and all(v in V for v in corner_new)
 # Natural tangent coordinates on the TRUE polar face at the apex.
 a=sub(V[apex],g); assert a[2]>0
 B=((F(1),F(0),F(0)),(F(0),F(1),F(0)),(-a[0]/a[2],-a[1]/a[2],1/a[2]))
 planar=tuple((v[0],v[1]) for v in q[:5]); qc=tuple(p+(F(1),) for p in planar)
 assert all(mv(B,qc[i])==q[i] for i in range(5))
 E=tuple(sub(planar[i+1],planar[i]) for i in range(4))
 slacks=tuple(cross2(sub(planar[(i+1)%5],planar[i]),sub(planar[j],planar[i])) for i in range(5) for j in range(5) if j not in (i,(i+1)%5))
 assert min(slacks)>0
 r1=(cross2(E[1],E[3]),cross2(E[3],E[0]),F(0),cross2(E[0],E[1]))
 r2=(cross2(E[2],E[3]),F(0),cross2(E[3],E[0]),cross2(E[0],E[2]))
 lam=add(scale(F(1,2),r1),r2);assert min(lam)>0
 assert tuple(sum(lam[i]*E[i][j] for i in range(4)) for j in range(2))==(0,0)
 S=((F(0),F(0)),(F(0),F(0)))
 for i in range(4): S=matadd(S,matscale(lam[i],sym_outer(planar[i],E[i])))
 Q=matscale(-1,S); assert min(minors(Q))>0
 # Stress in original 3D pole coordinates: -A Q A^T, rank two NSD.
 A=tuple(row[:2] for row in B)
 stress=((F(0),)*3,)*3
 for i in range(4): stress=matadd(stress,matscale(lam[i],sym_outer(q[i],sub(q[i+1],q[i]))))
 assert stress==matscale(-1,mm(mm(A,Q),tr(A)))
 witnesses=[]
 # Transport OLD strict witnesses by the initial planar translation and actual plane chart.
 T=((F(1),F(0),-SHIFT[0]),(F(0),F(1),-SHIFT[1]),(F(0),F(0),F(1)))
 L=mm(B,T);Li=inv(L)
 for omitted,old in enumerate(OLD_METRICS):
  N=mm(mm(tr(Li),old),Li);assert min(minors(N))>0
  D=tuple(form(N,q[i],sub(q[i+1],q[i])) for i in range(4))
  assert all(D[i]>0 for i in range(4) if i!=omitted) and D[omitted]<0
  witnesses.append(dict(omitted=omitted,selected_arrows=D,**census(V,faces,edges,g,q,N)))
 report=dict(identity='ACTUAL_E17_DEGREE5_MINIMAL_FOUR_POLAR_ARROWS_V1',
  input=dict(pentagon=P,shift=SHIFT,epsilon=EPS,corner_planes=[0,1,5],cuts=[[[1,1,1],1],[[1,2,3],2],[[1,4,5],3]]),
  normals=normals,offsets=offsets,vertices=V,faces=faces,edges=edges,apex=apex,
  volume=vol,centroid=g,poles=q,positive_fan=cells,apex_fan=fan2,
  tangent_chart=B,planar_points=planar,convexity_slacks=slacks,
  circuits=[r1,r2],weights=lam,positive_stress_2d=Q,stress_minors=minors(Q),stress_3d=stress,
  witnesses=witnesses,family=family(tuple(normals),tuple(offsets),V,faces,apex,T))
 def enc(o):
  if isinstance(o,F): return str(o)
  raise TypeError(type(o))
 data=(json.dumps(report,default=enc,sort_keys=True,indent=2)+'\n').encode()
 output=Path('actual_pentagon_report.json');output.write_bytes(data)
 print('ACTUAL_E17_TRUE_DEGREE5_PENTAGON_ALL_PROPER_SUBSYSTEMS_STRICT_PASS')
 print('VEF',len(V),len(edges),len(faces),'apex',apex,'faces',faces)
 print('ACTUAL_E17_ENTIRE_CUT_INTERVAL_0_LT_EPS_LE_1_1000_PASS')
 print('CENSUS',[(len(w['S']),len(w['U']),len(w['H'])) for w in witnesses])
 for path in (Path(__file__),output):
  raw=path.read_bytes();print(path.name,len(raw),hashlib.sha256(raw).hexdigest())

if __name__=='__main__': main()
```
