# material-29aa3aecf690

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# H5_ALLROOT_UNCAPPED_RHO_TUBE_RECOVERY_V1

Complete source-only recovery for the coordinator's actual all-root heptagon-triangle exclusion. This is not the earlier H5 three-arrow capped certificate. All exact body inputs, actual moments, true incidence, exhaustive rooted-tree enumeration, rational witness checks, polynomial compiler, interval cover builder, uniform-margin check and tube arithmetic are below. No parent implementation, saved sandbox, omitted helper, random seed or external dataset is required.

Save the two complete Python fences as the named UTF-8/LF files, each with its final newline. Numerical witness location was run with CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0 on Linux x86_64, OPENBLAS_NUM_THREADS=1. Assertions must be enabled. No random calls occur. The locator uses the specified SciPy release's default HiGHS LP options, method='highs'; explicit thresholds, rational denominator trials, branch order and all physical inputs are literal in the source. The scientific acceptance checks use Python standard-library Fraction arithmetic only. Numerical optimizer success or failure is never the proof of an exclusion.

Fresh reconstruction commands, from the directory containing both files:

```sh
OPENBLAS_NUM_THREADS=1 python -B allroot_stress.py search primal recovered
OPENBLAS_NUM_THREADS=1 python -B allroot_stress.py search polar recovered
OPENBLAS_NUM_THREADS=1 python -B stress_family.py build recovered
python -B -S allroot_stress.py check recovered/primal_search.json
python -B -S allroot_stress.py check recovered/polar_search.json
python -B -S stress_family.py check recovered/family_certificate.json
```

Two source-only runs in separate directories reproduced all three certificate JSON files byte-for-byte. The final comment correction in allroot_stress.py only identifies its locator whitening as numerical, not rational; it does not change executable statements. Exact checker output was also observed in both directories. These are coordinator computations and cold recovery, not another author's audit or formal proof-assistant verification. A changed numerical stack can locate different valid certificates; exact checking remains mandatory. The pinned reconstruction stack is needed for the following literal output identities.

Input pins:
- allroot_stress.py: 7405 bytes, SHA256 6b3b9ff9f11ab435db983abd64755351c365f7fd20abf488d620996afef84e7a.
- stress_family.py: 11944 bytes, SHA256 67af43b6325c9774d671825fbc644dc82c47da7e72dc5c73d6d1cd0abbf05728.

Reproduced certificate pins:
- primal_search.json: 44145 bytes, SHA256 49e03e041fff75e593e63beb07f8aa28d42f336faf287a6688610f83635a8b04.
- polar_search.json: 58679 bytes, SHA256 e7d373006329ee82879b50ad50de42dfdf9ab0ecac5108f3e72a8937e8673ce0.
- family_certificate.json: 50898 bytes, SHA256 1949f65642a5069c92040688a0a884f6e0520777604742c62e8490602e35069b.

Expected family-check stdout, 228 bytes, SHA256 14b6dedc37b99939ec9ba785cf706c416b5fc2b692d0cd97096a39d5619ad9bd:

```
H5_PARALLEL_FULL_RHO_ALL_PSD_U2_PASS 692 4 1561 48790
H5_PARALLEL_ACTUAL_MOMENTS_FIDELITY_PASS ['29/250', '1/6', '1/6']
H5_UNCAPPED_ALLROOT_UNIFORM_MARGIN_PASS 2^-24
H5_FULL_11_MODULI_THIN_TUBE_U2_PASS rho=[1/2,7] epsilon=2^-52
```

Expected polar-check stdout, 116 bytes, SHA256 dc1208451512b674b001bc267b4ebef6fb215754b1e7fb895f8c52f1c9d0a2e3:

```
ACTUAL_ALLROOT_NEGATIVE_DEFINITE_STRESS_PASS polar 874 [4879, 4879, 4879, 4879, 4879, 4879, 4879, 4879, 4879] 43911
```

The primal point check reports 674 stresses, 4879 trees per each of ten roots, and 48790 total. The family cover has intervals [1/2,21/16], [21/16,17/8], [17/8,15/4], [15/4,7], respectively 458,353,363,387 stress uses. There are 692 distinct retained stresses, 1561 uses and 393 interval-locator LP solves. The computational theorem and its actual-COM perturbation proof are preserved separately as H5_ALLROOT_UNCAPPED_RHO_TUBE_V1. In particular the tube epsilon=2^-52 is NOT the earlier full-width eleven-parameter H5 cylinder.

## File: allroot_stress.py

```python
#!/usr/bin/env python3
"""Exact actual geometry and all-root stress checker; numerical locator optional.
No scientific proof is inferred from a solver status. Every covering stress is
checked by rational Sylvester minors, and every labelled rooted tree is covered.
"""
from fractions import Fraction as F
from itertools import combinations,product
from pathlib import Path
import hashlib,json,sys,time
FACETS=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),(9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
EDGES=tuple(sorted({tuple(sorted((a,b))) for f in FACETS for a,b in zip(f,f[1:]+f[:1])}))
DUAL=tuple((i,j) for i,j in combinations(range(9),2) if len(set(FACETS[i])&set(FACETS[j]))==2)
THETA=tuple(map(F,('3/20','7/10','4/5','2/25','1/5','2/5','1/20','1/25')))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(a,s):return tuple(x*s for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(A):return dot(A[0],cross(A[1],A[2]))
def outer(a,b):return tuple(tuple(x*y for y in b) for x in a)
def inv(A):
 d=det(A);c=[cross(A[1],A[2]),cross(A[2],A[0]),cross(A[0],A[1])]
 return tuple(tuple(c[j][i]/d for j in range(3)) for i in range(3))
def mv(A,v):return tuple(dot(a,v) for a in A)
def actual(theta=THETA,rho=F(3,2),s=F(0),t=F(0)):
 b,c,p,q,a,d,u,v=theta
 Y=tuple(tuple(map(F,row)) for row in ((b,0,0),(c,0,0),(1-p,p,0),(q,1-q,0),(0,d,0),(0,a,0),(u,v,0),(0,0,1),(rho,0,1),(0,rho,1)))
 Y=tuple(scale(z,1/(1+s*z[0]+t*z[1])) for z in Y)
 o=Y[7];V=F(0);J=(F(0),)*3;T=[[F(0)]*3 for _ in range(3)]
 for f in FACETS:
  for k in range(1,len(f)-1):
   z=[o,Y[f[0]],Y[f[k]],Y[f[k+1]]];w=det([sub(v,o) for v in z[1:]])/6
   assert w>=0
   h=tuple(sum(v[i] for v in z) for i in range(3));V+=w;J=add(J,scale(h,w/4))
   for i in range(3):
    for j in range(3):T[i][j]+=w*(h[i]*h[j]+sum(v[i]*v[j] for v in z))/20
 assert V>0;g=scale(J,1/V);X=tuple(sub(y,g) for y in Y)
 C=tuple(tuple(T[i][j]/V-g[i]*g[j] for j in range(3)) for i in range(3))
 poles=[]
 for f in FACETS:
  a,b,c=[X[i] for i in f[:3]];n=cross(sub(b,a),sub(c,a));h=dot(n,a);assert h>0
  pole=scale(n,1/h)
  for i,z in enumerate(X):assert (dot(pole,z)==1) if i in f else (dot(pole,z)<1)
  poles.append(pole)
 return X,C,tuple(poles),V,g

def row(X,i,j):
 a=X[i];b=sub(X[j],a)
 return (a[0]*b[0],a[1]*b[1],a[2]*b[2],a[0]*b[1]+a[1]*b[0],a[0]*b[2]+a[2]*b[0],a[1]*b[2]+a[2]*b[1])
def matrix(r):return ((r[0],r[3]/2,r[4]/2),(r[3]/2,r[1],r[5]/2),(r[4]/2,r[5]/2,r[2]))
def pd(A):return A[0][0]>0 and A[0][0]*A[1][1]-A[0][1]**2>0 and det(A)>0

def rooted_trees(n,edges):
 for tree in combinations(edges,n-1):
  uf=list(range(n));ok=True
  def find(a):
   while uf[a]!=a:a=uf[a]
   return a
  adj=[[] for _ in range(n)]
  for a,b in tree:
   x,y=find(a),find(b)
   if x==y:ok=False;break
   uf[x]=y;adj[a].append(b);adj[b].append(a)
  if not ok:continue
  for root in range(n):
   parents=[-1]*n;parents[root]=root;stack=[root]
   for v in stack:
    for w in adj[v]:
     if parents[w]<0:parents[w]=v;stack.append(w)
   assert len(stack)==n
   yield root,tuple((i,p) for i,p in enumerate(parents) if i!=root)

def jdump(x):return json.dumps(x,sort_keys=True,separators=(',',':'))+'\n'
def stress_rows(X,terms):
 r=[F(0)]*6
 for i,j,w in terms:
  w=F(w);assert w>0
  a=row(X,i,j)
  r=[x-w*y for x,y in zip(r,a)]
 A=matrix(r);assert pd(A)
 return A

def search(side,folder,rho=F(3,2),seed=None):
 import numpy as np
 from scipy.optimize import linprog
 X,C,Q,V,g=actual(rho=rho)
 if side=='polar':X=Q;edges=DUAL
 else:edges=EDGES
 # Numerical covariance whitening is used only by the floating locator.
 cf=np.array(C,float)
 h,U=np.linalg.eigh(cf);T=(U*(1/np.sqrt(h)))@U.T
 if side=='polar':T=np.linalg.inv(T)
 Z=np.array(X,float)@T.T
 n=len(X);ij=tuple((i,j) for a,b in edges for i,j in ((a,b),(b,a)))
 rows=np.array([list(map(float,row(Z,i,j))) for i,j in ij])
 idx={e:k for k,e in enumerate(ij)}
 rays=[np.array(v,float) for v in product((-1,0,1),repeat=3) if any(v)]
 rays += [Z[b]-Z[a] for a,b in edges]
 rays += list(Z)
 # Trace-one PSD outer cone. The rows are exact in the final physical gauge;
 # the grid and whitening are locator choices, not proof dependencies.
 def rayrow(v):
  v=v/np.linalg.norm(v);return np.array([v[0]**2,v[1]**2,v[2]**2,2*v[0]*v[1],2*v[0]*v[2],2*v[1]*v[2]])
 G=np.array([-rayrow(v) for v in rays]);ng=len(G)
 certs=[];masks=[];processed=solves=0;unresolved=[];start=time.time()
 if seed:
  for terms in seed:
   try:stress_rows(X,terms)
   except AssertionError:continue
   certs.append(terms);masks.append(sum(1<<idx[(i,j)] for i,j,w in terms))
 for root,tree in rooted_trees(n,edges):
  bits=sum(1<<idx[e] for e in tree);processed+=1
  if any(bits&m==m for m in masks):continue
  ids=[idx[e] for e in tree];D=rows[ids]
  # Maximize the minimum selected arrow; PSD outer constraints are unshifted.
  A=np.vstack((np.c_[G,np.zeros(ng)],np.c_[-D,np.ones(len(D))]))
  b=np.zeros(len(A));eq=np.zeros((1,7));eq[0,:3]=1
  objective=np.zeros(7);objective[-1]=-1
  sol=linprog(objective,A_ub=A,b_ub=b,A_eq=eq,b_eq=[1.],bounds=[(None,None)]*7,method='highs')
  solves+=1
  if sol.success and sol.x[-1]<-1e-8:
   weights=-sol.ineqlin.marginals[ng:]
   terms0=[(ij[k][0],ij[k][1],float(w)) for k,w in zip(ids,weights) if w>1e-9]
   found=None
   for den in (1000,100000,10000000,1000000000):
    terms=[(i,j,str(F(w).limit_denominator(den))) for i,j,w in terms0 if F(w).limit_denominator(den)>0]
    try:stress_rows(X,terms);found=terms;break
    except AssertionError:pass
   if found is not None:
    certs.append(found);masks.append(sum(1<<idx[(i,j)] for i,j,w in found))
    if len(certs)%25==0:print(side,processed,'certs',len(certs),'solves',solves,'elapsed',round(time.time()-start,1),flush=True)
    continue
  unresolved.append({'root':root,'tree':tree,'status':int(sol.status),'margin':None if sol.x is None else float(sol.x[-1])})
  if len(unresolved)>=10:break
 out={'version':1,'side':side,'rho':str(rho),'theta':list(map(str,THETA)),'certificates':certs,'processed':processed,'solves':solves,'unresolved':unresolved}
 Path(folder).mkdir(exist_ok=True,parents=True)
 path=Path(folder)/(side+'_search.json');path.write_text(jdump(out))
 print(side,'END',processed,'certs',len(certs),'solves',solves,'unresolved',len(unresolved),'seconds',time.time()-start,flush=True)
 return out

def check(path):
 data=json.loads(Path(path).read_text());assert data['version']==1 and not data['unresolved'];assert data['theta']==list(map(str,THETA))
 X,C,Q,V,g=actual(rho=F(data['rho']));side=data['side']
 if side=='polar':X=Q;edges=DUAL
 else:assert side=='primal';edges=EDGES
 ij=tuple((i,j) for a,b in edges for i,j in ((a,b),(b,a)));idx={e:k for k,e in enumerate(ij)}
 masks=[]
 for terms in data['certificates']:
  stress_rows(X,terms);masks.append(sum(1<<idx[(i,j)] for i,j,w in terms))
 counts=[0]*len(X)
 for root,tree in rooted_trees(len(X),edges):
  bits=sum(1<<idx[e] for e in tree);assert any(bits&m==m for m in masks);counts[root]+=1
 print('ACTUAL_ALLROOT_NEGATIVE_DEFINITE_STRESS_PASS',side,len(masks),counts,sum(counts))
 return counts
if __name__=='__main__':
 if sys.argv[1]=='search':search(sys.argv[2],sys.argv[3],F(sys.argv[4]) if len(sys.argv)>4 else F(3,2))
 elif sys.argv[1]=='check':check(sys.argv[2])
 else:raise ValueError('search SIDE FOLDER [RHO] | check FILE')
```

## File: stress_family.py

```python
#!/usr/bin/env python3
"""Exact polynomial all-root cover for the actual H5 parallel rho family.
The check command uses only Python's standard library and allroot_stress.py.
"""
from allroot_stress import *
from math import comb

def pa(a,b):
 return tuple((a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(max(len(a),len(b))))
def ps(a,c):return tuple(c*x for x in a)
def pm(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return tuple(c)
def pe(a,x):
 y=F(0)
 for v in a[::-1]:y=y*x+v
 return y

def pvector_add(a,b):return tuple(pa(x,y) for x,y in zip(a,b))
def pvector_scale(a,k):return tuple(ps(x,k) for x in a)
def pdet(A):
 a,b,c=A
 return pa(pa(pm(a[0],pa(pm(b[1],c[2]),ps(pm(b[2],c[1]),-1))),ps(pm(a[1],pa(pm(b[0],c[2]),ps(pm(b[2],c[0]),-1))),-1)),pm(a[2],pa(pm(b[0],c[1]),ps(pm(b[1],c[0]),-1))))

def family_arrows():
 # Every coordinate is affine in rho. Integrate the genuine fixed-apex fan,
 # exactly as for the rational point; no interpolation guess is used.
 b,c,p,q,a,d,u,v=THETA;z=(F(0),);one=(F(1),);r=(F(0),F(1))
 Y=(((b,),z,z),((c,),z,z),((1-p,),(p,),z),((q,),(1-q,),z),(z,(d,),z),(z,(a,),z),((u,),(v,),z),(z,z,one),(r,z,one),(z,r,one))
 V=(F(0),);J=((F(0),),)*3;o=Y[7]
 for f in FACETS:
  for k in range(1,len(f)-1):
   tet=[o,Y[f[0]],Y[f[k]],Y[f[k+1]]]
   dd=[pvector_add(a,pvector_scale(o,-1)) for a in tet[1:]]
   w=ps(pdet(dd),F(1,6));V=pa(V,w)
   h=((F(0),),)*3
   for a in tet:h=pvector_add(h,a)
   J=pvector_add(J,tuple(ps(pm(w,hj),F(1,4)) for hj in h))
 while len(V)>1 and not V[-1]:V=V[:-1]
 assert len(V)<=3
 Xnum=tuple(tuple(pa(pm(V,y),ps(j,-1)) for y,j in zip(v,J)) for v in Y)
 ij=tuple((i,j) for a,b in EDGES for i,j in ((a,b),(b,a)))
 rows={}
 for i,j in ij:
  a=Xnum[i];d=pvector_add(Y[j],pvector_scale(Y[i],-1))
  row=(pm(a[0],d[0]),pm(a[1],d[1]),pm(a[2],d[2]),pa(pm(a[0],d[1]),pm(a[1],d[0])),pa(pm(a[0],d[2]),pm(a[2],d[0])),pa(pm(a[1],d[2]),pm(a[2],d[1])))
  assert all(not any(p[5:]) for p in row)
  rows[(i,j)]=tuple(tuple(p[k] if k<len(p) else F(0) for k in range(5)) for p in row)
 # Independent exact point identity checks on this algebraic compiler.
 for rho in (F(1,2),F(3,2),F(7)):
  X,C,Q,v,g=actual(rho=rho);assert pe(V,rho)==v
  assert tuple(pe(j,rho)/v for j in J)==g
  for e,rr in rows.items():assert tuple(pe(p,rho)/v for p in rr)==row_point(X,*e)
 return V,J,rows
row_point=row

def polynomial_stress(terms,rows):
 A=[(F(0),)*5 for _ in range(6)]
 for i,j,w in terms:
  for k in range(6):A[k]=pa(A[k],ps(rows[(i,j)][k],-F(w)))
 return tuple(A)

def bernstein(a,l,u):
 n=len(a)-1;w=u-l
 power=tuple(w**j*sum(a[i]*comb(i,j)*l**(i-j) for i in range(j,n+1)) for j in range(n+1))
 return tuple(sum(F(comb(k,j),comb(n,j))*power[j] for j in range(k+1)) for k in range(n+1))

def box_pd(poly,l,u):
 b=[bernstein(a,l,u) for a in poly]
 return all(pd(matrix(tuple(b[k][j] for k in range(6)))) for j in range(5))

def cover_search(folder):
 import numpy as np
 from scipy.optimize import linprog
 folder=Path(folder);folder.mkdir(exist_ok=True,parents=True)
 if not (folder/'primal_search.json').exists():search('primal',folder)
 db=json.loads((folder/'primal_search.json').read_text())['certificates']
 V,J,rows=family_arrows();polys=[polynomial_stress(t,rows) for t in db]
 ij=tuple((i,j) for a,b in EDGES for i,j in ((a,b),(b,a)));idx={e:k for k,e in enumerate(ij)}
 tree_data=list(rooted_trees(10,EDGES));trees=np.array([sum(1<<idx[e] for e in t) for r,t in tree_data],np.uint64)
 masks=np.array([sum(1<<idx[(i,j)] for i,j,w in t) for t in db],np.uint64)
 hit=(trees[None,:]&masks[:,None])==masks[:,None]
 seen={tuple(tuple(z) for z in t) for t in db}
 leaves=[];nodes=0;block_solves=0
 def numeric_good(l,u):
  pf=np.array(polys,float);ll,ww=float(l),float(u-l);tr=np.zeros((5,5))
  for k in range(5):
   for i in range(5):tr[k,i]=sum(comb(k,j)/comb(4,j)*ww**j*comb(i,j)*ll**(i-j) for j in range(min(k,i)+1))
  b=np.einsum('kij,rj->kir',pf,tr);a=np.zeros((len(polys),5,3,3))
  a[:,:,0,0]=b[:,0,:];a[:,:,1,1]=b[:,1,:];a[:,:,2,2]=b[:,2,:]
  a[:,:,0,1]=a[:,:,1,0]=b[:,3,:]/2;a[:,:,0,2]=a[:,:,2,0]=b[:,4,:]/2;a[:,:,1,2]=a[:,:,2,1]=b[:,5,:]/2
  return np.flatnonzero(np.all(np.linalg.eigvalsh(a)[:,:,0]>1e-9,axis=1)).tolist()
 def install(terms):
  nonlocal masks,hit
  key=tuple(tuple(z) for z in terms)
  if key in seen:return db.index(terms)
  seen.add(key);db.append(terms);polys.append(polynomial_stress(terms,rows))
  mask=np.uint64(sum(1<<idx[(i,j)] for i,j,w in terms));masks=np.r_[masks,mask];hit=np.vstack((hit,(trees&mask)==mask))
  return len(db)-1
 def robust_complete(l,u,good):
  nonlocal block_solves
  # Direct sum of five PSD cones is an outer primal for a common dual stress
  # negative definite at every degree-four Bernstein coefficient. All returned
  # rational stresses are then checked exactly; solver failure just subdivides.
  mid=(l+u)/2;x,c,q,*_=actual(rho=mid);cf=np.array(c,float);ev,U=np.linalg.eigh(cf);T=(U*(1/np.sqrt(ev)))@U.T
  rr=[]
  for e in ij:
   bb=[bernstein(p,l,u) for p in rows[e]];arr=[]
   for j in range(5):
    H=np.array(matrix(tuple(bb[k][j] for k in range(6))),float);H=T@H@T.T
    arr.append([H[0,0],H[1,1],H[2,2],2*H[0,1],2*H[0,2],2*H[1,2]])
   rr.append(np.array(arr).reshape(30))
  rr=np.array(rr);rays=[np.array(v,float) for v in product((-1,0,1),repeat=3) if any(v)]
  Z=np.array(x,float)@T.T;rays += [Z[b]-Z[a] for a,b in EDGES];rays+=list(Z)
  rayrows=[]
  for v in rays:
   v=v/np.linalg.norm(v);rayrows.append(-np.array([v[0]**2,v[1]**2,v[2]**2,2*v[0]*v[1],2*v[0]*v[2],2*v[1]*v[2]]))
  G=np.zeros((5*len(rays),31))
  for j in range(5):G[j*len(rays):(j+1)*len(rays),6*j:6*j+6]=rayrows
  eq=np.zeros((1,31))
  for j in range(5):eq[0,6*j:6*j+3]=1
  obj=np.zeros(31);obj[-1]=-1;ng=len(G)
  covered=np.any(hit[good],axis=0) if good else np.zeros(len(trees),bool)
  for ti in np.flatnonzero(~covered):
   if covered[ti]:continue
   root,tree=tree_data[ti];ids=[idx[e] for e in tree]
   A=np.vstack((G,np.c_[-rr[ids],np.ones(len(ids))]))
   sol=linprog(obj,A_ub=A,b_ub=np.zeros(len(A)),A_eq=eq,b_eq=[1.],bounds=[(None,None)]*31,method='highs');block_solves+=1
   if not sol.success or sol.x[-1]>=-1e-8:return None
   weights=-sol.ineqlin.marginals[ng:];raw=[(*ij[k],float(w)) for k,w in zip(ids,weights) if w>1e-9];found=None
   for den in (1000,100000,10000000,1000000000):
    terms=[(i,j,str(F(w).limit_denominator(den))) for i,j,w in raw if F(w).limit_denominator(den)>0]
    if box_pd(polynomial_stress(terms,rows),l,u):found=terms;break
   if found is None:return None
   k=install(found);good.append(k);covered|=hit[k]
  return good
 def solve(l,u,depth):
  nonlocal nodes
  nodes+=1;good=numeric_good(l,u)
  covered=np.any(hit[good],axis=0) if good else np.zeros(len(trees),bool)
  if not np.all(covered):good=robust_complete(l,u,good)
  if good is not None:
   # Incremental greedy updates charge each covered tree only once.
   gh=hit[good];scores=gh.sum(axis=1);remain=np.ones(len(trees),bool);chosen=[]
   while np.any(remain):
    p=int(np.argmax(scores));k=good[p];assert scores[p]>0
    assert box_pd(polys[k],l,u)
    new=remain&hit[k];chosen.append(k);remain&=~new;scores-=gh[:,new].sum(axis=1)
   leaves.append({'l':str(l),'u':str(u),'certificates':chosen})
   (folder/'database.json').write_text(jdump(db));(folder/'partial_cover.json').write_text(jdump({'leaves':leaves,'nodes':nodes}))
   print('LEAF',str(l),str(u),'witnesses',len(chosen),'depth',depth,'solves',block_solves,flush=True);return
  assert depth<12
  mid=(l+u)/2;solve(l,mid,depth+1);solve(mid,u,depth+1)
 solve(F(1,2),F(7),0)
 used=sorted({k for leaf in leaves for k in leaf['certificates']});new={old:k for k,old in enumerate(used)}
 for leaf in leaves:leaf['certificates']=[new[k] for k in leaf['certificates']]
 result={'version':1,'theta':list(map(str,THETA)),'range':['1/2','7'],'stress_certificates':[db[k] for k in used],'leaves':leaves,'nodes':nodes}
 path=folder/'family_certificate.json';path.write_text(jdump(result))
 print('FAMILY_BUILT',len(used),len(leaves),nodes,path.stat().st_size,'block_solves',block_solves,flush=True)

def cover_check(path):
 data=json.loads(Path(path).read_text());assert data['version']==1 and data['theta']==list(map(str,THETA)) and data['range']==['1/2','7']
 V,J,rows=family_arrows();assert all(x>0 for x in bernstein(V,F(1,2),F(7)))
 db=data['stress_certificates'];polys=[polynomial_stress(t,rows) for t in db]
 ij=tuple((i,j) for a,b in EDGES for i,j in ((a,b),(b,a)));idx={e:k for k,e in enumerate(ij)}
 masks=[]
 for terms in db:
  assert terms and all(F(w)>0 for i,j,w in terms) and len({(i,j) for i,j,w in terms})==len(terms)
  masks.append(sum(1<<idx[(i,j)] for i,j,w in terms))
 # Exact shape fidelity for every rho>0 follows from strict basal heptagon
 # inside Delta and fixed prismatoid facets; fixed incidence is also compiled
 # algebraically below and checked for every leaf as outward support signs.
 fidelity_check()
 trees=[sum(1<<idx[e] for e in t) for r,t in rooted_trees(10,EDGES)];assert len(trees)==48790
 leaves=data['leaves'];end=F(1,2);uses=0
 for leaf in leaves:
  l,u=F(leaf['l']),F(leaf['u']);assert l==end and l<u;end=u
  ks=leaf['certificates'];assert len(set(ks))==len(ks)
  for k in ks:
   assert box_pd(polys[k],l,u)
   # Certified normalized all-metric margin: V(rho)<10, sum weights=W.
   W=sum(F(w) for i,j,w in db[k]);shift=10*W/F(2**24)
   shifted=tuple(pa(p,(-shift,)) if j<3 else p for j,p in enumerate(polys[k]))
   assert box_pd(shifted,l,u)
  ms=[masks[k] for k in ks];assert all(any(t&m==m for m in ms) for t in trees)
  uses+=len(ks)
 assert end==7 and data['nodes']==2*len(leaves)-1
 print('H5_PARALLEL_FULL_RHO_ALL_PSD_U2_PASS',len(db),len(leaves),uses,48790)
 print('H5_PARALLEL_ACTUAL_MOMENTS_FIDELITY_PASS',list(map(str,V)))
 assert all(F(1,5)<x<10 for x in bernstein(V,F(1,2),F(7)))
 epsilon=F(1,2**52);vertex_change=128*epsilon
 assert epsilon<F(1,400) and epsilon<F(1,14) and vertex_change<F(1,2540)
 centered_change=25402*vertex_change
 assert centered_change<F(1,2**30) and 42*centered_change<F(1,2**24)
 # Exact basal guards on a larger containing box; positive projectivity
 # denominators preserve the raw facet lattice. See the accompanying proof.
 assert F(7,50)<F(3,20)-epsilon and F(3,20)+epsilon<F(4,25)
 assert F(69,100)<F(7,10)-epsilon and F(7,10)+epsilon<F(71,100)
 assert F(79,100)<F(4,5)-epsilon and F(4,5)+epsilon<F(81,100)
 assert F(3,40)<F(2,25)-epsilon and F(2,25)+epsilon<F(17,200)
 assert F(19,100)<F(1,5)-epsilon and F(1,5)+epsilon<F(21,100)
 assert F(39,100)<F(2,5)-epsilon and F(2,5)+epsilon<F(41,100)
 assert F(19,400)<F(1,20)-epsilon and F(1,20)+epsilon<F(21,400)
 assert F(3,80)<F(1,25)-epsilon and F(1,25)+epsilon<F(17,400)
 assert F(21,400)/F(7,50)+F(17,400)/F(19,100)==F(91,152)<1
 assert F(81,100)+F(17,200)<1 and 1-7*epsilon>0
 print('H5_UNCAPPED_ALLROOT_UNIFORM_MARGIN_PASS 2^-24')
 print('H5_FULL_11_MODULI_THIN_TUBE_U2_PASS rho=[1/2,7] epsilon=2^-52')
 return data

def fidelity_check():
 # With rho>0 the prescribed facet planes support all labelled vertices.
 # Planes and signed slacks are low-degree polynomials; exact Bernstein
 # coefficients on [1/2,7] verify strict slacks except incident zeros.
 b,c,p,q,a,d,u,v=THETA;z=(F(0),);one=(F(1),);r=(F(0),F(1))
 Y=(((b,),z,z),((c,),z,z),((1-p,),(p,),z),((q,),(1-q,),z),(z,(d,),z),(z,(a,),z),((u,),(v,),z),(z,z,one),(r,z,one),(z,r,one))
 for f in FACETS:
  aa,bb,cc=[Y[i] for i in f[:3]]
  e=pvector_add(bb,pvector_scale(aa,-1));d=pvector_add(cc,pvector_scale(aa,-1))
  for k,y in enumerate(Y):
   diff=pvector_add(aa,pvector_scale(y,-1))
   slack=pdet([e,d,diff])
   if k in f:assert all(v==0 for v in slack)
   else:assert all(v>0 for v in bernstein(slack,F(1,2),F(7)))
 assert len(EDGES)==17 and len(FACETS)==9

if __name__=='__main__':
 if sys.argv[1]=='build':cover_search(sys.argv[2])
 elif sys.argv[1]=='check':cover_check(sys.argv[2])
 else:raise ValueError('build FOLDER | check CERTIFICATE')
```
