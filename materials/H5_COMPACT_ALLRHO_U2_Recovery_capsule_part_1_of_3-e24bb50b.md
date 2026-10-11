# material-e24bb50bf803

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

# H5_COMPACT_ALLRHO_11PARAMETER_U2_V1 — Recovery capsule part 1/3

All THREE ordered recovery parts are required. Part 1 contains the complete allroot_stress.py and common manifest. Part 2 contains the complete taylor_tube.py. Part 3 contains the complete tube_cover.py. Save each Python fence with its displayed filename, UTF-8/LF, final newline. No previous sandbox, certificate, source, coordinate table, seed or external dataset is required. The companion theorem supplies the geometric proof and precise domain.

Physical rho>0 is compactified to ell=rho/(1+rho). The compact body has bottom vertices ((1-ell) B_i,0) and top (0,0,1),(ell,0,1),(0,ell,1). Independent normalized projectivities s_hat,t_hat are in [-1/200,1/200], and the body is uniformly refilled. This corresponds in the original physical chart to |s_raw|,|t_raw|<=1/(200(1+rho)); it is NOT the entire old raw-projectivity cylinder. All eight basal intervals are literal in part 2. The endpoints ell=0,1 are labelled compactification limits, not genuine V10/E17/F9 bodies. The variable called rho in part 2 is explicitly ell; this part retains physical rho for its separate point-seed locator.

Pinned locator environment: CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, Linux x86_64, OPENBLAS_NUM_THREADS=1. No randomness. linprog uses method='highs' and that release's defaults; all denominator rules, thresholds, orders and limits are explicit. Numerical output is only a locator. Final proof acceptance uses standard-library Fraction arithmetic, not optimizer status.

Reconstruct and verify from a fresh directory containing all three sources:

```sh
OPENBLAS_NUM_THREADS=1 python -B tube_cover.py build recovered 1
python -B -S tube_cover.py check recovered/tube_certificate.json
```

The build automatically generates primal_search.json; no input checkpoint is needed. The checker imports no NumPy/SciPy and uses assertions, which must be enabled. It reconstructs actual volume and first moments after every projective refill, rational Taylor enclosures, all 171120 matrix guards and all 48790 rooted primal trees on each of 49 closed ell cells. There are 1236 distinct rational stresses, 14260 uses and 97 binary nodes; the locator used 1447 calls beyond its separately generated point seed. All used stress supports have at most eight arrows. The final checker also proves V>1/10, congruent diagonal-dominance margins>2^-13 and W*||H||_F^2<2^14; with V<2 this gives normalized actual stress margin 2^-28. The separate geometric argument gives the matched-vertex same-lattice actual-refill displacement tube 2^-43. Checking its scalar constants is not by itself the geometric proof.

Source pins:
- allroot_stress.py: 7327 bytes, SHA256 19663c1c7a10a8c586d648768abc7ff17c09a7ef34ca72449feb3483619eafa8.
- taylor_tube.py: 6643 bytes, SHA256 69d4c0318b54a89827cf922b338fbf9c8490f5065f75423e05e6900b5afb8902.
- tube_cover.py: 9179 bytes, SHA256 e4f0071f6333237eb55f11f66548a395d4d17a837e94ab1966ca283a849b28b3.
Reproduced outputs:
- recovered/primal_search.json: 44145 bytes, SHA256 49e03e041fff75e593e63beb07f8aa28d42f336faf287a6688610f83635a8b04.
- recovered/tube_certificate.json: 2108195 bytes, SHA256 8828a49e64b62f3d7a36234726ac7ff449386e2ef6ace35c39c04df37eb37993.

The final strengthened checker passed. A fresh final-source-only build completed and reproduced both JSON files byte-for-byte; an earlier source-only build did so as well. These are coordinator computations, not a proof-assistant formalization or an independent-author audit. The final checker prints 49 CHECK_LEAF lines followed by:

```
H5_COMPACT_ALLRHO_11_PARAMETER_ALLROOT_U2_PASS 1236 49 14260 48790
H5_RATIONAL_TAYLOR_GERSHGORIN_GUARDS_PASS 171120 mult 1
H5_TRUE_VOLUME_POSITIVE_PASS 0.10415104725658439 minimum_guard 0.00013146299656449417
H5_ALLRHO_NORMALIZED_STRESS_MARGIN_PASS 2^-28
H5_ALLRHO_TRUE_LATTICE_DISPLACEMENT_TUBE_PASS 2^-43
```

Decimals are diagnostics only. A changed numerical stack may find different valid certificates; exact checking remains mandatory.

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
