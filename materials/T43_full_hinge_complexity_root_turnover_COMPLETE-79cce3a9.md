# material-79cce3a9f66b

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Complete T43 full-hinge atlas, C<=408 family bound, exact finite root protection, and nonrecord C272 turnover

This is a self-contained exact recovery capsule, not achievement of own110. The sole source below contains all43 literal T43 integer rows/1000, the entire plane atlas, finite-velocity polygons, exact own-volume moments, the quadratic old-root protection method, an exact full-hinge body, and every required helper. No prior sandbox, previous source file, archive attachment, numerical library, or FULL76 is required. The input is the literal T43 previously read from [internal-source-reference]. This new capsule also repairs delivery dependence on earlier atlas/pruned materials whose ownership reads failed; it does not rename those old IDs.

## New substantive conclusions
1. Complete geometric eligibility: for an interior plane z=n.x-h and n.v=0, F_v(x)=x+v max(0,z) admits a nonzero convex FULL image iff the crossed-facet cone {v:n.v=0,m_f.v<=0} is nontrivial. Without an original edge in the section this cone is zero. A generic section with exactly one old edge has a nonzero cone iff its endpoint interior angles sum to<=pi. Orient n so n cross(b-a) points into the section; with the unique crossed-facet normals ma,mb at the two endpoints, the exact criterion is n.(ma cross mb)<=0. Removing the old-edge normal from the section's cyclic normal fan leaves a gap2pi-alpha-beta; remaining normals fit a closed semicircle iff this gap>=pi. Critical additional-vertex planes require the full cone test. The projective edge-plane charts split at old-vertex sign changes and at the affine determinant zero. This proves coverage rather than relying on a numerical sample.
2. Exact atlas counts: all123 old edges,5166 vertex-sign chart intervals,5028 interior,238 extra flat-angle cuts,1142 eligible and4124 impossible open cells;4905 edge-indexed critical interior-plane occurrences,1219 eligible. Repeated geometric planes under different edges are NOT unique-plane counts. Chart infinity is included. This is complete geometric eligibility, not an equilibrium-family exclusion.
3. NEW whole-family complexity bound: in every eligible open cell the number k of strictly crossed old edges is constant and lies1..27. On all eligible boundary occurrences it lies1..26 (1197 old-vertex planes,22 chart infinities,238 flat-angle planes). A full image has only the43 original vertex images plus at most k section vertices, so V<=70. Every 3D convex polyhedron satisfies E<=3V-6, hence C=2E<=408 for this ENTIRE single-convex-full-hinge family and every nonsingular affine post-image. Noninterior section planes give affine images with only43 vertices and also satisfy the bound. This does not cover repeated hinges. Thus complexity is safely below500 throughout this family; own strict110/weak000 remains unachieved.
4. NEW exact finite-velocity root test: write c(v)=c+mu v,mu=J/V,J=integral_K z_+ dx, f_i=z_i+,r_i=x_i-c,a_i=f_i-mu. For each other old/section point j, q_ij(v)=(r_i+a_i v).(x_j-x_i+(f_j-f_i)v) equals a constant plus linear term plus a_i(f_j-f_i)||v||^2. Its maximum over the exact rational velocity polygon is attained at a polygon vertex when the scalar quadratic coefficient is nonnegative; when negative, also test stationary points on edges and the unconstrained planar stationary point when feasible. All candidates are rational in an exact tangent basis. Maxima<0 for every j certify the old vertex remains strictly unstable throughout the WHOLE finite polygon. Positive maxima produce exact escape witnesses. A zero closed-support result alone would still require checking true vertex status before classifying weak U.
5. The original plane n=(-325273,-698874,-240310),h=-45275161 protects both old U24/29 throughout its finite velocity polygon. The new plane n=(33745,-31042,-11934),h=-26644117 through old edge0--1 does not: both have exact positive escape witnesses. The full two-plane certificates are reconstructed below. This is a strict extension beyond the old fixed-plane result, NOT a global two-U exclusion.
6. NEW physical counterexample to global old-root protection: use that new plane and choose velocity coordinates equal to1/20 of the sum of the two nonzero vertices of its exact velocity triangle. Include every section point. The reconstructed body is V49/E136/F89,C272, own strict222, additional weak000, primitivezero000. Both original U24/29 disappear; new U are41 and46 (46 is a section vertex). S are facet23 and73 in the output order. Positive primal bar P=.9609628930141586 and polar bar Q=.9981208567747304. It is a genuine finite root/interface replacement, but has not cancelled either unwanted pair and has much deeper bars than T43. Preserve as a useful nonrecord, not a canonical improvement.

Exact velocity in raw-coordinate convention: (-89445591423652877/470883665054119711420,-1834060893299048701/9417673301082394228400,-287741863753498987/9417673301082394228400). All raw output coordinates and COM are divided by1000 for physical coordinates. Raw rational point numerators/denominators need at most83bits, raw COM196bits; unlike the earlier18–19bit pruned controls, this example is not arithmetically simpler.

## Mechanics, proof scope, and orientation
For K={m_f.x<=b_f}, exact convexity is enforced by all lower/upper facet pieces: if min_f z<0 then every old p with z(p)>0 satisfies z(p)(m_f.v)<=b_f-m_f.p; if max_f z>0 then every p with z(p)<0 satisfies -z(p)(m_f.v)<=b_f-m_f.p. Lower supports remain(m,b), upper supports become(m-(m.v)n,b-(m.v)h). These support inequalities make the closed image boundary equal its convex-hull boundary. Full filled volume remains V and M'=M+vJ. The code integrates J by coning clipped upper original facets from an old point on the section; cap terms vanish. It separately reintegrates the completed body's uniform V/M and checks this mass law. The PRUNED old-vertex hull omitting section vertices is a different physical object and does NOT obey this law.
Reversing the moving half is affine-equivalent: F_{-n,v}(x)=(I-v n^T)F_{n,v}(x)+vh, because n.v=0. Thus the two plane orientations have the same convex velocity domain, but generally different Euclidean equilibria. Orientation is redundant only when an unrestricted nonsingular affine post-map is already included. This is an analytic identity, not a numerical family search.

The old T43 hull is recovered by exhaustive exact supporting triples and asserted simplicial. The transformed body uses maximal material facet pieces, verifies every support against every generated point, requires distinct planes and no unlisted coplanar point, reconstructs true edge owners, and explicitly checks rank3 of incident facet normals at EVERY listed vertex. This ensures the49 points are extreme, not subdivisions of true edges. It handles the nonsimplicial facet polygons in this control, but deliberately rejects a boundary velocity where material facet pieces merge; it is not advertised as a general degenerate-hull auditor. Every own-centred strict and closed S/U/H predicate is tested, including both edge-foot bounds and both normal-cone coefficients. No primitive zero occurs. Every positive primal/polar bar is preserved on TRUE edges, with full component, cut, attaining edge and path. No bar floor or inferred Euler-only census is used. One exact implementation with redundant support/moment/cone checks is not an independent second engine.

## Reconstruction
Save the sole code block as T43_hinge_atlas_and_turnover_recovery.py including final newline:17773bytes SHA256 c68703403c31dcef466a5ded85a353ed98b8e58b755d57b304c3dcab81fb0c1c. Verified environment CPython3.13.5 standard library only. Execute `python -B -S T43_hinge_atlas_and_turnover_recovery.py`.
Expected markers EXACT_HINGE_PLANE_ATLAS_PASS with counts above; EXACT_FULL_HINGE_COMPLEXITY_PASS27 70 408; EXACT_FULL_HINGE_TURNOVER_PASS[49,136,89]272[2,2,2][0,0,0][0,0,0],U[41,46],S[23,73],old_root_escapeTrue True; EXACT_ROOT_PROTECTION_PASS[[True,True],[False,False]].
Reproduced files:
T43_HINGE_ELIGIBILITY_ATLAS.json1991140bytes SHA1625d61c49eeb6e58bbf06a9d438e1d405d2b62b9c489a8e7bb86e3416ba882a.
T43_HINGE_COMPLEXITY_COUNTS.json784bytes SHAe37a293795589880f90f1bd3e4b17e6394f5fba851cfe6c1be4f779233cd6f1a.
T43_FULL_HINGE_ROOT_TURNOVER.json28568bytes SHAfd97dee5919f820b239604377b30cfa07d0f32fe7223cab4b547fde1023ab4f1.
T43_TWO_PLANES_ROOT_PROTECTION.json127762bytes SHA7c2e2081ce28d641c2289eb46ddd56de4d326a1eb1e46e9b3ce1efa2a221ce95.
The former17596byte draft omitted the extreme-vertex-rank assertion; this17773byte final unit is authoritative. All reproduced outputs are unchanged. Canonical own110 remainsC622; no own110<500 is being claimed.

```python
"""New finite-hinge atlas implementation; literal T43 input from immutable recovery."""
from fractions import Fraction as F
from itertools import combinations
from collections import defaultdict
import math,json
P0=[[-1131,-380,23],[-1127,-283,-218],[-1086,-225,-391],[-1013,-181,-547],[-945,-683,646],[-931,-156,-666],[-871,-801,885],[-869,-137,-738],[-780,-129,-818],[-668,-131,-892],[-635,202,-115],[-589,230,-7],[-559,224,54],[-528,217,107],[-496,331,-186],[-445,199,212],[-382,425,-214],[-366,407,-88],[-316,410,9],[-307,448,-285],[-230,462,-332],[-215,439,46],[-128,476,-366],[-30,481,-367],[-2,-201,-1240],[126,415,143],[140,485,-321],[295,502,-44],[325,457,97],[385,-951,2433],[389,393,124],[432,342,135],[462,305,132],[491,268,127],[517,230,121],[553,-80,-600],[564,161,93],[602,94,61],[633,24,23],[657,-49,-23],[674,-125,-78],[675,-281,-220],[681,-203,-143]]
P=[tuple(x) for x in P0]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(a,t):return tuple(t*x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def primitive(a):
 g=math.gcd(*a);return tuple(x//g for x in a)
def hull(X):
 faces=[]; edges=defaultdict(list)
 for ids in combinations(range(len(X)),3):
  a,b,c=[X[i] for i in ids];m=cross(sub(b,a),sub(c,a))
  if not any(m):continue
  h=dot(m,a);s=[dot(m,p)-h for p in X]
  if min(s)<0<max(s) or min(s)==max(s):continue
  if max(s)>0:m=mul(m,-1);ids=(ids[0],ids[2],ids[1])
  assert s.count(0)==3
  m=primitive(m);h=dot(m,a);fi=len(faces);faces.append((ids,m,h))
  for e in combinations(ids,2):edges[tuple(sorted(e))].append(fi)
 assert all(len(x)==2 for x in edges.values()); assert len(X)-len(edges)+len(faces)==2
 return faces,dict(edges)
faces,edges=hull(P)

"""Exact finite-velocity polygons, uniform mass and old-root protection of T43.
The complete literal input and all necessary functions are included in this unit.
All arithmetic after the literal input uses int/Fraction. No sampling in velocity.
"""
from fractions import Fraction as F
from pathlib import Path
import json,math,sys,hashlib,time
W=sum(det(*(P[i] for i in f)) for f,m,h in faces)
V=F(W,6)
C=tuple(F(sum(det(*(P[i] for i in f))*sum(P[i][k] for i in f) for f,m,h in faces),4*W) for k in range(3))

def tidy(poly):
 out=[]
 for p in poly:
  if not out or p!=out[-1]:out.append(p)
 if len(out)>1 and out[0]==out[-1]:out.pop()
 return out

def clip(poly,a,b):
 out=[]
 if not poly:return out
 for p,q in zip(poly,poly[1:]+poly[:1]):
  f=dot(a,p)-b;g=dot(a,q)-b
  if f<=0:out.append(p)
  if (f<0<g) or (g<0<f):out.append(add(p,mul(sub(q,p),F(f,f-g))))
 return tidy(out)

def finite_domain(n,h):
 z=[dot(n,p)-h for p in P]
 assert min(z)<0<max(z)
 k=min(range(3),key=lambda k:abs(n[k]));e=tuple(int(i==k) for i in range(3))
 u=primitive(cross(n,e));w=primitive(cross(n,u));basis=[u,w]
 bounds=[]
 for ids,m,b in faces:
  lo=min(z[i] for i in ids);hi=max(z[i] for i in ids);cand=[]
  for p,zz in zip(P,z):
   if lo<0<zz:cand.append(F(b-dot(m,p),zz))
   if hi>0>zz:cand.append(F(b-dot(m,p),-zz))
  assert cand
  bounds.append((tuple(dot(m,t) for t in basis),min(cand)))
 assert all(b>=0 for a,b in bounds)
 size=F(1)
 while True:
  poly=[(-size,-size),(size,-size),(size,size),(-size,size)]
  for a,b in bounds:poly=clip(poly,a,b)
  assert poly
  # If the intersection has no box-boundary point, convexity proves D is inside.
  if all(abs(x)<size for p in poly for x in p):break
  size*=2
  if size>2**100:raise RuntimeError('Unresolved exact bounding search')
 return z,basis,bounds,poly

def mass_section(n,h,z):
 # An exact coning origin on H; no section-cap triangulation is needed.
 zeros=[i for i,s in enumerate(z) if not s]
 assert zeros
 o=P[zeros[0]];J=F(0);VU=F(0);MU=(F(0),)*3
 for ids,m,b in faces:
  poly=clip([P[i] for i in ids],mul(n,-1),-h)
  for j in range(1,len(poly)-1):
   a,bb,c=poly[0],poly[j],poly[j+1]
   D=det(sub(a,o),sub(bb,o),sub(c,o));assert D>=0
   VU+=F(D,6);MU=add(MU,mul(add(add(o,a),add(bb,c)),F(D,24)))
   J+=F(D,24)*(dot(n,a)+dot(n,bb)+dot(n,c)-3*h)
 assert J==dot(n,MU)-h*VU and J>0
 section=[]
 for a,b in edges:
  if z[a]*z[b]<0:
   section.append(mul(sub(mul(P[b],z[a]),mul(P[a],z[b])),F(1,z[a]-z[b])))
 return J/V,section,dict(J=J,upper_volume=VU,upper_moment=MU)

def quadratic_max(c,l,k,basis,bounds,poly):
 def val(t):
  v=add(mul(basis[0],t[0]),mul(basis[1],t[1]))
  return c+dot(l,t)+k*dot(v,v)
 candidates=[(val(p),p,'vertex') for p in poly]
 if k<0:
  for p,q in zip(poly,poly[1:]+poly[:1]):
   d=sub(q,p)
   if not any(d):continue
   vp=add(mul(basis[0],p[0]),mul(basis[1],p[1]));vd=add(mul(basis[0],d[0]),mul(basis[1],d[1]))
   t=-F(dot(l,d)+2*k*dot(vp,vd),2*k*dot(vd,vd))
   if 0<t<1:
    x=add(p,mul(d,t));candidates.append((val(x),x,'edge_stationary'))
  a=dot(basis[0],basis[0]);b=dot(basis[0],basis[1]);cc=dot(basis[1],basis[1]);ds=a*cc-b*b
  x=(-F(cc*l[0]-b*l[1],2*k*ds),-F(a*l[1]-b*l[0],2*k*ds))
  if all(dot(aa,x)<=bb for aa,bb in bounds):candidates.append((val(x),x,'interior_stationary'))
 return max(candidates,key=lambda t:t[0])

def audit_plane(n,h,roots=(24,29)):
 z,basis,bounds,poly=finite_domain(n,h);mu,sec,mm=mass_section(n,h,z)
 X=P+sec;ff=[max(0,zz) for zz in z]+[F(0)]*len(sec);out=[]
 for i in roots:
  r=sub(X[i],C);a=ff[i]-mu;rows=[]
  for j,x in enumerate(X):
   if j==i:continue
   d=sub(x,X[i]);delta=ff[j]-ff[i];lv=add(mul(d,a),mul(r,delta));l=tuple(dot(lv,u) for u in basis)
   m,t,kind=quadratic_max(dot(r,d),l,a*delta,basis,bounds,poly)
   rows.append(dict(j=j,maximum=m,velocity_coordinates=t,where=kind))
  worst=max(rows,key=lambda d:d['maximum'])
  out.append(dict(root=i,strictly_protected=worst['maximum']<0,closed_protected=worst['maximum']<=0,worst=worst,all_witness_bounds=rows))
 return dict(n=n,h=h,basis=basis,polygon=poly,section_points=sec,mu=mu,mass=mm,roots=out)

def serial(o):
 if isinstance(o,F):return str(o)
 if isinstance(o,dict):return {str(k):serial(v) for k,v in o.items()}
 if isinstance(o,(list,tuple)):return [serial(v) for v in o]
 return o


def chord(a,b):
 A=dot(a,a);B=dot(a,b);C=dot(b,b)
 if B>=A:return A
 if B>=C:return C
 return F(A*C-B*B,A+C-2*B)

def bars(X,EE):
 rr=[dot(x,x) for x in X];ed=sorted([(chord(X[i],X[j]),i,j) for i,j in EE],key=lambda a:(-a[0],a[1],a[2]))
 par=list(range(len(X)));peaks=par.copy();out=[]
 def root(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 for death,u,v in ed:
  i,j=root(u),root(v)
  if i==j:continue
  if (rr[peaks[i]],-peaks[i])<(rr[peaks[j]],-peaks[j]):i,j=j,i
  birth=rr[peaks[j]]
  if birth>death:out.append({'root':peaks[j],'elder':peaks[i],'birth':birth,'death':death,'depth':F(birth-death,birth)})
  par[j]=i
 for o in out:
  adj=defaultdict(list);inc=defaultdict(list)
  for val,u,v in ed:
   if val>o['death']:adj[u].append(v);adj[v].append(u)
   if val>=o['death']:inc[u].append(v);inc[v].append(u)
  comp={o['root']};stack=[o['root']]
  for u in stack:
   for v in adj[u]:
    if v not in comp:comp.add(v);stack.append(v)
  cut=[(val,u,v) for val,u,v in ed if (u in comp)!=(v in comp)]
  assert max(val for val,u,v in cut)==o['death']
  stack=[o['root']];prev={o['root']:None}
  for u in stack:
   if u==o['elder']:break
   for v in sorted(inc[u]):
    if v not in prev:prev[v]=u;stack.append(v)
  assert o['elder'] in prev
  path=[o['elder']]
  while path[-1]!=o['root']:path.append(prev[path[-1]])
  path.reverse()
  assert min(chord(X[i],X[j]) for i,j in zip(path,path[1:]))==o['death']
  o.update(component=sorted(comp),cut=sorted([i,j] for val,i,j in cut),attaining=sorted([i,j] for val,i,j in cut if val==o['death']),path=path)
 return sorted(out,key=lambda b:(-b['depth'],b['root']))


"""Exact full-hinge material-facet audit, with every exact source dependency included.
All half-space support, own filled mass and closed/strict predicates are exact.
"""
from collections import defaultdict

def plane_key(n,b):
 a=list(n)+[b];L=math.lcm(*(F(x).denominator for x in a));a=[int(x*L) for x in a];g=math.gcd(*a)
 return tuple(x//g for x in a)

def build(n,h,uv):
 z,basis,bounds,poly=finite_domain(n,h)
 assert all(dot(a,uv)<=b for a,b in bounds)
 v=add(mul(basis[0],uv[0]),mul(basis[1],uv[1]));assert dot(n,v)==0
 mu,sec,mass=mass_section(n,h,z);c=add(C,mul(v,mu));XX=[];table={};FF=[];keys=set()
 def vid(p):
  if p not in table:table[p]=len(XX);XX.append(p)
  return table[p]
 # Keep original material labels for all old vertices, then true crossing points.
 for p,zz in zip(P,z):vid(add(p,mul(v,max(0,zz))))
 for p in sec:vid(p)
 for ids,m,b in faces:
  for high in (False,True):
   pp=clip([P[i] for i in ids],mul(n,-1) if high else n,-h if high else h)
   if len(pp)<3:continue
   if all(dot(n,p)==h for p in pp):continue
   pp=[add(p,mul(v,max(0,dot(n,p)-h))) for p in pp]
   ii=[vid(p) for p in pp];mv=dot(m,v);nn=sub(m,mul(n,mv)) if high else m;hh=b-mv*h if high else b
   key=plane_key(nn,hh)
   assert key not in keys,'This audit requires distinct maximal material facet pieces'
   keys.add(key);FF.append((ii,nn,hh))
 assert set(i for f,m,b in FF for i in f)==set(range(len(XX)))
 ee=defaultdict(list)
 for fi,(ids,m,b) in enumerate(FF):
  assert all(dot(m,p)<=b for p in XX)
  assert {j for j,p in enumerate(XX) if dot(m,p)==b}==set(ids)
  assert dot(m,sub(XX[ids[0]],c))>0
  for a,bb in zip(ids,ids[1:]+ids[:1]):ee[tuple(sorted((a,bb)))].append(fi)
 for i in range(len(XX)):
  incident=[m for ids,m,b in FF if i in ids]
  assert any(det(a,b,c)!=0 for a,b,c in combinations(incident,3)),'Listed point is not an extreme vertex'
 assert all(len(f)==2 for f in ee.values()) and len(XX)-len(ee)+len(FF)==2
 vv=F(0);mm=(F(0),)*3
 for ids,nf,b in FF:
  for j in range(1,len(ids)-1):
   a,bb,cc=[XX[i] for i in (ids[0],ids[j],ids[j+1])];D=det(sub(a,c),sub(bb,c),sub(cc,c));assert D>0
   vv+=F(D,6);mm=add(mm,mul(add(add(c,a),add(bb,cc)),F(D,24)))
 assert vv==V and mm==mul(c,V)
 Z=[sub(p,c) for p in XX];strict=[[],[],[]];weak=[[],[],[]];zeros=[0,0,0]
 def test(k,label,a):
  zeros[k]+=sum(t==0 for t in a)
  if min(a)>=0:(strict if min(a)>0 else weak)[k].append(label)
 for i,p in enumerate(Z):test(1,i,[-dot(p,sub(q,p)) for j,q in enumerate(Z) if j!=i])
 for fi,(ids,m,b) in enumerate(FF):test(0,fi,[dot(m,cross(Z[a],Z[bb])) for a,bb in zip(ids,ids[1:]+ids[:1])])
 for (i,j),(f,g) in sorted(ee.items()):
  p=Z[i];d=sub(Z[j],p);d2=dot(d,d);t=-dot(p,d);q=add(mul(p,d2),mul(d,t));m,nn=FF[f][1],FF[g][1]
  aa=dot(m,m);bb=dot(m,nn);cc=dot(nn,nn);dd=aa*cc-bb*bb;assert dd>0
  l=cc*dot(q,m)-bb*dot(q,nn);k=aa*dot(q,nn)-bb*dot(q,m)
  assert mul(q,dd)==add(mul(m,l),mul(nn,k))
  test(2,[i,j],[t,d2-t,l,k])
 Q=[mul(m,F(1,b-dot(m,c))) for ids,m,b in FF];PB=bars(Z,sorted(ee));QB=bars(Q,sorted(tuple(sorted(f)) for f in ee.values()))
 assert len(PB)==len(strict[1])-1 and len(QB)==len(strict[0])-1
 return dict(normal=n,offset=h,uv=uv,velocity=v,centroid_raw=c,volume_raw=V,coordinate_scale=1000,points_raw=XX,facets=[f[0] for f in FF],support_planes=[[list(m),b] for f,m,b in FF],edges=sorted(ee),VEF=[len(XX),len(ee),len(FF)],C=2*len(ee),strict=strict,weak=weak,primitive_zero_counts=zeros,P=PB,Q=QB,root24_witnesses=[j for j,p in enumerate(Z) if j!=24 and dot(Z[24],sub(p,Z[24]))>0],root29_witnesses=[j for j,p in enumerate(Z) if j!=29 and dot(Z[29],sub(p,Z[29]))>0])


"""Exact open-chart eligibility atlas of convex FULL T43 hinges.
All literal input is included in this complete unit. No floating arithmetic.
This does not solve finite-amplitude equilibrium cancellation.
"""
from fractions import Fraction as F
from pathlib import Path
import json,math,hashlib

def integer_normal(n0,n1,t):
 return primitive(add(mul(n0,t.denominator),mul(n1,t.numerator)))
def interior(n,a):
 zz=[dot(n,sub(p,P[a])) for p in P]
 return min(zz)<0<max(zz),zz

def crossed(zz):
 return [f for f,(ids,m,h) in enumerate(faces) if min(zz[i] for i in ids)<0<max(zz[i] for i in ids)]
def tangent_rays(n,fs):
 ns=[faces[f][1] for f in fs];rays=set()
 for m in ns:
  r=cross(n,m)
  if not any(r):continue
  r=primitive(r)
  for v in (r,mul(r,-1)):
   if all(dot(mm,v)<=0 for mm in ns):rays.add(v)
 return sorted(rays)

def sample(lo,hi):
 if lo is None:return hi-1 if hi is not None else F(0)
 if hi is None:return lo+1
 return (lo+hi)/2

def local_test(n,e,zz):
 a,b=e;d=sub(P[b],P[a]);u=cross(n,d)
 em=[faces[f][1] for f in edges[e]]
 su=[dot(m,u) for m in em]
 assert su[0]*su[1]>0
 if su[0]>0:n=mul(n,-1);u=mul(u,-1)
 fs=crossed(zz)
 aa=[f for f in fs if a in faces[f][0]];bb=[f for f in fs if b in faces[f][0]]
 assert len(aa)==len(bb)==1
 ma,mb=faces[aa[0]][1],faces[bb[0]][1]
 assert dot(ma,d)<0<dot(mb,d)
 turn=dot(n,cross(ma,mb))
 rays=tangent_rays(n,fs)
 assert bool(rays)==(turn<=0), (e,n,turn,rays)
 return turn,aa[0],bb[0],rays,n

def serialize(o):
 if isinstance(o,F):return str(o)
 if isinstance(o,dict):return {str(k):serialize(v) for k,v in o.items()}
 if isinstance(o,(tuple,list)):return [serialize(v) for v in o]
 return o

def run():
 out=[];counts={'old_edges':len(edges),'vertex_sign_intervals':0,'interior_intervals':0,'eligible_open_cells':0,'ineligible_open_cells':0,'flat_endpoint_cuts':0,'critical_interior_planes':0,'critical_eligible_planes':0}
 for e in sorted(edges):
  a,b=e;d=sub(P[b],P[a]);axis=min(range(3),key=lambda k:abs(d[k]));base=tuple(int(k==axis) for k in range(3));n0=primitive(cross(d,base));n1=primitive(cross(d,n0));assert any(n0) and any(n1)
  aa=[dot(n0,sub(p,P[a])) for p in P];bb=[dot(n1,sub(p,P[a])) for p in P]
  crit=sorted(set(F(-q,r) for q,r in zip(aa,bb) if r))
  cuts=[None]+crit+[None];rows=[];boundary=[]
  for lo,hi in zip(cuts,cuts[1:]):
   counts['vertex_sign_intervals']+=1;t=sample(lo,hi);n=integer_normal(n0,n1,t);ok,zz=interior(n,a)
   if not ok:continue
   counts['interior_intervals']+=1
   turn,fa,fb,rays,nor=local_test(n,e,zz)
   crossm=cross(faces[fa][1],faces[fb][1]);A=dot(n0,crossm);B=dot(n1,crossm)
   kink=F(-A,B) if B else None
   split=kink is not None and (lo is None or lo<kink) and (hi is None or kink<hi)
   subcuts=[lo,kink,hi] if split else [lo,hi]
   for ll,hh in zip(subcuts,subcuts[1:]):
    tt=sample(ll,hh);nn=integer_normal(n0,n1,tt);ok,z=interior(nn,a);assert ok
    turn,fa2,fb2,rr,nor=local_test(nn,e,z);assert (fa,fb)==(fa2,fb2)
    eligible=turn<=0;counts['eligible_open_cells' if eligible else 'ineligible_open_cells']+=1
    rows.append(dict(lo=ll,hi=hh,eligible=eligible,endpoint_facets=[fa,fb],sample=tt,normal=nor,rays=rr,turn=turn))
   if split:
    nn=integer_normal(n0,n1,kink);ok,z=interior(nn,a);turn,fa2,fb2,rr,nor=local_test(nn,e,z);assert turn==0 and len(rr)==1
    counts['flat_endpoint_cuts']+=1;boundary.append(dict(t=kink,kind='flat_endpoint',normal=nor,rays=rr))
  for tt in crit+[None]:
   nn=n1 if tt is None else integer_normal(n0,n1,tt);ok,z=interior(nn,a)
   if not ok:continue
   rr=tangent_rays(nn,crossed(z));counts['critical_interior_planes']+=1
   if rr:counts['critical_eligible_planes']+=1
   boundary.append(dict(t=tt,kind='projective_infinity' if tt is None else 'old_vertex',normal=nn,rays=rr,zero_vertices=[i for i,s in enumerate(z) if s==0]))
  out.append(dict(edge=e,n0=n0,n1=n1,cells=rows,boundaries=boundary))
 return dict(counts=counts,edges=out,scope='Complete exact projective plane eligibility atlas per labelled old edge; boundary planes may appear under more than one edge. No finite-amplitude own-equilibrium exclusion.')



def complexity_census(atlas):
 from collections import Counter
 hist=Counter();boundary=Counter();kind=Counter()
 for item in atlas['edges']:
  for row in item['cells']:
   if not row['eligible']:continue
   n=row['normal'];h=dot(n,P[item['edge'][0]]);z=[dot(n,p)-h for p in P]
   hist[sum(z[a]*z[b]<0 for a,b in edges)]+=1
  for row in item['boundaries']:
   if not row['rays']:continue
   n=row['normal'];h=dot(n,P[item['edge'][0]]);z=[dot(n,p)-h for p in P]
   boundary[sum(z[a]*z[b]<0 for a,b in edges)]+=1;kind[row['kind']]+=1
 k=max(max(hist),max(boundary))
 return dict(open_cell_crossing_histogram=dict(sorted(hist.items())),boundary_crossing_histogram=dict(sorted(boundary.items())),boundary_kinds=dict(kind),max_crossings=k,max_vertices=len(P)+k,safe_C=6*(len(P)+k)-12,scope='Complete eligible geometric-plane atlas; finite convex full images and their nonsingular affine images have at most43+27 vertices. Does not determine their equilibria.')

def save_exact(name,obj):
 raw=(json.dumps(serial(obj),sort_keys=True,separators=(',',':'))+'\n').encode();path=Path(__file__).with_name(name);path.write_bytes(raw)
 print('RECOVERED',name,len(raw),hashlib.sha256(raw).hexdigest(),flush=True)

if __name__=='__main__':
 atlas=run();save_exact('T43_HINGE_ELIGIBILITY_ATLAS.json',atlas)
 print('EXACT_HINGE_PLANE_ATLAS_PASS',atlas['counts'],flush=True)
 counts=complexity_census(atlas);save_exact('T43_HINGE_COMPLEXITY_COUNTS.json',counts)
 print('EXACT_FULL_HINGE_COMPLEXITY_PASS',counts['max_crossings'],counts['max_vertices'],counts['safe_C'],flush=True)
 n=(33745,-31042,-11934);h=dot(n,P[0]);z,b,bounds,p=finite_domain(n,h);a=[x for x in p if any(x)];assert len(a)==2
 uv=mul(add(a[0],a[1]),F(1,20));o=build(n,h,uv);save_exact('T43_FULL_HINGE_ROOT_TURNOVER.json',o)
 print('EXACT_FULL_HINGE_TURNOVER_PASS',o['VEF'],o['C'],list(map(len,o['strict'])),list(map(len,o['weak'])),o['primitive_zero_counts'],'U',o['strict'][1],'S',o['strict'][0],'old_root_escape',bool(o['root24_witnesses']),bool(o['root29_witnesses']),'P',[float(q['depth']) for q in o['P']],'Q',[float(q['depth']) for q in o['Q']],flush=True)
 roots=[audit_plane((-325273,-698874,-240310),-45275161),audit_plane(n,h)]
 save_exact('T43_TWO_PLANES_ROOT_PROTECTION.json',roots)
 print('EXACT_ROOT_PROTECTION_PASS',[[r['strictly_protected'] for r in o['roots']] for o in roots],flush=True)
```
