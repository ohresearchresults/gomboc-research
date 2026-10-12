# material-c0d9799c6cfa

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""CANONICAL_C622_ONE_FACET_CENTROID_ACTUATOR_V1.
Exact differential, bounded-release and target-interiority certificate. NOT a new endpoint.
Parents: canonical scoped16 recovery, plus complete exact_ears.py helpers.
"""
from exact_ears import *
from itertools import combinations
PIN='142ddb5d88fdc8b1721dbb62f52d9b71b78ac4c36e8600131235c6c4289698a0'

def loadexact(path):
 data=Path(path).read_bytes();assert sha256(data).hexdigest()==PIN
 r=json.loads(data);X=[tuple(map(F,p)) for p in r['raw_vertices']]
 adj=[set() for x in X]
 for i,j in r['edges']:adj[i].add(j);adj[j].add(i)
 return r,X,adj

def outer(a,b):return [[x*y for y in b] for x in a]
def matadd(a,b):return [[x+y for x,y in zip(c,d)] for c,d in zip(a,b)]
def matscale(a,t):return [[t*x for x in r] for r in a]

def exact_audit(path,rawpath,out):
 r,X,adj=loadexact(path);g=tuple(map(F,r['raw_centroid']));V=F(r['ordinary_volume'])
 movable=[i for i,face in enumerate(r['faces']) if all(len(adj[v])==3 for v in face)]
 assert movable==[48,55,69,70,89,93,99,100,101,105,110,112,113,114,115,117,120,123,124,125]
 rows=[]
 for f in movable:
  cy=r['faces'][f];N=cross(sub(X[cy[1]],X[cy[0]]),sub(X[cy[2]],X[cy[0]]));h=dot(N,X[cy[0]])
  if h<0:N=tuple(-x for x in N);h=-h
  assert h>0;q=tuple(x/h for x in N)
  assert all(dot(q,X[i])==1 for i in cy)
  assert all(dot(q,x)<1 for i,x in enumerate(X) if i not in cy)
  w=F(0);c=(F(0),)*3;T=[[F(0)]*3 for _ in range(3)]
  for j in range(1,len(cy)-1):
   tri=[X[k] for k in [cy[0],cy[j],cy[j+1]]];weight=det(*tri)/2
   assert weight>0
   s=tuple(sum(p[k] for p in tri) for k in range(3));w+=weight
   c=tuple(c[k]+weight*s[k]/3 for k in range(3))
   K=outer(s,s)
   for p in tri:K=matadd(K,outer(p,p))
   T=matadd(T,matscale(K,weight/12))
  c=tuple(x/w for x in c);T=matscale(T,1/w)
  assert all(dot(T[i],q)==c[i] for i in range(3))
  # All leading principal minors certify the true facet SECOND moment positive.
  pm=[T[0][0],T[0][0]*T[1][1]-T[0][1]**2,det(*T)];assert min(pm)>0
  A=matadd(T,matscale(outer(g,c),-1));gap=1-dot(q,g);assert gap>0
  assert det(*A)==gap*pm[2]
  rows.append(dict(facet=f,vertices=cy,area_over_normal=str(w),surface_centroid=list(map(str,c)),second_moment_sha256=sha256(B(T)).hexdigest(),jacobian_determinant_sha256=sha256(B(-w**3*det(*A)/V**3)).hexdigest(),centroid_interior_gap_sha256=sha256(B(gap)).hexdigest(),positive_gram_minors=3,determinant_identity=True))
 # Four nontriangular true parent planes remain after every simple deletion.
 raw=Path(rawpath).read_bytes()
 assert sha256(raw).hexdigest()=='ac01d1625274b64f336a715e1f5462f40686f647f0b7d1a4d90a5ee21765adb5'
 H=json.loads(raw)['H'];Q=[tuple(F(x,h[-1]) for x in h[:3]) for h in H]
 fixed=[6,77,107,130];base=Q[fixed[-1]];cols=[sub(Q[k],base) for k in fixed[:-1]];rhs=tuple(-x for x in base)
 dd=det(*cols);assert dd!=0
 alpha=[]
 for k in range(3):
  cc=list(cols);cc[k]=rhs;alpha.append(det(*cc)/dd)
 alpha.append(1-sum(alpha));assert min(alpha)>0
 assert all(sum(alpha[j]*Q[fixed[j]][k] for j in range(4))==0 for k in range(3))
 assert all(len(r['faces'][f])>=4 and f not in movable for f in fixed)
 assert all(dot(Q[f],g)<1 for f in fixed)
 for f in fixed:
  assert all(dot(Q[f],X[i])==1 for i in r['faces'][f])
  assert all(dot(Q[f],x)<1 for i,x in enumerate(X) if i not in r['faces'][f])
 simple=[i for i in range(len(X)) if len(adj[i])==3];ear_rows=[]
 for v in simple:
  a,b,c=[X[j] for j in sorted(adj[v])];N=cross(sub(b,a),sub(c,a));h=dot(N,a)
  if dot(N,X[v])<h:N=tuple(-x for x in N);h=-h
  assert dot(N,X[v])>h
  assert all(dot(N,x)<h for i,x in enumerate(X) if i!=v and i not in adj[v])
  gap=h-dot(N,g);assert gap>0
  ear_rows.append(dict(delete=v,target_inside_gap_sha256=sha256(B(gap)).hexdigest()))
 assert len(ear_rows)==133
 report=dict(object='CANONICAL_C622_SINGLE_FACET_COM_AND_BOUNDED_RELEASE_V1',parent_A_sha256=PIN,
  facets=movable,rows=rows,exact_facets=20,positive_gram_minors=60,
  bounding_facets=fixed,bounding_positive_weights=list(map(str,alpha)),
  bounding_affine_rank_determinant_sha256=sha256(B(dd)).hexdigest(),
  all_simple_ear_target_interior=ear_rows,ear_count=133)
 raw=B(report);Path(out).write_bytes(raw)
 print('CANONICAL_C622_TWENTY_SINGLE_FACET_COM_ACTUATORS_EXACT_PASS',flush=True)
 print('CANONICAL_C622_ALL133_EAR_TARGET_INTERIOR_AND_COMMON_BOUNDED_RELEASE_PASS',len(raw),sha256(raw).hexdigest(),flush=True)

if __name__=='__main__':
 assert len(sys.argv)==4
 exact_audit(sys.argv[1],sys.argv[2],sys.argv[3])
