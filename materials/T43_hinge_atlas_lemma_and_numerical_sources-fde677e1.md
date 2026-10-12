# material-fde677e1eca6

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Finite full hinge: rigidity, edge-plane atlas and exact discovery-source units

This records a geometric lemma and finite numerical exploration, NOT a new own110 body or an exhaustive exclusion. Exact T43 input is from fully read [internal-source-reference] SHA d62d046640d6365501698bb41185ba3e351e043f8935a5c0a02bd3654d2deb00. Its earlier fixed-plane exact controls and auditor remain authoritative. The literal T43 rows are included here as a complete runnable dependency.

## Convexity and rigidity lemma
Let bounded full-dimensional K have maximal supports m_f.x<=b_f, and let H={n.x=h} cut its interior. Put z(x)=n.x-h, n.v=0 and F_v(x)=x+v max(0,z(x)). This is an invertible determinant-one PL map. A lower original facet piece keeps support(m_f,b_f); an upper piece has support(m_f-(m_f.v)n,b_f-(m_f.v)h). The entire filled image F_v(K), NOT merely the convex hull of moved old vertices, is convex exactly when all its nonempty boundary facet pieces support all transformed vertices. Sufficient finite inequalities are also necessary:
- whenever min_f z<0, every old p with z(p)>0 obeys z(p)(m_f.v)<=b_f-m_f.p;
- whenever max_f z>0, every old p with z(p)<0 obeys -z(p)(m_f.v)<=b_f-m_f.p.
Section vertices satisfy inherited supports. These inequalities make every image boundary piece lie on the boundary of the convex hull of the image; the embedded closed boundary sphere must then equal that hull boundary. This proves sufficiency, not just local necessity.

A crossed facet has min_f z<0<max_f z and forces m_f.v<=0. All other nontrivial inequalities have positive right sides at v=0. Therefore a nonzero sufficiently small convex hinge exists exactly when the cone T_H={v:n.v=0,m_f.v<=0 for all crossed f} is nontrivial. This cone is the exact tangent cone of the finite admissible-velocity polygon, not a numerical near-zero decision.

If H contains no original edge, every boundary edge of bounded planar section K intersect H is induced by a crossed facet. Their projected outward normals positively span H's direction plane, so T_H={0}. Thus every nonzero convex full hinge cutting the interior MUST have a section plane containing an original edge. Containing such an edge is NOT sufficient: remaining crossed normals can still positively span the plane.

## Finite rational atlas, not a completed exhaustive solve
For old edge a--b take a rational basis n0,n1 perpendicular to b-a and parameterize n(t)=n0+t n1,h(t)=n(t).a. Signs z_i(t) change at finitely many rational parameters. In each open interval crossed facets are fixed. Each velocity upper bound is a minimum of constant slack divided by a positive affine function z_i(t); active quotients switch at linear comparison roots. In tangent basis (b-a,n(t) cross(b-a)), velocity polygon coefficients are rational functions, and its nondegenerate vertex formulas are rational. Section vertices and upper-half volume/first moment/J are rational on fixed-combinatorics charts. Cover the missing projective direction and both orientations explicitly. Subsequent equilibrium conditions at the true centroid are semi-algebraic. None of this asserts that every chart has been solved.

For the FULL filled image, volume V'=V and first moment M'=M+vJ, J=integral_K max(0,z)dx; hence c'=c+vJ/V. These formulas are NOT valid for the pruned hull that omits section vertices. Under an explicit noncollapse hypothesis retaining all original vertices/edges/facets, k new crossing points and c genuinely split facets give combinatorial V_new=V_old+k,F_new=F_old+c,E_new=E_old+k+c. When in-plane old edges form q disjoint nonempty paths along the section boundary, k=c-q. The known T43 plane contains old edge15--29, k23,c24: nominal E170, versus E169 on a boundary ray with one unsplit face. Do not apply these counts at arbitrary degeneracies.

## Scope and limitations of the numerical source below
Save both code blocks with final newlines. Environment used for discovery: CPython3.13.5,NumPy2.3.5,SciPy1.17.0. Run `python hinge_atlas.py` to print43 vertices,123 edges,82 facets and the old fixed-plane section counts. Run `python hinge_numeric.py rootedges` to explore old edges incident to24 or29, third-vertex critical planes and one midpoint per angular interval on ONE halfturn. It samples numerical velocity polygons; it does not exhaust the oriented-plane atlas. The bounding box1e8, zero thresholds and plane merge tolerances are numerical conveniences. Apparent S1/U2 nominations disagreeing with positive Q bars were rejected; no new exact121/211/110 was accepted. The all-pair chord barcode in this discovery source suppresses depths<=1e-12 and is a SCREEN ONLY. Exact accepted controls elsewhere use all true edges and no positive-bar threshold. No finite failure here is a family exclusion.

hinge_atlas.py:2289bytes SHA256 f8e19b2d6f5f5ae1aaddb4fabbc4e38126332de881c881b68caeadd1328d3e5b.
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
if __name__=='__main__':
 n=(-325273,-698874,-240310);h=-45275161
 z=[dot(n,p)-h for p in P]
 print('counts',len(P),len(edges),len(faces))
 print('z0',[i for i,x in enumerate(z) if not x])
 print('inplane_edges',[e for e in edges if all(z[i]==0 for i in e)])
 print('crossed_edges',sum(z[a]*z[b]<0 for a,b in edges))
 print('crossed_faces',sum(min(z[i] for i in ids)<0<max(z[i] for i in ids) for ids,m,h in faces))
```

hinge_numeric.py:5594bytes SHA256 2ce18301abf87c61abb48db371ec249159326abf61346deab14a208a6cfb8728.
```python
"""Finite discovery on moving edge-aligned hinge planes; exact T43 is imported.
Numerical counts are nominations only, not weak-equilibrium certificates.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np
from scipy.spatial import ConvexHull
from hinge_atlas import P,faces,edges
import json,time,math
X=np.array(P,dtype=float)/1000
FI=np.array([f[0] for f in faces]);E=np.array(list(edges))
N=np.array([f[1] for f in faces],float);H=np.array([f[2] for f in faces],float)/1000
L=np.linalg.norm(N,axis=1);N/=L[:,None];H/=L
SL=H[:,None]-N@X.T
SL[np.abs(SL)<1e-12]=0
# Exact oriented simplicial input determines filled moment, not surface mean.
W=np.einsum('ij,ij->i',X[FI[:,0]],np.cross(X[FI[:,1]],X[FI[:,2]]))
V=W.sum()/6;C=np.einsum('i,ij->j',W,X[FI].sum(1))/(4*W.sum())

def domain(n,h):
 z=X@n-h
 z[np.abs(z)<1e-12]=0
 lo=np.min(z[FI],axis=1);hi=np.max(z[FI],axis=1)
 pos=np.flatnonzero(z>0);neg=np.flatnonzero(z<0)
 if not len(pos) or not len(neg):return None
 B=np.full(len(N),np.inf)
 aa=lo<0;bb=hi>0
 B[aa]=np.min(SL[aa][:,pos]/z[pos],axis=1)
 B[bb]=np.minimum(B[bb],np.min(SL[bb][:,neg]/(-z[neg]),axis=1))
 assert np.isfinite(B).all()
 k=np.argmin(abs(n));u=np.cross(n,np.eye(3)[k]);u/=np.linalg.norm(u);w=np.cross(n,u)
 basis=np.array([u,w]).T;A=N@basis
 poly=[np.array(x,float) for x in [(-1e8, -1e8),(1e8,-1e8),(1e8,1e8),(-1e8,1e8)]]
 for a,b in zip(A,B):
  if not poly:break
  new=[]
  for p,q in zip(poly,poly[1:]+poly[:1]):
   f=a@p-b;g=a@q-b
   if f<=1e-13:new.append(p)
   if (f<0<g) or (g<0<f):new.append(p+(q-p)*(f/(f-g)))
  poly=new
 if not poly:return None
 poly=np.array(poly);poly=poly[np.r_[True,np.linalg.norm(np.diff(poly,axis=0),axis=1)>1e-9]]
 if np.max(np.linalg.norm(poly,axis=1))<1e-8:return None
 if np.max(abs(poly))>9e7: return None # unresolved huge numerical domain is not an exclusion
 crossmask=z[E[:,0]]*z[E[:,1]]<0
 ee=E[crossmask];zz=z[ee]
 CP=(zz[:,0,None]*X[ee[:,1]]-zz[:,1,None]*X[ee[:,0]])/(zz[:,0]-zz[:,1])[:,None]
 upper=np.vstack([X[z>=0],CP]);hu=ConvexHull(upper)
 ff=hu.simplices.copy();oriented=np.einsum('ij,ij->i',np.cross(upper[ff[:,1]]-upper[ff[:,0]],upper[ff[:,2]]-upper[ff[:,0]]),hu.equations[:,:3])
 ff[oriented<0]=ff[oriented<0][:, [0,2,1]]
 d=np.einsum('ij,ij->i',upper[ff[:,0]],np.cross(upper[ff[:,1]],upper[ff[:,2]]))
 Vu=d.sum()/6;Mu=np.einsum('i,ij->j',d,upper[ff].sum(1))/24
 J=n@Mu-h*Vu
 return dict(n=n,h=h,z=z,lo=lo,hi=hi,poly=poly,basis=basis,CP=CP,J=J,AA=A,B=B)

def evald(d,uv):
 v=d['basis']@uv;Y=np.vstack([X+np.maximum(0,d['z'])[:,None]*v,d['CP']]);c=C+v*d['J']/V
 ns=[];hs=[]
 for m,b,l,r in zip(N,H,d['lo'],d['hi']):
  mv=m@v
  if l<0:ns.append(m);hs.append(b)
  if r>0:
   a=m-mv*d['n'];s=b-mv*d['h']
   if l<0 and abs(mv)<1e-10:continue
   ns.append(a);hs.append(s)
 ns=np.array(ns);hs=np.array(hs);Q=ns/(hs-ns@c)[:,None];P=Y-c
 def roots(Z):
  rr=np.einsum('ij,ij->i',Z,Z);D=Z@Z.T-rr[:,None];np.fill_diagonal(D,-np.inf)
  m=np.max(D,axis=1)/rr
  return np.flatnonzero(m< -1e-9),m
 up,mp=roots(P);sq,mq=roots(Q)
 return dict(S=len(sq),U=len(up),up=up.tolist(),sq=sq.tolist(),p_min=float(np.min(mp)),q_min=float(np.min(mq)),Y=Y,c=c,P=P,Q=Q,v=v)

def bar(Z):
 rr=np.einsum('ij,ij->i',Z,Z);ii,jj=np.triu_indices(len(Z),1);A=rr[ii];B=np.einsum('ij,ij->i',Z[ii],Z[jj]);D=rr[jj]
 vals=np.where(B>=A,A,np.where(B>=D,D,(A*D-B*B)/(A+D-2*B)))
 par=np.arange(len(Z));birth=rr.copy();out=[]
 def root(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 for k in np.argsort(-vals):
  i,j=root(ii[k]),root(jj[k])
  if i==j:continue
  if birth[i]<birth[j]:i,j=j,i
  dep=(birth[j]-vals[k])/birth[j]
  if dep>1e-12:out.append(float(dep))
  par[j]=i
 return sorted(out,reverse=True)

def nom(d,q,e,third=None):
 o=evald(d,q);o['Pbar']=bar(o['P']);o['Qbar']=bar(o['Q']);o['edge']=list(map(int,e));o['third']=third
 o.update(n=d['n'],h=d['h'],uv=q,J=d['J'],poly=d['poly'])
 return {k:(v.tolist() if isinstance(v,np.ndarray) else v) for k,v in o.items() if k not in ('P','Q','Y')}

if __name__=='__main__':
 import sys
 mode=sys.argv[1] if len(sys.argv)>1 else 'rootedges'
 candidates=[tuple(e) for e in E if 24 in e or 29 in e] if mode=='rootedges' else [tuple(e) for e in E]
 ledger=[];hist={};best=100;t=time.time()
 for e in candidates:
  a,b=X[list(e)];direction=b-a;direction/=np.linalg.norm(direction)
  k=np.argmin(abs(direction));n0=np.cross(direction,np.eye(3)[k]);n0/=np.linalg.norm(n0);n1=np.cross(direction,n0)
  ev=[]
  for j,p in enumerate(X):
   if j in e:continue
   r=p-a;ang=math.atan2(-(r@n0),r@n1)%math.pi;ev.append((ang,j))
  ev.sort();angles=[(ang,j) for ang,j in ev]
  angles+= [((ev[i][0]+(ev[(i+1)%len(ev)][0]+(math.pi if i==len(ev)-1 else 0)))/2,None) for i in range(len(ev))]
  for ang,j in angles:
   n=n0*math.cos(ang)+n1*math.sin(ang);d=domain(n,n@a)
   if d is None:continue
   pol=d['poly'];cen=pol.mean(0)
   for q in [cen*.4,cen,cen*1.5]+[(2*p+cen)/3 for p in pol if np.linalg.norm(p)>1e-8]:
    if np.max(d['AA']@q-d['B'])>1e-9:continue
    o=evald(d,q);key=(o['S'],o['U']);hist[key]=hist.get(key,0)+1
    if sum(key)<best:
     best=sum(key);r=nom(d,q,e,j);ledger.append(r);print('BEST',e,j,key,r['Pbar'],r['Qbar'],flush=True)
    if key in [(1,1),(1,2),(2,1)]:
     ledger.append(nom(d,q,e,j))
  print('EDGE',e,'best',best,'trials',sum(hist.values()),'seconds',round(time.time()-t,1),flush=True)
 out={'mode':mode,'hist':{str(k):v for k,v in hist.items()},'ledger':ledger}
 open('/mnt/data/hinge_'+mode+'_screen.json','w').write(json.dumps(out,sort_keys=True,indent=2)+'\n')
 print('COMPLETE',hist,len(ledger),time.time()-t,flush=True)
```
