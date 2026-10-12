# material-8c37a3a6e845

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Complete exact control for POLAR_GLOBAL_RADIUS_TRANSFER_V1.
python -S radius_transfer_compact.py build
python -S radius_transfer_compact.py check
Python>=3.10 standard library, assertions enabled; no input files or randomness.
This genuine polar pyramid is NOT centered at its volume centroid and has U=3.
"""
from fractions import Fraction as F
from itertools import combinations as C
from pathlib import Path
import hashlib,json,sys
assert __debug__
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def sub(a,b):return [x-y for x,y in zip(a,b)]
def det(a):
 m=[list(map(F,r)) for r in a];v=F(1);n=len(m)
 for k in range(n):
  j=next((j for j in range(k,n) if m[j][k]),None)
  if j is None:return F(0)
  if j!=k:m[j],m[k]=m[k],m[j];v=-v
  p=m[k][k];v*=p
  for j in range(k+1,n):
   t=m[j][k]/p
   for l in range(k+1,n):m[j][l]-=t*m[k][l]
 return v
def solve(a):
 d=det(a)
 if not d:return None
 return tuple(det([[F(1) if j==k else row[j] for j in range(3)] for row in a])/d for k in range(3))
def enc(x):
 if isinstance(x,F):return [x.numerator,x.denominator]
 if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [enc(v) for v in x]
 return x
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
def main():
 assert sys.argv[1:] in (['build'],['check'])
 q=[list(map(F,p)) for p in [(1,0,1),(1,2,1),(-3,4,1),(-11,-2,1),(F(-1,2),F(-1,3),-1)]]
 g=[[dot(a,b) for b in q] for a in q];n=[g[i][i] for i in range(5)]
 assert n==[2,6,26,126,F(49,36)]
 xs=set()
 for ids in C(range(5),3):
  x=solve([q[i] for i in ids])
  if x is not None and all(dot(a,x)<=1 for a in q):xs.add(x)
 assert xs=={(F(0),F(0),F(1)),(F(4),F(0),F(-3)),(F(12,23),F(24,23),F(-37,23)),(F(-36,151),F(48,151),F(-149,151)),(F(4,5),F(-24,5),F(1,5))}
 xs=sorted(xs);stars=[tuple(i for i,a in enumerate(q) if dot(a,x)==1) for x in xs]
 assert set(stars)=={(0,1,2,3),(0,1,4),(1,2,4),(2,3,4),(0,3,4)}
 ori=[det([sub(q[(i+1)%4][:2],q[i][:2]),sub([F(1,2),F(1,3)],q[i][:2])]) for i in range(4)]
 assert ori==[1,F(23,3),F(151,3),5] and all(x>0 for x in ori)
 # Strictly interior base point -qE makes 0 interior to Q, hence P bounded.
 edges=[];dual=set()
 for i,j in C(range(5),2):
  common=tuple(sorted(set(stars[i])&set(stars[j])))
  if len(common)==2:edges.append((i,j));dual.add(common)
 assert len(edges)==8 and dual=={(0,1),(1,2),(2,3),(0,3),(0,4),(1,4),(2,4),(3,4)}
 u=(F(0),F(0),F(1));weights=[35,1,1,3]
 assert all(sum(weights[i]*(q[i][k]-u[k]) for i in range(4))==0 for k in range(3))
 arrows=[(i,j) for i in range(4) for j in range(4) if i!=j and g[i][j]>=n[i]]
 assert arrows==[(0,1),(1,2),(2,3)] and all(g[i][i+1]==n[i] for i in range(3))
 roots=[i for i,x in enumerate(xs) if all(dot(x,sub(xs[b if a==i else a],x))<0 for a,b in edges if i in (a,b))]
 assert roots==[1,3,4] and xs.index(u)==1
 tvals=[(64*n[0]-n[3])/63,(4*n[0]-n[2])/3,(4*n[1]-n[3])/3]
 assert tvals==[F(2,63),F(-6),F(-34)]
 norms=[dot(x,x) for x in xs]
 assert max(norms)==25 and max(tvals)<min(1/x for x in norms)
 minors=[]
 for t in tvals:
  assert all(x>t for x in n)
  for ids in stars:
   record=[]
   for k in range(1,len(ids)+1):
    for ind in C(ids,k):
     value=det([[g[i][j]-t for j in ind] for i in ind])
     assert value>=0;record.append([ind,value])
   assert any(len(ind)==3 and value>0 for ind,value in record)
   assert len(ids)!=4 or record[-1][1]==0
   minors.append([t,ids,record])
 assert sum(len(x[2]) for x in minors)==129
 taus=[]
 for i,j in sorted(dual):
  d=n[i]*n[j]-g[i][j]**2;l=n[i]+n[j]-2*g[i][j]
  assert d>0 and l>0;v=d/l
  assert v>max(tvals)
  assert all(det([[n[i]-t,g[i][j]-t],[g[i][j]-t,n[j]-t]])>0 for t in tvals)
  taus.append([[i,j],v])
 T=min(v for _,v in taus);assert T==F(17,229)
 angular=[]
 for s in [F(1),min(n[:4]),T]:
  eta=[(n[i]-s)/(n[i+1]-s) for i in range(3)]
  assert all(0<=v<1 for v in eta)
  b=1-sum(eta);delta=b*b-4*eta[0]*eta[1]*eta[2]
  angular.append([s,eta,b,delta,b>0 and delta>0])
 assert [a[-1] for a in angular]==[True,True,False]
 assert angular[-1][2:4]==[F(55890667658,232325550033),F(-177970077478710096944,53975161198135986301089)]
 raw=[[n[2]-n[1],n[1]-n[0]],[n[1]-n[0],n[3]-n[2]-n[1]+n[0]]]
 assert raw==[[20,4],[4,96]] and det(raw)==1904
 by=dict(zip(stars,xs));v0,v1,v2,v3=[by[i] for i in [(0,1,4),(1,2,4),(2,3,4),(0,3,4)]]
 tetra=[[u,v0,v1,v2],[u,v0,v2,v3]]
 volumes=[abs(det([sub(x,a[0]) for x in a[1:]]))/6 for a in tetra]
 assert volumes==[F(3840,3473),F(5376,755)]
 volume=sum(volumes);centroid=[sum(v*sum(x[k] for x in a)/4 for v,a in zip(volumes,tetra))/volume for k in range(3)]
 assert volume==F(142848,17365) and dot(q[4],centroid)==F(1,2)
 report={'identity':'POLAR_GLOBAL_RADIUS_TRANSFER_V1','status':'EXACT_RELAXATION_SEPARATION_NOT_GOMBOC_NOT_OWN_CENTROID','poles':q,'gram':g,'vertices':xs,'stars':stars,'edges':edges,'oriented_base_tests':ori,'root_tangent_weights':weights,'root_local_zero_arrows':arrows,'strict_unstable_indices':roots,'squared_norms':norms,'linear_thresholds':tvals,'all_star_principal_minors':minors,'edge_taus':taus,'angular_tests':angular,'raw_gap_matrix':raw,'tetrahedra':tetra,'tetrahedron_volumes':volumes,'volume':volume,'actual_centroid':centroid}
 b=(json.dumps(enc(report),sort_keys=True,separators=(',',':'))+'\n').encode()
 path=Path('radius_transfer_compact_report.json')
 if sys.argv[1]=='build':path.write_bytes(b)
 else:assert path.read_bytes()==b
 print('POLAR_GLOBAL_RADIUS_TRANSFER_EXACT_PASS 5 8 5 3 129')
 print('NONLINEAR_EDGE_ANGULAR_SEPARATES_ALL_LINEAR_STAR_CUTS_NOT_GOMBOC')
 print('SOURCE',*pin(Path(__file__).read_bytes()));print('OUTPUT',*pin(b))
if __name__=='__main__':main()
