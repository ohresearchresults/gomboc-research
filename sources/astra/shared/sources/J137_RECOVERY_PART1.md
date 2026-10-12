# J137 exact recovery capsule, part 1/2

Object identities: unchanged QW49I_LOW43_G9 with three new rational reference centres, and new J137_RAY_REF_G12. This is NOT a new own110 construction. LOW43 remains own121; the new ray body is own222. Both have V43/E123/F82,C246, weak000. Each listed reference centre is exact strict110/weak000, but is not its body's actual uniform-volume centroid.

Part 2 supplies every literal input. This part supplies the complete standard-library auditor. It enumerates all supporting triples, merges maximal coplanar facets, constructs their exact planar convex boundaries and true edges, integrates signed oriented tetrahedra, tests face/vertex/edge equilibria using Fractions, and records every positive physical/polar persistence interval. SciPy and floating signs play no role in acceptance. Floating numbers in the JSON are displays of exact fractions, not predicates. Strict edges are tested directly, not inferred solely from Euler.

Evidence: coordinator executed these units under Python 3.13.5. This audit was needed for newly computed reference points and the new ray witness; it was not a prerequisite to trusting the author's LOW43 result. The literal parent asg_WTYrOdQ2sp01hQDbBD8jRwWU was read completely, SHA175a3e59df4b325321fb17cd840963166f88abf8de551837f030f97202667928. The LOW43 input is byte-identical to the parent's 1534-byte primary input, SHAc9cfe9c62a5835f6aecbbb77513ab9727a6a2a08f34429d22e0873d76f9dc6f6. No claim is made to have independently replayed the parent's entire 44-unit package.

Recovery: save each fenced unit under its indicated filename, or extract with Python regular expression `r'### File: ([^\n]+)\n```[^\n]*\n(.*?)```'` using re.S across BOTH parts; write the second match group verbatim, UTF-8. All file units have a final newline. Do not strip source whitespace.

Run:
```
python exact137.py LOW43.json REFERENCE_CENTRES137.json
python exact137.py RAY_REF_G12.json ORIGIN137.json
```
Expected markers:
```
EXACT137_PASS LOW43.json 43 123 82 {'own': ([1, 2, 1], [0, 0, 0]), 'reference_max': ([1, 1, 0], [0, 0, 0]), 'reference_mid': ([1, 1, 0], [0, 0, 0]), 'reference_nearest': ([1, 1, 0], [0, 0, 0])}
EXACT137_PASS RAY_REF_G12.json 43 123 82 {'own': ([2, 2, 2], [0, 0, 0]), 'reference_zero': ([1, 1, 0], [0, 0, 0])}
```
Expected outputs: LOW43_EXACT137.json,8081 bytes,SHA9f1f178acafb4cd0fd9d315d5a34e631a5d842ae9fd207713c58cab023d35cc0; RAY_REF_G12_EXACT137.json,8105 bytes,SHAf82ca2bed83dcadd5a9212bbb12d1eeca26de4d7e75484aa48604f8a0f1ed7e9.

The same engine was also executed on all eight points of {-1,1}^3. It returned true V8/E12/F6, own(6,8,12),weak000: artificial triangle diagonals are correctly absent. This is a sanity test, not independent verification of the engine.

## Exact geometric argument behind the reference certificate
For a convex polyhedron about a strictly interior origin, a physical directed edge i→j with x_i·(x_j-x_i)>0 strictly increases |x|². A selected outgoing edge at every vertex except one therefore reaches that root and excludes every other unstable vertex. Apply the identical argument to the genuine polar polyhedron to exclude all but one stable face. The engine additionally tests strict extrema, all weak cases, and all actual saddle edges directly.

For edge endpoints a,b, let e=b-a, tau=-a·e/(e·e), q=a+tau e. The edge equilibrium is strict precisely when 0<tau<1 and q is a strictly positive combination of its two outward facet normals. Multiplying by their positive Gram determinant gives the two exact numerator tests in classify(). Boundary versions enumerate weak carriers. Interior face projections and supporting vertex radial planes are tested separately.

The two-field persistence calculation adds vertices at squared radius and edges at the minimum squared radius along their segment, pairing by the elder rule. It reports every strictly positive interval; zero-length events are not counted. It uses maximal-facet edges and the dual adjacency, never triangulation diagonals.

### File: exact137.py
```python
"""Complete exact convex-hull, uniform mass and equilibrium auditor.
Input: integer vertex cloud / common positive denominator. Enumerates ALL
support triples, merges coplanar maximal facets, and uses true edges only.
No SciPy hull or floating sign enters any acceptance predicate.
"""
import json,sys,itertools,math,hashlib
from fractions import Fraction as Q
from pathlib import Path

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(s,a):return tuple(s*x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def hull2(ids,W,n):
 drop=max(range(3),key=lambda k:abs(n[k]));axes=[k for k in range(3) if k!=drop]
 ids=sorted(ids,key=lambda i:tuple(W[i][k] for k in axes))
 def orient(a,b,c):
  x,y=axes
  return (W[b][x]-W[a][x])*(W[c][y]-W[a][y])-(W[b][y]-W[a][y])*(W[c][x]-W[a][x])
 lo=[];hi=[]
 for i in ids:
  while len(lo)>1 and orient(lo[-2],lo[-1],i)<=0:lo.pop()
  lo.append(i)
 for i in reversed(ids):
  while len(hi)>1 and orient(hi[-2],hi[-1],i)<=0:hi.pop()
  hi.append(i)
 out=lo[:-1]+hi[:-1]
 if dot(cross(sub(W[out[1]],W[out[0]]),sub(W[out[2]],W[out[0]])),n)<0:out.reverse()
 return out

def lattice(W):
 W=[tuple(map(int,w)) for w in W];planes={}
 for i,j,k in itertools.combinations(range(len(W)),3):
  n=cross(sub(W[j],W[i]),sub(W[k],W[i]));h=dot(n,W[i])
  if n==(0,0,0):continue
  side=[dot(n,w)-h for w in W]
  if min(side)<0<max(side):continue
  if max(side)>0:n=mul(-1,n);h=-h;side=[-s for s in side]
  gg=math.gcd(*n,h);key=tuple(x//gg for x in (*n,h))
  if key not in planes:planes[key]=[i for i,s in enumerate(side) if s==0]
 assert len(planes)>=4,'not three-dimensional'
 ordered=sorted(planes.items(),key=lambda kv:tuple(kv[1]));F=[];N=[];HH=[]
 for (a,b,c,h),ids in ordered:
  f=hull2(ids,W,(a,b,c));F.append(f);N.append((a,b,c));HH.append(h)
 EF={}
 for f,cy in enumerate(F):
  for i,j in zip(cy,cy[1:]+cy[:1]):EF.setdefault(tuple(sorted((i,j))),[]).append(f)
 E=sorted(EF);active=sorted({i for cy in F for i in cy})
 assert len(active)-len(E)+len(F)==2 and all(len(EF[e])==2 for e in E)
 for n,h,cy in zip(N,HH,F):
  assert all(dot(n,w)<=h for w in W)
  assert all(dot(n,W[i])==h for i in cy)
 return W,F,N,HH,E,EF,active

def mass(W,F,D):
 total=0;num=[0,0,0]
 for cy in F:
  for j in range(1,len(cy)-1):
   a,b,c=[W[k] for k in (cy[0],cy[j],cy[j+1])];d=det(a,b,c);total+=d
   for k in range(3):num[k]+=d*(a[k]+b[k]+c[k])
 assert total>0
 return Q(total,6*D**3),tuple(Q(x,4*D*total) for x in num)

def persistence(P,E):
 birth=[dot(p,p) for p in P];events=[(r,0,i) for i,r in enumerate(birth)]
 for k,(i,j) in enumerate(E):
  e=sub(P[j],P[i]);u=-dot(P[i],e)/dot(e,e);u=max(Q(0),min(Q(1),u));q=add(P[i],mul(u,e));events.append((dot(q,q),1,k))
 events.sort(key=lambda e:(-e[0],e[1],e[2]));uf=list(range(len(P)));elder=list(range(len(P)));on=set();bars=[]
 def root(i):
  while uf[i]!=i:uf[i]=uf[uf[i]];i=uf[i]
  return i
 for level,kind,k in events:
  if kind==0:on.add(k);continue
  i,j=E[k];assert i in on and j in on;a,b=root(i),root(j)
  if a==b:continue
  u,v=elder[a],elder[b]
  if (birth[u],-u)<(birth[v],-v):a,b=b,a;u,v=v,u
  if birth[v]>level:bars.append({'birth_vertex':v,'death_edge':list(E[k]),'birth':birth[v],'death':level,'relative_depth':(birth[v]-level)/birth[v]})
  uf[b]=a;elder[a]=u
 assert len({root(i) for i in range(len(P))})==1
 return sorted(bars,key=lambda r:r['relative_depth'],reverse=True)

def classify(W,F,N,HH,E,EF,active,D,c):
 X=[sub(tuple(Q(x,D) for x in w),c) for w in W];h=[Q(v,D)-dot(n,c) for n,v in zip(N,HH)];assert min(h)>0,'centre is not strictly inside'
 poles=[mul(1/b,n) for n,b in zip(N,h)];S=[];U=[];H=[];Ws=[];Wu=[];Wh=[];adj={i:[] for i in active};zeros={'physical_arrows':[],'polar_arrows':[]}
 for i,j in E:adj[i].append(j);adj[j].append(i)
 for i in active:
  z=[dot(X[i],sub(X[j],X[i])) for j in adj[i]]
  zeros['physical_arrows'] += [[i,j] for j,zj in zip(adj[i],z) if zj==0]
  if max(z)<0:U.append(i)
  elif max(z)==0:Wu.append(i)
 for f,n in enumerate(N):
  q=mul(h[f]/dot(n,n),n);slack=[h[k]-dot(m,q) for k,m in enumerate(N) if k!=f]
  if min(slack)>0:S.append(f)
  elif min(slack)==0:Ws.append(f)
 for e in E:
  i,j=e;a,b=X[i],X[j];v=sub(b,a);tau=-dot(a,v)/dot(v,v);q=add(a,mul(tau,v));f,k=EF[e];n,m=N[f],N[k];nn,mm,nm=dot(n,n),dot(m,m),dot(n,m);delta=nn*mm-nm*nm;assert delta>0
  aa=dot(q,n)*mm-dot(q,m)*nm;bb=dot(q,m)*nn-dot(q,n)*nm
  if 0<tau<1 and aa>0 and bb>0:H.append(list(e))
  elif 0<=tau<=1 and aa>=0 and bb>=0 and (tau in (0,1) or aa==0 or bb==0):Wh.append(list(e))
  for u,vv in [(f,k),(k,f)]:
   if dot(poles[u],sub(poles[vv],poles[u]))==0:zeros['polar_arrows'].append([u,vv])
 mp={old:i for i,old in enumerate(active)};P=persistence([X[i] for i in active],[(mp[i],mp[j]) for i,j in E]);QE=[tuple(fs) for fs in EF.values()];Qbar=persistence(poles,QE)
 for b in P:b['birth_vertex']=active[b['birth_vertex']];b['death_edge']=[active[i] for i in b['death_edge']]
 if not Ws and not Wu and not Wh:assert len(S)+len(U)-len(H)==2
 return {'strict':[len(S),len(U),len(H)],'weak':[len(Ws),len(Wu),len(Wh)],'S_faces':S,'S_carriers':[F[i] for i in S],'U_vertices':U,'H_edges':H,'weak_S':Ws,'weak_U':Wu,'weak_H':Wh,'primitive_zero_arrows':zeros,'P':P,'Q':Qbar,'centre':c}

def clean(x):
 if isinstance(x,Q):return {'q':str(x),'float':float(x)}
 if isinstance(x,dict):return {k:clean(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [clean(v) for v in x]
 return x

def audit(src,centres=None):
 W,F,N,HH,E,EF,active=lattice(src['rows']);D=int(src['denominator']);vol,g=mass(W,F,D);out={'name':src.get('name'),'V':len(active),'E':len(E),'F':len(F),'C':2*len(E),'active_vertices':active,'facets':F,'volume':vol,'own':classify(W,F,N,HH,E,EF,active,D,g)}
 for name,c in (centres or {}).items():out[name]=classify(W,F,N,HH,E,EF,active,D,tuple(Q(str(x)) for x in c))
 return clean(out)
if __name__=='__main__':
 source=Path(sys.argv[1] if len(sys.argv)>1 else 'LOW43.json');src=json.loads(source.read_text());centres={}
 if len(sys.argv)>2:centres=json.loads(Path(sys.argv[2]).read_text())
 out=audit(src,centres);out['input_sha256']=hashlib.sha256(source.read_bytes()).hexdigest();target=source.with_name(source.stem+'_EXACT137.json');target.write_text(json.dumps(out,indent=2)+'\n');print('EXACT137_PASS',source.name,out['V'],out['E'],out['F'],{k:(v['strict'],v['weak']) for k,v in out.items() if isinstance(v,dict) and 'strict' in v},flush=True)
```

Source exact137.py:6536 bytes,SHA140298b0806f9be76b2345c5c5a8ea45b3d629edfa86c03109d7b8f24ef902d2. The equality and weak conventions above are explicit. Do not turn a numerical MILP optimum, its node count, a reference110 certificate, or these transport hashes into a claim of own110 or a global shape exclusion.
