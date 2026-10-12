# material-ac06eb24e9dd

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Balanced escape: exact core, observed tests, and subtraction-free merit

This is a complete standalone mathematical/source unit, not a new polyhedron. It advances the source-only derivation in [internal-source-reference] by an observed exact run and a numerically safer equivalent merit evaluation. Canonical C622 is unchanged. No literature-novelty claim is made.

For distinct nonzero vectors x_i define d=x_j-x_i,c=x_i.d,A=|x_i|^2,D=|d|^2, e=c/sqrt(AD), b=2c/D, a=max(-1,min(e,b)). The minimum is per edge, before maximizing witnesses. Since b=(|x_j|^2-|x_i|^2)/D-1, a>-1 implies strictly increasing squared radius. Hence every directed cycle includes weight -1 and every maximum-radius outgoing row is identically -1. For ANY designated root, the minimum nonroot row maximum equals the worst widest-path-to-root bottleneck: if the local value is greater than -1, choose row-maximizing exits, which are acyclic and end at the only non-exiting root; at -1 the direct edges prove equality. This equality is of the worst bottleneck, not of each individual row maximum and its own path label.

The increasing signed-square map h(z)=z|z| gives the rational key K=max(-1,min(c|c|/(AD),4c|c|/D^2)). All finite min/max comparisons and path/cut tests remain exact. Let k_i=max_j Kij and choose one maximum-radius index r, so k_r=-1. For 0<=rho<=1 both sum max(0,rho-k_i)-(1+rho) and sum max(0,rho-k_i)^2-(1+rho)^2 are nonnegative. They are EXACTLY equal to the respective sums omitting row r. Thus the omitted-row form avoids catastrophic floating subtraction near feasibility, without changing the mathematical objective. The same statement holds for unsquared escape a with positive margin gamma. A linear loss <rho, or squared loss <rho^2, forces every nonroot key strictly positive and consequently exactly one strict U with no other weak U at the reference origin.

For an actual uniformly filled physical body use X=v-g(P), and centered-polar points Q_f=n_f/(h_f-n_f.g(P)) for maximal facets. Do not use the polar body's own mass. Positive nonroot escape on both point systems supplies strict unique U and S with no extra weak vertex/facet equilibria, but does not replace independent maximal-hull, true-edge, filled-mass, all-edge saddle and weak audits. No qualifying polyhedron was produced by these finite-vector tests.

Recovery: save the full code block, including its terminal newline, as BALANCED_ESCAPE_CORE.py. CPython3.13.5 standard library, assertions enabled. Run `python -B -S BALANCED_ESCAPE_CORE.py > CORE_TEST_RECEIPT.txt`. The source is 4378 bytes, SHA256 5c77caa5321a5a1cf610c271921bc476262c0638fc1a22ec862b3bdfb341662c. Observed successful exit0, marker BALANCED_ESCAPE_CORE_EXACT_TESTS_PASS; CORE_REPORT.json is 1187 bytes, SHA256 db3ad903f802f351c2e3077da59603b8d7da814fb8c53c78741ae0f9abe7de14. Tests cover 114 finite 2D/3D sets, 372 exhaustive root choices, 12 additional family root choices, scale/rotation invariance, equal-radius exceptions, and the exact omitted-root identities. They are not low-C polyhedron searches.

```python
#!/usr/bin/env python3
"""Exact balanced escape kernel and finite-vector theorem tests.
Standard library only. No own-mass polyhedron or optimization success is inferred.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib,json,sys
assert __debug__
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def kernel(points):
 P=[tuple(F(z) for z in p) for p in points];n=len(P)
 assert n>=2 and len(set(P))==n and len({len(p) for p in P})==1
 A=[dot(p,p) for p in P];assert min(A)>0
 K=[[None]*n for p in P];E=[[None]*n for p in P];U=[[None]*n for p in P]
 for i,x in enumerate(P):
  for j,y in enumerate(P):
   if i==j:continue
   d=tuple(b-a for a,b in zip(x,y));D=dot(d,d);c=dot(x,d);z=c*abs(c)
   E[i][j]=z/(A[i]*D);U[i][j]=4*z/(D*D);K[i][j]=max(F(-1),min(E[i][j],U[i][j]))
   assert -1<=K[i][j]<=1
   assert (K[i][j]>0)==(c>0)
   if K[i][j]>-1:assert A[j]>A[i]
 return P,A,K,E,U

def rooted(points,r):
 P,A,K,_,_=kernel(points);n=len(P);assert 0<=r<n
 ell=min(max(K[i][j] for j in range(n) if j!=i) for i in range(n) if i!=r)
 d=[F(-1)]*n;d[r]=F(1)
 for _ in range(n-1):
  old=d[:]
  for i in range(n):
   if i!=r:d[i]=max(old[i],max(min(K[i][j],old[j]) for j in range(n) if j!=i))
 assert min(d[i] for i in range(n) if i!=r)==ell
 parent={}
 for i in range(n):
  if i==r:continue
  j=r if ell==-1 else max((j for j in range(n) if j!=i),key=lambda j:(K[i][j],-j))
  assert K[i][j]>=ell
  if ell>-1:assert A[j]>A[i]
  parent[i]=j
 for start in parent:
  i=start;seen=set()
  while i!=r:assert i not in seen;seen.add(i);i=parent[i]
 cut=[i for i in range(n) if i!=r and d[i]<=ell];assert cut
 assert max(K[i][j] for i in cut for j in range(n) if j not in cut)==ell
 return {'root':r,'bottleneck_key':str(ell),'parents':parent,'attaining_cut':cut}

def root_free(points,rho=F(1,10**8)):
 _,A,K,_,_=kernel(points);n=len(A);rho=F(rho);assert 0<=rho<=1
 k=[max(K[i][j] for j in range(n) if j!=i) for i in range(n)]
 root=max(range(n),key=lambda i:A[i]);assert k[root]==-1
 linear=sum(max(F(0),rho-z) for z in k)-(1+rho)
 squared=sum(max(F(0),rho-z)**2 for z in k)-(1+rho)**2
 # Omitting one maximum-radius row is EXACTLY the same functional and
 # avoids subtraction of nearly equal large quantities in floating point.
 assert linear==sum(max(F(0),rho-k[i]) for i in range(n) if i!=root)
 assert squared==sum(max(F(0),rho-k[i])**2 for i in range(n) if i!=root)
 assert linear>=0 and squared>=0
 if linear<rho or squared<rho*rho:
  exceptional=[i for i,z in enumerate(k) if z<=0]
  assert exceptional==[root] and k[root]==-1
 return linear,k

def verify():
 pool=[(-3,0,1),(-2,2,-1),(-1,-2,3),(0,1,-3),(1,0,0),(2,-1,-2)];count=0;sets=0
 for dim in (2,3):
  for n in range(2,7):
   for subset in combinations(pool,n):
    P=[p[:dim] for p in subset]
    for r in range(n):rooted(P,r);count+=1
    root_free(P);sets+=1
 assert count==372 and sets==114
 family=[]
 for m in (2,10,100,1000):
  P=[(F(1),F(1,m)),(F(1),F(-1,m)),(F(-m),F(0))]
  _,_,K,E,U=kernel(P)
  for r in range(3):rooted(P,r)
  angle=max(E[0][1],E[0][2]);chord=max(U[0][1],U[0][2]);balanced=max(K[0][1],K[0][2])
  assert angle==F(-1,m*m+1) and K[0][1]==-1 and balanced==E[0][2]
  assert balanced<angle and balanced<chord
  assert kernel([tuple(F(7,3)*z for z in p) for p in P])[2]==K==kernel([(-p[1],p[0]) for p in P])[2]
  loss,_=root_free(P,0)
  family.append(dict(m=m,angular=str(angle),twice_chord=str(chord),balanced=str(balanced),zero_margin_loss=str(loss)))
 assert root_free([(1,0),(2,0),(3,0)])[0]==0
 # Distinct equal-maximum-radius points require at least two exceptional rows.
 loss,k=root_free([(1,0),(-1,0),(0,F(1,2))],F(1,100));assert loss>=F(101,100)
 src=Path(__file__).read_bytes();report=dict(marker='BALANCED_ESCAPE_CORE_EXACT_TESTS_PASS',exhaustive_root_checks=count,additional_family_root_checks=12,finite_sets=sets,family=family,source_sha256=hashlib.sha256(src).hexdigest(),source_bytes=len(src),scope='Finite vectors only; no own-mass polyhedron construction or convergence claim.')
 data=(json.dumps(report,sort_keys=True,indent=2)+'\n').encode();Path(__file__).with_name('CORE_REPORT.json').write_bytes(data)
 print(data.decode(),end='');print('CORE_REPORT_BYTES',len(data),'CORE_REPORT_SHA256',hashlib.sha256(data).hexdigest())
if __name__=='__main__':verify()
```

Observed diagnostic keys for m=2: separately maximized angular=-1/5, twice-chord=-676/1369, balanced=-169/185; zero-margin root-free loss338/185. For m=1000 separately maximized angular=-1/1000001 while balanced=-1002001002002000001/1002002002002000001, close to -1. Thus separate small negative local defects are not a proof of small global defect; the per-edge balanced quantity exposes the barrier.
