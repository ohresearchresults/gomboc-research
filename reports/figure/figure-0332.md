# figure-0332

Historical AI scientific report · saved 2026-09-06 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Rapid Atlas 04 — exact asymmetric one-pair successor from the corrected cut architecture

## 1. Determination

**No homogeneous strict (1,1,0) winner was obtained.** This continuation produced and independently verified a new exact rational homogeneous polyhedron:

**RA04-ASYM-H123-COND-R12: (V,E,F)=(242,363,123), strict own-centroid (S,U,H)=(1,2,1), with no degenerate equilibria.**

Its true-edge budget is **2E=726**, and its formal mechanical complexity is **724**. It has one stable maximal octagon, two unstable vertices, and one saddle edge. Every true-feature mechanical primitive used by the primary census is nonzero.

This reduces the corrected CUT148_U7 branch from six unwanted unstable–saddle pairs to one. It is **not** a new global record for class(1,2,1), and it is not the lead’s separate COORD-H107-S1U2-R12. The remaining pair is robust, not a near-zero numerical wall.

The successful operation was an **asymmetric replacement of the supporting-plane architecture**, with actual three-component volume-moment closure. It is **not an all-inward staged-cut descendant**: the new body extends outside ARCH274 and is not C3-invariant. The pure sequential-cut attempts did not complete the target. The distinction matters: the valid one-wave diameter-ball obstruction was escaped by leaving its hypotheses, not refuted.

## 2. Parent identity and source reconciliation

The authoritative parent read for this assignment was `figure-0330`, SHA-256 `30d790145009a47baf5205296a665b89d31e8212b2f77ca059cffdf69473a4cc`.

The actual starting geometry was its corrected ARCH274/CUT148_U7 table. The ARCH274 row beginning `-4581451990` uses third coordinate **5980611542**. The inconsistent older47-row table beginning `-3537051546` was not used. The journal’s explicit correction and its distinction between the two source objects remain in force. :contentReference[oaicite:0]{index=0}

The parent’s accepted cut endpoints remain distinct: CUT148_U7 is292/438/148, class(1,7,6); CUT166_DEEP3 is304/456/154, class(1,7,6). The assignment’s compact description “176” denotes the equilibrium class, not176 vertices. Their own-centred construction and complete defining rows are preserved in the immutable payload. :contentReference[oaicite:1]{index=1}

The new endpoint below has its **own complete123-row H definition**, so reconstructing it does not require recovering an optimizer checkpoint, an old cut selector, or the defective table.

## 3. Complete finite definition

Decode the H payload in Section9. It expands to6672 bytes of ASCII text containing123 integer quadruples `(a,b,c,h)`, one row per line.

**Every row represents exactly ONE inequality**

`a*x+b*y+c*z <= h`.

There is **no cyclic expansion**, no normalization of the integer coefficients, and no implicit symmetry. All123 inequalities are active in the final body.

Let K be their closed intersection, filled with constant density1. Reconstruct its exact rational vertices and maximal facets by the procedure and executable below. Compute its actual ordinary volume V and first-moment vector M, and put

`g=M/V`,

`P=K-g`.

**P is the exact own-centred body claimed here.** The raw origin is not substituted for g.

The complete H text has SHA-256

`f74a0fcaa1b4a64e43f58212646746dea0fe85db6dc2d5aa674d6f8b451c8f57`.

### Canonical incidence

Enumerate every nonzero-determinant triple of supporting planes. For rows `(n_i,h_i),(n_j,h_j),(n_k,h_k)`, use

```text
d = det(n_i,n_j,n_k),
p = h_i(n_j cross n_k)+h_j(n_k cross n_i)+h_k(n_i cross n_j).
```

Normalize d to be positive. Retain `p/d` if and only if it satisfies **every** supplied inequality exactly. Reduce the homogeneous quadruple by its positive gcd, deduplicate, and sort the actual rational Cartesian coordinates lexicographically. This defines vertex indices0 through241.

For each plane, collect its complete exact equality-contact set. Its exact planar convex hull, oriented outward, is one maximal facet. Rotate each cycle to begin at its smallest vertex index. The distinct unordered consecutive pairs in these cycles, including closing pairs, are precisely the true edges.

The executed reconstruction gives:

```text
V=242, E=363, F=123.
Maximal face sizes:
3:7, 4:23, 5:46, 6:20, 7:7, 8:6,
9:4, 10:4, 11:3, 13:1, 18:1, 26:1.
```

Fan-triangulation of these polygons gives480 outward integration triangles and720 display edges. **357 exactly coplanar diagonals are display-only**, not physical edges.

The normal directions positively span space. A four-row certificate uses input rows `[0,1,2,15]`; the alternating cofactors are all positive:

```text
428650945812109644159694324866152699
87856775497339538110509593673890331
860929285167870508108610760348297252
754103202610983783306375724521964976
```

Together with strictly positive raw support heights, this establishes a bounded full-dimensional intersection containing the raw origin strictly inside.

## 4. Ordinary volume, actual centroid, and exact mass closure

For the outward polygon-fan triangles `(i,j,k)`, let

`Delta_ijk=det(v_i,v_j,v_k)`.

The primary implementation computes

```text
V = (1/6) sum Delta_ijk,
M = (1/24) sum Delta_ijk*(v_i+v_j+v_k),
g = M/V.
```

All these are finite rational sums over the actual reconstructed boundary. They are not vertex averages, quadrature estimates, or moments of an obsolete incidence cell.

A separate implementation integrates nonnegative tetrahedra with a boundary vertex as apex and obtains **exactly the same rational volume and centroid**. For the translated body P, the centred first moments are the exact identities

`M_x-V*g_x = M_y-V*g_y = M_z-V*g_z = 0`.

This is not a claim that the raw moment is zero. The raw centroid is small but nonzero and has unequal coordinates:

```text
9036506742524/10^12 < V < 9036506742525/10^12,

-129566/10^18 < g_x < -129565/10^18,
7160/10^18 < g_y < 7161/10^18,
216198/10^18 < g_z < 216199/10^18.
```

For orientation only,

```text
V ≈ 9.036506742524375,
g ≈ (-1.2956515208450837e-13,
       7.160679245254527e-15,
       2.1619874686465627e-13).
```

The enclosures are not definitions. The complete integer H table and displayed finite sums determine the exact rational numbers. The executable writes their full numerator/denominator strings.

The successful primary implementation uses heterogeneous rational coordinates and origin-based tetrahedra. An earlier common-denominator audit on a rejected numerical proposal timed out; it is **not** counted as a completed pass or as direct reintegration of this final table.

## 5. Full equilibrium census and positive margins

### Exact own-centroid features

```text
Stable maximal face:
[28,227,231,230,46,41,36,30]

Unstable vertices:
[60,231]

Saddle true edge:
[211,229]

Degenerate equilibria: none.
Zero true-feature mechanical primitives: 0.
```

Vertex231 is the unique maximum-radius vertex. The stable plane is independently the unique minimum-distance support. The second unstable vertex60 and saddle[211,229] remain genuine open features.

All indices refer to the **new242-point rational table**. In particular, `[211,229]` must not be replaced by an index pair from the earlier unconditioned or numerical H123 proposals.

### Direct mixed-normal-cone audit

For a centred edge from a to b, put

```text
d=b-a,
L=d·d,
T=-a·d,
W=L*a+T*d.
```

For its two outward incident normals n,m, the Gram determinant is strictly positive:

`G=|n|^2|m|^2-(n·m)^2>0`.

The two normal-cone coefficient numerators are

```text
beta_n=(W·n)|m|^2-(W·m)(n·m),
beta_m=(W·m)|n|^2-(W·n)(n·m).
```

A strict saddle requires **all four** of `T,L-T,beta_n,beta_m` to be positive. Both full implementations enumerate all363 true edges and evaluate their full cones. The unique passing edge is[211,229]. Every other edge has a strict exclusion component. H is not inferred from Euler.

Maximal faces are tested by their literal perpendicular feet and true polygon sides. Vertices are tested by their complete normal cones; the independent implementation additionally tests every vertex against every other vertex.

### Certified normalized margins

Conservative exact rational lower bounds for this body are:

| Predicate family | Strict lower bound |
|---|---:|
| Every nonincident supporting-plane distance | >1/12000 |
| Stable face’s minimum side margin | >1/10 |
| A strict exclusion for every nonstable face | >1/2100 |
| Each unstable vertex’s minimum adjacent-edge cone margin | >13/100 |
| A strict escape witness for every nonunstable vertex | >1/18000 |
| Saddle’s minimum four-component margin | >4/25 |
| A strict exclusion component for every nonsaddle edge | >1/18000 |

For centred a,b and outward normal N, the normalized face-side expression is

`N·(a cross b)/(||N|| ||b-a||)`.

The normalized endpoint expression is

`-a·(b-a)/||b-a||`.

The two incident face-side signs are separately checked against the Gram-cone signs. Integer ceilings of square roots give rational denominator bounds; the acceptance does not depend on floating square roots.

These expressions are1-Lipschitz in the reference centre. The recorded strict bounds therefore imply that the **complete strict class(1,2,1) persists throughout the closed Euclidean reference-centre ball of radius1/20000 around the actual centroid**. This is a reference-point result for one fixed physical body, not a coordinate-perturbation guarantee or manufacturing tolerance.

## 6. Exact evidence that the one-wave hypotheses have been left

The accepted body is not an inward-cut subset of ARCH274. Its raw vertex231 is exactly the homogeneous quadruple

```text
(173717142195659072811710816699925242,
 -173996731429187130721613056793902149,
 -255123395018333739940116996977823654,
 147456981712395965418209097147610245).
```

The last entry is the positive common denominator. Against the literal ARCH274 inequality

```text
(1957737524,-9423925590,-2712358801)·x <= 10321609317,
```

this point has violation divided by the old normal’s length **greater than3/4**, checked exactly.

It is also not C3-invariant about its own centroid. Let `R(x,y,z)=(y,z,x)`. The point `R(v231-g)+g` violates the new inequality

```text
(-550607651741,-660688837195,510217085416)·x <= 1466201541440
```

by a normal-distance **greater than9/10**, again checked exactly.

Thus both the retained-subbody and C3 assumptions of the parent’s one-wave diameter-ball exclusion fail. The exclusion itself remains valid within its stated scope. The construction does not prove that sequential inward cuts alone can solve the problem.

## 7. What was tried and what materially changed

### 7.1 The stipulated sequential-cut route

The literal two-stage escape was reconstructed as a numerical starting control. Its second face foot enters the original body but is excluded by the first cut, as in the parent. Opposite-sign moment compensation was then searched using actual finite-hull integration.

A2400-direction compensation screen did not complete mass closure. A greedy positive-side continuation reduced the common centroid displacement from about0.015 to about0.0084 by activeF166; continuing beyond that reached about0.0063 only in an activeF187 body, outside the sufficient facet budget. These are finite search outcomes, not capacity theorems.

A20-plane asymmetric sequential-cut optimization imposed current-prefix foot exclusion, all three actual volume moments, and forced removal of the diameter-ball witness. Its bounded120-iteration run ended with a nonzero centroid and an unsatisfied forced-removal constraint. It is not an accepted successor.

Further current-safe, paired-cut, and geodesic normal-chain proposals either retained the protected witness, failed the moment equations, or exceeded the active-facet budget. No numerical state from these searches is labelled110 or exact-certified merely because it had fixed-origin S1.

### 7.2 The successful asymmetric support replacement

The reframe allowed individual supporting normals and offsets to move, rather than restricting every change to an additional inward halfspace.

For numerical unit-normal rows, a directed witness tree rooted at the negative axial stable plane enforced

`h_i(n_i·n_parent)>h_parent`.

Its support heights strictly decrease toward the root, so it is acyclic. Positive logarithmic reserves parameterized these inequalities. They exclude every nonroot plane foot at the numerical reference and keep the root plane stable.

That S1 construction alone is not homogeneous. **All three actual tetrahedral first moments were constrained independently**, and the actual convex intersection and its incidence were rebuilt at every evaluation. No C3 moment cancellation was assumed after symmetry breaking.

To measure whole regions rather than one small edge defect, a numerical component-merger objective was built on the actual true-edge graph. A vertex carried squared radius `f_i=||v_i||^2`; an edge carried

`b_ij=min_(0<=t<=1)||(1-t)v_i+t v_j||^2`.

Descending edge levels merge connected components; the lower surviving peak supplies a peak-to-merge loss. Initially, minimizing squared losses spread a large defect into many smaller extrema. A square-root version used the direct geometric identity for an interior edge foot,

`sqrt(f_i-b_ij)=|v_i·(v_j-v_i)|/||v_j-v_i||`,

instead of subtracting nearly equal squared radii. This reduced cancellation error near endpoint events.

These graph losses were discovery objectives, **not certificates of physical equilibria or basin topology**. Final repair imposed a positive radial-escape reserve for every nonmaximum vertex while retaining two robust maxima. It removed all other unwanted maxima; it did not cancel the last pair. A subsequent conditioning solve enlarged the nonstable-face reserve while preserving the three actual mass equations and all nonmaximum exits.

The accepted sequence recorded in the research archive is:

```text
CUT148_U7
 -> PERS1 -> PERS2 -> PERS3 -> PERS4 -> PERS5
 -> SPARSIFY1 -> SPARSIFY2 -> SPARSIFY3
 -> GEO1_checkpoint -> REPAIRED2
 -> COND3 -> COND4_best.
```

The bounded numerical controls were: PERS stages75,75,75,75,90 iterations; sparsification reserves1e-4,1e-4,1e-5 with160,110,110 iterations; GEO1 120 iterations; radial-escape repair reserve1e-4 with120 iterations; conditioning stable-foot reserves1e-5 and5e-5 with120 iterations each. Complete programs, inputs, logs and checkpoints are retained in the discovery archive.

The final123 active rows from `COND4_best.npz` were rationalized on a10^12 proposal scale. The **literal final H coefficients**, not the optimizer’s floating centroid or its stopping label, define the accepted body. Exact reconstruction then recomputed its own centroid and every feature.

### 7.3 A rejected false near-count and the remaining numerical trap

`GEO1_best.npz` appeared numerically(1,2,1) under a1e-8 feature threshold. Its rationalized H table was actually **(3,2,3)**: two weak stable–saddle pairs had been hidden together, so Euler’s identity did not expose the incorrect numerical count. That table was not promoted. The later positive-reserve repair and conditioning produced the different exact body defined here.

Further local escape minimization could make an objective extremely small by collapsing a tiny facet at the unwanted maximum, while a substantial whole-region barrier remained. This was not an equilibrium cancellation. Free-height, rooted-arborescence, and additional cut continuations did not produce an accepted110 endpoint. In particular, small objective values, inactive rows, and solver termination were never substituted for a full own-centroid exact census.

## 8. Remaining finite geometry and the next useful continuation

The new one-pair body leaves45 additional facet slots before the sufficient boundF<=168. For any convex3-polytope, `E<=3F-6`, so F<=168 guarantees **E<=498**. Simplicity is unnecessary, and a useful intermediate operation need not decrease E monotonically.

The extra maximum60 is incident to input support rows `[93,113,119]`. Their maximal cycles are

```text
93:  [52,73,60]
113: [60,73,79,84,87,89,92,95,98,111,131,104,67]
119: [35,43,49,52,60,67,62,57,48,45,44].
```

The sole saddle[211,229] is incident to rows64 and114:

```text
64:  [161,186,211,229,232,205]
114: [163,167,168,229,211,175,164].
```

A shortest combinatorial dual route from an extra-maximum incident face to a saddle incident face is

```text
113 -> 115 -> 64,
115: [104,131,151,164,175,186,161,156,150,141].
```

This is a concrete connected support region for simultaneous replacement. It is only a face-adjacency route, not an asserted gradient separatrix or a proof that a prescribed patch is feasible.

The next useful search should replace that entire region and its complete incident stars, permitting old rows and vertices to become inactive, while closing all three solid moments. Isolated truncation of vertex60 has already exhibited the peak-transfer/tiny-facet failure mode. The target maximum231 and the stable octagon are robust, but their identities need not be protected at the cost of blocking a real cancellation.

For fixed normal directions and affine support-height controls on a **verified actual incidence cell**, vertices are affine, volume is at most cubic, and first moments are at most quartic. A scalar algebraic root or a multi-control exact solve must be paired with incidence and all-feature sign checks on its root box. Crossing a circuit requires rebuilding the actual cell and its moments. No specific next root or successful cancellation is claimed.

## 9. Complete runnable recovery capsule

Save the following as `EXACT_BODY.py` and run

```text
python -S EXACT_BODY.py REBUILT
```

It has no external data dependency. The embedded payload is the entire123-row H table, not a locator or a partial mask. The program reconstructs the full finite boundary, actual ordinary moments, own-centroid full feature census, and exact nondegeneracy. The separate independent implementation and the complete fresh replay are in the proof packet.

The development interpreter was Python3.13.5. Exact replay uses only its standard library. Numerical discovery used NumPy2.3.5, SciPy1.17.0, PyTorch2.10.0+cpu and NetworkX3.6.1. Reproducing the accepted object does not require bit-identical optimizer output. Do not use Python `-O`.

```python
import sys,json,math,itertools,base64,zlib,hashlib
from fractions import Fraction as F
from functools import reduce
from pathlib import Path
sys.set_int_max_str_digits(0)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def mul(t,a): return tuple(t*x for x in a)
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def canon(a):
 d=reduce(math.gcd,map(abs,a));assert d
 return tuple(x//d for x in a)
def run(reps):
 rows=list(dict.fromkeys(canon(tuple(r))for r in reps));N=[r[:3]for r in rows];hh=[r[3]for r in rows]
 assert all(h>0 for h in hh)
 cert=None
 for ii in itertools.combinations(range(len(N)),4):
  ns=[N[i]for i in ii];v=[(-1)**k*det(*[ns[j]for j in range(4)if j!=k])for k in range(4)]
  if all(t>0 for t in v)or all(t<0 for t in v):cert=(ii,v);break
 assert cert is not None
 C={}
 for i,j in itertools.combinations(range(len(N)),2):
  C[i,j]=cross(N[i],N[j]);C[j,i]=mul(-1,C[i,j])
 pts=set();triples=0;tests=0
 for i,j,k in itertools.combinations(range(len(N)),3):
  triples+=1;d=dot(N[i],C[j,k])
  if not d: continue
  p=add(add(mul(hh[i],C[j,k]),mul(hh[j],C[k,i])),mul(hh[k],C[i,j]))
  if d<0: p=mul(-1,p);d=-d
  for n,h in zip(N,hh):
   tests+=1
   if dot(n,p)>h*d: break
  else: pts.add(canon((*p,d)))
 P=sorted(pts,key=lambda p:tuple(F(x,p[3])for x in p[:3]));assert len(P)>=4
 X=[tuple(F(x,p[3])for x in p[:3])for p in P]
 def delta(i,j): return sub(mul(P[i][3],P[j][:3]),mul(P[j][3],P[i][:3]))
 faces=[];normals=[];heights=[];active=[]
 for fi,(n,h) in enumerate(zip(N,hh)):
  ids=[i for i,p in enumerate(P)if dot(n,p[:3])==h*p[3]]
  assert all(dot(n,p[:3])<=h*p[3]for p in P)
  if len(ids)<3: continue
  drop=next(k for k in range(3)if n[k]);axes=[k for k in range(3)if k!=drop]
  ids.sort(key=lambda i:(X[i][axes[0]],X[i][axes[1]]))
  def turn(i,j,k):
   u,v=axes;return (X[j][u]-X[i][u])*(X[k][v]-X[i][v])-(X[j][v]-X[i][v])*(X[k][u]-X[i][u])
  def half(seq):
   out=[]
   for i in seq:
    while len(out)>1 and turn(out[-2],out[-1],i)<=0:out.pop()
    out.append(i)
   return out
  f=half(ids)[:-1]+half(ids[::-1])[:-1]
  assert len(f)>=3 and set(f)==set(ids)
  if det(n,delta(f[0],f[1]),delta(f[0],f[2]))<0:f.reverse()
  z=f.index(min(f));f=f[z:]+f[:z]
  faces.append(f);normals.append(n);heights.append(h);active.append(fi)
 E={};stars=[[]for p in P];adj=[set()for p in P];support_tests=0;polygon_tests=0
 for fi,(f,n,h)in enumerate(zip(faces,normals,heights)):
  contacts=[]
  for j,p in enumerate(P):
   s=h*p[3]-dot(n,p[:3]);assert s>=0;support_tests+=1
   if s==0:contacts.append(j)
  assert set(contacts)==set(f)
  for i,j in zip(f,f[1:]+f[:1]):
   for k in f:
    if k not in (i,j):assert det(n,delta(i,j),delta(i,k))>0;polygon_tests+=1
   E.setdefault(tuple(sorted((i,j))),[]).append((fi,i,j));stars[i].append(fi)
 assert len(P)-len(E)+len(faces)==2
 for (i,j),ss in E.items():
  assert len(ss)==2 and ss[0][1:]==ss[1][1:][::-1];adj[i].add(j);adj[j].add(i)
 for i in range(len(P)):
  assert any(det(normals[a],normals[b],normals[c])!=0 for a,b,c in itertools.combinations(stars[i],3))
  link={j:set()for j in adj[i]}
  for fi in stars[i]:
   f=faces[fi];p=f.index(i);a,b=f[p-1],f[(p+1)%len(f)];link[a].add(b);link[b].add(a)
  assert all(len(s)==2 for s in link.values());todo=[next(iter(link))];seen=set()
  while todo:
   k=todo.pop()
   if k not in seen:seen.add(k);todo.extend(link[k]-seen)
  assert seen==set(link)
 todo=[0];seen=set()
 while todo:
  i=todo.pop()
  if i not in seen:seen.add(i);todo.extend(adj[i]-seen)
 assert len(seen)==len(P)
 # Actual ordinary mass from origin-based tetrahedra.
 V=F(0);M=[F(0)]*3;T=[]
 for f in faces:
  for j,k in zip(f[1:-1],f[2:]):
   i=f[0];T.append((i,j,k));v=F(det(P[i][:3],P[j][:3],P[k][:3]),6*P[i][3]*P[j][3]*P[k][3]);assert v>0;V+=v
   for d in range(3):M[d]+=v*(X[i][d]+X[j][d]+X[k][d])/4
 assert V>0;g=[m/V for m in M]
 q=math.lcm(*(c.denominator for c in g));p=tuple(c.numerator*(q//c.denominator)for c in g)
 Z=[sub(mul(q,v[:3]),mul(v[3],p))for v in P]
 assert all(q*h-dot(n,p)>0 for n,h in zip(normals,heights))
 S=[];U=[];H=[];deg=[];zero=0
 for fi,(f,n,h)in enumerate(zip(faces,normals,heights)):
  nn=dot(n,n);foot=add(mul(nn,p),mul(q*h-dot(n,p),n));den=q*nn
  sg=[det(n,delta(i,j),sub(mul(P[i][3],foot),mul(den,P[i][:3])))for i,j in zip(f,f[1:]+f[:1])]
  zero+=sum(x==0 for x in sg)
  if all(x>0 for x in sg):S.append(f)
  elif all(x>=0 for x in sg):deg.append(['F',fi])
 for i,z in enumerate(Z):
  sg=[-dot(z,delta(i,j))for j in adj[i]];zero+=sum(x==0 for x in sg)
  if all(x>0 for x in sg):U.append(i)
  elif all(x>=0 for x in sg):deg.append(['V',i])
 for (i,j),ss in sorted(E.items()):
  d=delta(i,j);ell=dot(d,d);t=-P[j][3]*dot(Z[i],d);foot=add(mul(ell*P[j][3],Z[i]),mul(t,d));n,m=[normals[s[0]]for s in ss]
  a,b,c=dot(n,n),dot(n,m),dot(m,m);assert a*c-b*b>0
  dn,dm=dot(foot,n),dot(foot,m);sg=[t,q*ell-t,dn*c-dm*b,dm*a-dn*b];zero+=sum(x==0 for x in sg)
  if all(x>0 for x in sg):H.append([i,j])
  elif all(x>=0 for x in sg):deg.append(['E',i,j])
 assert len(S)+len(U)-len(H)==2
 return dict(V=len(P),E=len(E),F=len(faces),class_=[len(S),len(U),len(H)],degeneracies=deg,primitive_zeros=zero,volume=str(V),raw_moments=list(map(str,M)),raw_centroid=list(map(str,g)),centred_moments=[str(M[i]-V*g[i])for i in range(3)],positive_span_certificate=cert,homogeneous_raw_vertices=P,faces=faces,true_edges=sorted(E),triangles=T,active_rows=active,stable_faces=S,unstable_vertices=U,saddle_edges=H,triples=triples,construction_support_tests=tests,global_support_tests=support_tests,polygon_tests=polygon_tests)

DATA='''
c-noLTaqj%3`GBH6>Oj*Kp-Cb-<Z$QIQ(hb;oH+w1wu+?rntX-_BeZ=*Y9d`&)l=Gz29hi^>cTuxkhgz=iDRTd9lXFmzneQ$i3Rl
(eJ#2cTW4Qog>B?>#p5~D~y%nzC7RIp*}|5o|gyT8Z+O#^W3)lu-}{~vW+qNV#9Oa9^dcq#9OD2?7hWYIs03&2`W$aIpzyqB*L+R
t@hk&ePhS$lR((C-Em{B)qC*6FM04zkMNceE`ojY?RUS!YuPi;+dR1Y8MpITKfBE}--+EjyAxp#zP*R-*7v)+KaLpda+Dttur;68
X-QUZ?}NidW1HA{$Lal!Z`{*w<T!B~HF!SP;{^K>GzB3Sn`HD&u-2u={_@=$<K)^@>vzZ!Td#A1+I9ASi#;yM@Y~=M=S)+$I;A2D
yIUg8G5E;ZjUwFH`zEi42>EmGJV8mnABE@ra|XF<R&mc@i|N)c1~K=!37>Kuz|g7FeV@4zM)&4!Kk~}XhpoqM5maQoI+3Z*Itsvv
??>FAs0+r~z}DDQjg`rEu6M=*UgR*l@c}Zj|NUn4ZasUR*>=S0>_<(K2!R9WJ*0})c#21k$6jA-3QhQ+(FkKkknwE?1f{rxv;jum
x&tu32e>!sxO-Ei$!@Pja)>dB|B%v4`grS^0A2%43F7CQymoRQ7NEM1%^s<yDS!;?4|?ix{`-!F=G*b+I1ki6&_=(3cOgOO>rfl^
6nt|4UpAp&Nw<QRLH0foyF~ozF&cQMJy?53Z*EA~@3M>ur3vpj8!UY>Hn|~9$#ai)`lV629Y9h@7^$KO%tkIsYiG|7*bcx*0SCvL
hmG@|eW(NQ>Dws4gUx(9?M2eY{5%LGu-_waAp2@>`fW86#GyEDx6A+~z=bP*0lpSTrk=0eDc?|8T9am`vM|={CyelHXoVx*XM{lN
1w=Kf>jU<JN(hD2ST9xwaOQJ^sYRjB`+lI6(oqut&cO!dSeGNP1|WufGAXW*3PBGh($oi>@rd^FI%Q6a37~k2_dt3~zQ|cfWM@t^
I2qKDRBKC@o(2Y3Zbuggs+WZa-Xg)BVC^_IOQ8#X^9GbVE+J7p$cwkmO`>A)xUxs|`{>m>rBWJT!f6{s5*D>SMU7;p{Q_3D3qa_p
jt1&{@fYO?)BtpX6ZvDw6KUzl5Ha#>*qIF&5)^xlnCW{^#^E!6_~fSC_l!Tr?@9N<@~?R30J*!sCsaW713ZD&{o0|x!1~g&a`Gc}
U>C3zH$pmbt#^J9I;h~qR9*ln#j;#oZj?-TZANvqby^6DT@CnV^~JMrDpr6%nrBzxu4ynFbGhJ3San25JxI^>xM42YN{o(Cs{nlt
EoJ#$kvs)PgUAVsgn9;5k;`emySQN$U<?;?a8!btkA2~S+&m#a@*+KwN0FKEDAWT<<Y*EFN2fdZLE5wRB~2O*nnyBtj?%WNM1Xxs
UO1D)cr+AhPsKSjnt|Mt6>9W`N+!F}=MoqvI@St+aX`{yF84#5=qrRkT$&IP`Gh^~dO1uVRefkM$@$SP@E)kn`Y&Ww^2V9~Wk{xg
;Yw<$fFOc2<ea3$rh_7=Ho>WDse;mmB#<>hD|^vNP{B{d!xn^0A|tcr(!RW2hl4422i^B{vMU>q?FJZ-tu8@(IIO|Ju}~oj0IywB
+@FU7Cn&OXg??Xucrz3YQ9!$1wjWY*sM0oubb{O>Q-~;0{bYEmu~3*w$%G|9O_)jmvL=<MyJ)%VnkG_N`bl1YjJ<4CIt;wg)QePJ
83=@#44wp`8ZeqP8<}HunuPrb6Lq3k@m^^gu8HU+CE5l0#EH;kRSqZ|#9(UDoY=TauQk@U{_F<?Qz+qO1RU^T32xCay?8v@(ME8h
rP9;Y1Aqdj3_DKGftcZk8Uly#pl?U(gJC()H<l*VdOQHXrE-vhM(^F^<Um9Urog0YywcGC5W|9hgnH1IiLmHe&P(kG`V^1?rxn^!
Y_1K^1rk>|x<Vi}b69Itm6I$eXqgwRDTdh)i@s?Y!~}>yjCvcyq~YFle(JlP?v@+XC$B$X9mAkgzD0|NKIrwTwB8yYlQ;<|5x!&<
2+<I`CISLYdyNhxBD!j-vUK43qtg<OEoqt-@qvy!E2?9HtaTX6>`*iLr62+%;8h-@X?9^Bhyh8oU+nXxYKkE$A`b;oQ;q9FAw~a@
vKF8<B&3M9a`8A7Q&ig0P110zWQ3gP38GmDhNI9(6o`%qxDzCDH2WCmM}tGPbUk1>f9{mH<W&w`e3J6`n}4N%o}4aV2KHsLL8G=J
dL2U?6!b+90FpJ-C@_i-q@*P_XeA^FCL7z+x=*EBdUx2IHCZG+V$toQ#W04j*O720b|SxY$i6BwxOWhs!%&THJ7u7GW)vto2_Y%^
lZGB(*$}w0xScaYg(wOm31x;CrrgV@#e-c>yOcPR0fL}kN>OjYeEVo*K6n&ukhSR}3<C5+%yi^xq`<B4p~q2+(%|UtzixzhX*Tr7
vpAEm`y*G0UXvJoVK0u`;t7_UrXCt(Git^p*1+Qw1`Z1z^JzsK2&!T<qq%?meVl0%5)pV9uzf&1SOpOv4e5~zr4nV^u5xtvOkCF^
0(PT<E9iaJqF_`EFk<j5nC-gROtSn09*|aZ$>Mfo<QE~e!pFy`Boz1JD5&WI)>JG?Mxf16sMoD4ehkOe+vWafmH|{w`GmezY9Pk^
M+NquuL_q$te{{6(gLb4FlVa1HWFFHsSSNTV(t2r4@$%Mm_<)Zx=4{(#MIL&{JwuA9lC&ritm|7QE|Et@PjH=4uj15=iZkn*`l7J
J8ZzAe`?HRhO|M3mOb?3RL2PI4M!g5T&LJ2o!EZqn9gU=qm=2W*!{+=Y0Ks!K&J4IN@%Yju`_hWXW2-4wiaFi5Lh@3P}Wl;JcA>3
hR^E@I-I;c^%FP6_RM*Vh;FWkI?Fgk9<Lofo|;-i5MZ4_7f90M!U&whQfhk529;(tR*LV?H}VTflR9YDT;6u{I;G<!gbHvJ!l7M*
tU(8;;mn%WY@61yd^8J7;P%qM_}BS@>5TlLUwC&`U;z?cY(F%K{6qhZ_7Klkh+9O+M%0y2gKpGGKRohP<>3`aUM(X81?nLUQlh14
WmRYtQiVMGf9j}ro(;g#wYcb|L?A1WLTUkL>9e*6*f6k4n$F@NLT#m98V3AR(3kp12mf;4)E;Ig#Je;)UhS}B*EEnPe5)4OpFlI4
Ibzq12A%<^bon3N7J23#8=)m~M)RVi+%W>fJ6Ao|e^VpQ#A@!R&GZ%r+;W~pNYKu)@R(i(ON_3!7i6-odybQ83SvLj%}KgLcx}LU
<XrtDF))a!T)6({P>1V-b}B=6VsD`x>^AybHE!f{Dw8)ArM%v#m4L-pjut7902)%hZ}pWBnY~;ZtQtZeI6$Fv><c^#Q6YN_-lv@Y
*6Llb+GHv|@hlu98oiw02`xJ)m<~Gd^lh9D-GFoOymSw-!Q48CMjLQ4XII?RhY#?o2}+zajJG8YWvMaq#wPHb4p<gjR^OBcyNJk>
8GYOm?FgtA9C|sDt5yaEt*Z(<1>Jz-B^_!Ob$;BavozfkP{kpk;)=H0bxX$ZsX^G5i@9AOVQ{1Q3CUp|U`G9&$`V9g9E|tT4TUr2
2m8=RbW4;o1;LPyvESx3fd0QURGAd~$SS5Ax_KH6qMB{hZ5DW&g+%O>UX<a+V=;lS2%)FM?N$IE_(F5}%DCS~WfU-QsND`P103hk
w$G8BX2!Q*32Iz?R)oHrt**KPj@-^Pq3czXz>1y^Y@!yP1ta?4DDP%cx0&X6Or;8bfDKuUQ_DEp-wD3myl>T%(X4g55lTeb5#=u@
U5eV@3ny~EUCt0q2xWr?b4+e2oOCrPtlH;941mdr<0j_UyPmF_Cl`>gjfqdH8_c?0Q=L_kx*0BKM9znERyI0|;?rJUV>&`EZ~82!
0fPPG=xMRUQFL=4SXFik@zgrGwwK-=yM#6-aX8(5s{L&Y{5@fm<8(ZA4R2AsB*cMx0adr2-aP~;BrR0P%i%|Xm_X>WcfBH`u6&7?
+KLezh5i6i@C1<}He`;f=%#SYUS3Y8FK{b?qk_8x;?$HQBZG}j!wvbMi=mxaH=N=15G0^t>MgxjGw=l>Kbp>o1lILbz{kK-z7X~B
RIiIJ_TW_Xk^(yv>Fq$R_H3PBDPVZXuC#bFK#N4txNZs_lx^wM?x~tLo*cm2P4s0t(S%ud9@)1hdO(3v;+%jMqXyY~IstF;=uG(W
?=tLV)ya1N|IN>fRj+TJvLk_m6}XAv3C>|r`KMG8+;Il1(Deq0TGG%Y0J?P~<SEu6p6i7O=U75kGU3<YsLxN^1xI20rMc}*7Yw0S
d3A&2rp~Y+%yFZ8tLT8JpAgOHjTbhgRSG+8*JTcIb^q4HzY~D|;2%entnn4WhP{8PAyi|7XLA&QC$EyPy_R{kb<67to80R>4%2G%
R8-_pWfg{|S1eR|JvIDG76mIc=X4x1F%<YeKfV9{;kADNEZZLt
'''
H_SHA='f74a0fcaa1b4a64e43f58212646746dea0fe85db6dc2d5aa674d6f8b451c8f57'
def decode():
 raw=zlib.decompress(base64.b85decode(''.join(DATA.split())))
 assert len(raw)==6672 and hashlib.sha256(raw).hexdigest()==H_SHA
 rows=[list(map(int,line.split()))for line in raw.decode('ascii').splitlines()]
 assert len(rows)==123 and all(len(r)==4 for r in rows)
 return raw,rows
def run_to(directory):
 directory=Path(directory);directory.mkdir(exist_ok=True,parents=True);raw,rows=decode();a=run(rows)
 assert [a[k]for k in ['V','E','F']]==[242,363,123]
 assert a['class_']==[1,2,1] and a['degeneracies']==[] and a['primitive_zeros']==0
 assert a['centred_moments']==['0','0','0']
 (directory/'H_FULL.txt').write_bytes(raw)
 json.dump({'name':'RA04-ASYM-H123-COND-R12','rows':rows,'cyclic_expand':False},open(directory/'H_DEFINITION.json','w'))
 json.dump(a,open(directory/'capsule_report.json','w'))
 json.dump({'rows':rows,'homogeneous_vertices':a['homogeneous_raw_vertices']},open(directory/'exact_intersections.json','w'))
 json.dump({'faces':a['faces']},open(directory/'geometry_raw.json','w'))
 return a
if __name__=='__main__':
 a=run_to(sys.argv[1]if len(sys.argv)>1 else 'REBUILT')
 print(json.dumps({'status':'EXACT_ONE_PAIR_NONWINNER_REBUILT','new_winner':False,'V':a['V'],'E':a['E'],'F':a['F'],'class':a['class_'],'degeneracies':a['degeneracies']}))
```

## 10. Observed independent acceptance and artifact integrity

The frozen proof archive was extracted into a new directory, and its own standard-library `REPLAY.py` was actually run there. It completed with

**`RA04_ASYMMETRIC_ONE_PAIR_FRESH_EXACT_REPLAY_PASS`**

and explicitly recorded **`new_winner:false`**.

The cold reconstruction examined302621 plane triples and performed1618219 construction support comparisons. The primary full boundary audit performed29766 maximal-plane/all-point comparisons and3832 polygon halfplane comparisons. It checked complete contacts, every vertex link, oriented closed connected topology, all rank-three support cones, and every true-feature equilibrium predicate.

The independent implementation imports neither the builder nor the primary geometry checker. It separately validates supports, contacts, polygons, links and extremality; integrates boundary-apex tetrahedra; tests58322 ordered global vertex supports; and solves all363 two-normal Gram cones. Its volume, centroid and complete feature identities agree exactly with the primary calculation.

The fresh replay also verified the exact normalized margins and source-escape inequalities; tested translation by `(1,-2,3)/10^6`; rejected reversed-face, open-boundary and corrupted-vertex fixtures; and calibrated a regular tetrahedron as(4,4,6). All21 manifest payloads matched before and after replay.

OBJ and ASCII STL readback matched all242 vertices,123 maximal polygons and480 triangles with exact rational coordinate error below10^-49. These files are explicitly **display approximations of the raw rational body**, not alternative exact definitions. No mechanical claim is made for a separately reinterpreted rounded mesh.

### Delivered files

[Complete exact one-pair construction and two-program proof replay](sandbox:/mnt/data/RA04_ASYMMETRIC_ONE_PAIR.zip)

```text
440902 bytes
SHA-256 0a21433c9025b2135c952cbe1d6f194aaa694018b6278ea288a6e0a0f4a26fb0
```

[Complete retained discovery programs, inputs, checkpoints and bounded failed branches](sandbox:/mnt/data/RA04_ASYMMETRIC_DISCOVERY.zip)

```text
3919838 bytes
SHA-256 614c6a29b6c48be5b98c03fb191253c32571ef98bad98af943f192fffc7e2740
```

[Actual fresh-extracted archive replay report](sandbox:/mnt/data/RA04_ASYMMETRIC_ONE_PAIR_ARCHIVE_REPLAY.json)

```text
2378 bytes
SHA-256 c19da11195dff2420d5cc41aefc3b1a9a170bd580fdac92a1b94d7914a18e651
```

[Delivery manifest](sandbox:/mnt/data/RA04_ASYMMETRIC_DELIVERY.json)

The archived `EXACT_BODY.py` has SHA-256 `1c05d79c51fce9d01acceb37be7f5375ff67fbfc0816e58d136990cd75ff6f1d`; it carries the same complete H payload and reconstruction, with an additional introductory comment/docstring. The invariant defining checksum is the decoded H-table SHA given above.

**Final disposition:** a new independently exact, homogeneous, asymmetric242/363/123 class(1,2,1) successor below the requested edge budget; an explicit geometric departure from the parent’s one-wave cut restrictions; and a fully specified connected region for the remaining cancellation. The strict110 target, a successful inward-only staged-cut construction, minimality, external peer review and manufacturing tolerance remain unclaimed.
