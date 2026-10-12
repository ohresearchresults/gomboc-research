# figure-0317

AI research report · 2026-09-05 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Calm Nova 11 — exact P50 compression to 2,033 vertices

## Determination

**The new rational body `CN11-P50-R2033-Q10` is a homogeneous convex polyhedron, exactly centred at its ordinary-volume centroid, with strict equilibrium class (S,U,H)=(1,1,0).** Its actual face lattice is

```
V=2033, E=6090, F=4059, C=2E=12180.
```

This reduces the assigned P50-4355 parent's C=26112 by **53.3547794117647%**, a factor of **2.1438423645320195**. There is one stable hexagon, one unstable vertex of true degree14, no saddle and no degenerate equilibrium. **C<1000 was not achieved.** No minimum, global impossibility, manufacturing tolerance, external human peer review or proof-assistant formalization is claimed.

The substantive algorithmic advance is **full three-coordinate, ordinary-moment-aware global margin relaxation followed by renewed contractions and cavity deletions**. This passed a plateau that pure deletion, asymmetric contractions, projective recentering and three-vertex cavities did not pass.

The complete absolute coordinates, complete triangulation, deterministic reconstruction and a new exact global verifier are supplied below. **The final reconstruction and certificate require only the Python standard library: no parent archive, optimizer, Qhull, NumPy or SciPy is needed.**

## 1. Source authority and distinctions

The geometric parent is literal result `figure-0311`, SHA256 `2e32e75e0d7968fe4238ef9c894ddf1cb491de3e42947626a34f91a761492173`. Its Library archive `POLYNOMIAL_SOURCE_GOMBOC_HANDOFF.zip`, file_id `file_00000000bde88210bfc6469cb5b03cdd`, was recovered and checked: 1,613,638bytes, SHA256 `5d4e3a2b942e9c906f0bbc50df4e87aad4248ec998f3d54a26925a823a697a8e`. The actual parent I/B/F hashes matched the literal payload. No source/alias conflict was found.

The methods parent is `figure-0309`, SHA256 `d08513544ea0708366548c84468693278e5977d95b3f9fd4d204abedba112f0c`. Its R31291 archive SHA256 is `320aca1675371c2cbc607d3412017f1340be9bda9459ccf2c6f88950cfcb73aa`. **R31291 supplied algorithms and verification implementations, not this run's starting geometry.** The old134131-row body and false J56 were not used as geometric restarts.

An earlier high-precision rational `CN11_P50_R2033` was separately accepted. The final **Q10** figure is a different, newly quantized and newly recentered exact body with the same counts. Its standalone ordering is a deliberate permutation into adjacent C2 pairs. The appendix defines only this final primary body.

The parent's denominator, root and physical bump are not the final definition. In particular, the parent apex degree12 has become **14**, and the cap/apex coordinates have changed.

## 2. Exact definition and actual ordinary-volume centroid

Decode the appendix into integer rows J_i and oriented triangles. Set

```
D0=10000000000.
```

The codec explicitly creates1016 pairs `(x,y,z),(x,-y,-z)`, followed by the axial apex. This is a property of the **new** ordering, not an assumption about the parent's arbitrary IDs. Raw little-endian signed-int64 hashes are

```
J: 100d30a5a8acabb494cb3aed8310bb2db9564fac075b111d751c310ef83f0f9b
F: 4a2b225ceb04f5e9d85228add63cf88195b67b23e5f38657751f51c31d72a3c8.
```

Calculate entirely in integers

```
W=sum_f det(J_a,J_b,J_c)
M=sum_f det(J_a,J_b,J_c)*(J_a+J_b+J_c).
```

Executed values:

```
W=24532589646322078519397059746174
M=(-964963956628164293346296189650,0,0).
```

The accepted body is exactly

```
P=conv{(4W J_i-M)/(4D0 W)}.
```

This subtracts the **actual ordinary-volume centroid**, rather than retaining a reference centre or old root. The raw centroid is `(g,0,0)`, where

```
g=-19299279132563285866925923793
  /19626071717057662815517647796939200000000
 ≈-9.83349057865189e-13.
```

The exported common denominator after gcd reduction is

```
H=490651792926441570387941194923480000000000.
```

The exact volume is

```
4088764941053679753232843291029 / 10^30
≈4.08876494105368.
```

All three centred first-moment numerators are **literally zero** upon independent reintegration. The standalone code also checks preservation of volume and the exact relation between every raw and centred coordinate. **No isolated algebraic root is needed in the final definition.**

### Unique equilibria and maximal faces

The stable hexagon's outward cycle is **[0,5,3,1,4,2]**. Raw rows J_0 through J_5 are

```
(-9462884856,-893532316,0)
(-9462884856, 893532316,0)
(-9462884856,-869677648,-1506325872)
(-9462884856, 869677648, 1506325872)
(-9462884856,0,-1896118514)
(-9462884856,0, 1896118514).
```

Divide by D0 and subtract `(g,0,0)`. The stable plane is

```
x=-9462884856/10^10-g
 =-464298142084804703860976595699321148987063/H.
```

The unique unstable vertex is **2032**, raw row `(10537115144,0,0)`, exact coordinate

```
(517005443768078436914905794147638851012937/H,0,0).
```

Its true degree is14. There are **4058 triangular maximal faces and one hexagon**. The triangulation has4062 triangles and6093 edges. Exactly three coplanar cap diagonals are removed, leaving **6090 true edges**. The actual Euler relation is `2033-6090+4059=2`.

## 3. Executed complete certificates

The final exported rational table passed **three implementations**:

* The inherited first rational verifier returned `INDEPENDENT_EXACT_AUDIT_PASS`.
* The distinct inherited standard-library verifier returned `VERIFIED_GOMBOC`, with **62954 exact predicates** and all2033 radial vertex-link windings one.
* The newly written standalone implementation returned `SELF_CONTAINED_EXACT_GLOBAL_PASS`, including **8251947 exact maximal-facet/all-point support tests**.

The first uses ray `(5,7,19)`; the others use `(3,11,17)`. Each finds radial degree1. The latter ray hits exactly canonical triangle2015, without a boundary hit.

The standalone implementation checks a connected closed oriented triangular two-manifold, a single-cycle link at every vertex, Euler2, positive radial determinants, convex hinges and exact coplanar components. Each maximal face has a single strictly convex polygonal boundary, its exact supporting-plane equality set, and a complete area-matching triangulation. **Every supplied point is tested against every maximal supporting plane in integers.** Each vertex has three independent incident support normals.

Thus every listed polygon is a complete actual exposed facet of the convex hull. Both incident facets are included at every listed facet edge; connected convex-hull facet adjacency leaves no omitted facet. Rank-three intersections prove all supplied points extreme. This establishes the global convex boundary, not merely local hinge convexity. The independent degree-one radial checks provide additional assurance.

For a true edge i→j in facet f and j→i in facet g, define

```
a=v_i·(v_j-v_i)
b=v_j·(v_i-v_j)
u=N_f·(v_i×v_j)
v=N_g·(v_j×v_i).
```

A strict saddle requires **a<0,b<0,u>0,v>0**. Both line-foot tests and both incident-normal cone tests are evaluated, as are all face projection-side and complete vertex-neighbour tests. The second verifier records **3326 interior line feet excluded by the full normal cone**. Absence of saddles is not inferred from Euler's equilibrium identity.

The result is `(1,1,0)`, **zero degenerate equilibria**, and **zero zero-valued individual true-edge primitives**. Incidence zeros on the three cap diagonals are not mechanical degeneracies.

The inherited rational verifier files were unchanged in this final replay:

```
first SHA256:
6286a97084e5b8e9e0ed4485957b3c013c6083e2bc96ebf44eef5d631017c30f
second SHA256:
c3ebc9db1491c74fc689f8dd021722985a389a9f8dbdc076dcf5711054bd5abe.
```

These are separately written algorithms within this research workflow, not outside human peer review.

An additional exact integer bound certifies the family

```
diag(1,1+s,1+t)P, |s|,|t|<=2^-32.
```

All **24360=4E** true-edge primitive signs persist. For each primitive P, express it as three coordinate-product terms with absolute sum G; the script verifies `((1+rho)^4-1)G<|P|`. Invertibility preserves the complete lattice and exact centroid. This is a two-parameter mechanical chamber, **not** arbitrary-coordinate or manufacturing tolerance.

Executed fixtures classify the regular tetrahedron `(4,4,6)` and reject wrong equilibrium claims, open/reversed meshes, nonzero centroid, duplicate vertices, incorrect scale and nonconstant data in the rational interface where applicable. OBJ/STL decimal and incidence readback passes; rounded mechanics are not certified.

Fresh standalone reconstructions, followed by the second verifier, reproduced these exact core bytes:

```
vertices.csv.gz:
1dfac3504729d1cd372a085f8a1206a7ce664c1c5d71ba6babbe18d6b05ea84a
triangles.csv.gz:
c305fd9a43173c07d4aba4b04fb4f872b51ade7ce645329f0799b53fa0d3050c
definition.json:
015992eb05cc4ae8a0522d5dae4e588d81ac52e5ac642ec18139b7ed7ae3cedc.
```

## 4. Construction search and the successful new mechanism

The first phase applied weighted rational edge contractions, C2-paired deletions, adjacent-pair cavities, radial replacements and nonlinear replacement-point optimization to **P50**. Actual hulls and moments were rebuilt. Numerical checkpoints decreased through3761,3477,3203 and3099; separately certified historical checkpoints are retained in the package.

The3099 state had numerical escape margin about7.80e-10. I then optimized **C2-paired XYZ velocities and a common minimum linearized physical exclusion margin**. The inequalities used a strongest outgoing escape per nonapex vertex, one excluding side per nonstable face, all apex-neighbour instability conditions, and linearized hinge convexity. One full ordinary x-moment derivative equation was imposed; C2 kills the other moments. Cap/apex velocities were fixed during a relaxation step, while all other coordinates could leave the source surface.

After each trial, coordinates were quantized, the global hull rebuilt, the actual volume centroid recomputed and subtracted, and the full numerical feature audit run. A line search rejected failed trials. This is discovery, not an exact chamber assertion.

For continuation, useful exact derivatives are: with `d=det(a,b,c)` and `s_x=a_x+b_x+c_x`,

```
grad_a(d*s_x)=s_x*(b×c)+d*e_x.
```

For `P=N·(a×b)`, `N=(b-a)×(c-a)`, `Q=a×b`,

```
grad_a P=(b-c)×Q+b×N
grad_b P=(c-a)×Q-a×N
grad_c P=(a-b)×Q.
```

The vertex primitive `a·(b-a)` has gradients `b-2a,a`. Normalizing factors are frozen within a linearization and remeasured after each trial. Rescaling small hinge rows improved LP conditioning; the actual hull remained authoritative.

At unchanged V3099, eight accepted steps raised the numerical minimum vertex exclusion to **0.00117039** and false-face exclusion to **0.00104001**. Six relaxation/compression epochs then gave

```
3099 -> 2867 -> 2517 -> 2369 -> 2257 -> 2213 -> 2153.
```

A separate free-coordinate contraction pass from the margin-improved **2213** state beat the basic2153 branch: **90 paired contractions in2879 attempts**, producing2033 vertices. Actual global hull and ordinary centroid were checked before committed proposals. The high-precision figure was exactly promoted, followed by a distinct coarse-grid rationalization and exact recentering to the primary Q10 body.

In late discovery states B_i=D represented a common x-translation to the actual centroid, making closure linear and rational. This is not P50's inherited physical bump. Genuine geometry changes came from XYZ relaxation and replacement vertices. The old root and smooth actuator interval are not assigned to the altered finite figures.

## 5. Failed approaches and scoped limitations

At the3099 stage, an asymmetric deletion/contraction sweep tried64792 candidates and accepted none; its projectively recentered counterpart also accepted none in64792 trials. A connected triple-cavity sweep accepted none in29376 trials. Stable-face births and lost vertex escapes dominated. These finite searches do **not** establish a complexity floor: subsequent XYZ relaxation passed their plateau.

An exact local counterexample explains why first-order actuator budgets were unsafe. This concerns one origin-relative vertex primitive, not a claimed own-centred full-body class. Set D=10^14 and

```
Iu=(-75240026724785,-6832290540248,70940351045639), Bu=-8911998351
Iv=(-75769950338187,-5387603371731,70517447242757), Bv=-8849229939
u(s)=(Iu-s*Bu*e_x)/D, v(s)=(Iv-s*Bv*e_x)/D.
```

Then `D²u(s)·(v(s)-u(s))=P0+sP1+s²P2`, with

```
P0=124399949002864756
P1=18627557729991318
P2=-559391984238888612.
```

Exactly `20|P1|<3P0`, yet

```
16P(1/4)=1505517430726912756>0
4P(1/2)=-24537072767446952<0.
```

A first-order budget below15% therefore misses a witness death. A sufficient safe bound must include the quadratic term, such as `kappa|P1|+kappa²|P2|<|P0|`. Failure of that sufficient bracket is not a global actuator-family exclusion.

Coarsening the high-precision endpoint beyond the accepted10^-10 raw grid, always recomputing the actual centroid, gave numerical classes `(33,25,56)` at10^-9, `(69,49,116)` at10^-8 and `(79,61,138)` at10^-7. These are **different nonwinning bodies**. The10^-10 body is accepted only through complete exact replay.

The final exact directed true-edge graph has shortest cap-to-apex escape length215 at all six cap vertices and maximum shortest length297. These are graph diagnostics, not lower bounds after new edges or geometry changes. The old R31291 roundness obstruction is not transferred to this shape.

With one hexagon and triangular remaining faces, E=3V-9; C<1000 requires V<=169. No global obstruction explaining2033 was proved, nor is2033 asserted a local minimum.

## 6. Resumable state and delivery

The most useful continuation is another whole-body XYZ margin-improvement phase followed by communicating multi-vertex replacement, without preserving the inherited escape tree. Critical-collar turnover and genuinely nonsimplicial side faces remain possible but unproved here. Every promoted successor needs its own full exact certificate.

The package's `final_native.npz` stores **D0=10^10 and the new paired ordering**. Do not feed it unchanged into scripts assuming D10^14 or apex4354. The included and exercised `prepare_restart.py` rescales integers exactly by10000, builds the new parent/mate interface and changes apex constants to2032. Historical original-ID correspondence is supplementary; no old-ID mask is needed to reconstruct the final figure.

[Complete exact package, discovery sources, checkpoints and replay implementations](sandbox:/mnt/data/CN11_P50_R2033_Q10_FULL_HANDOFF.zip): **16030146bytes**, SHA256 **f59cb69bbc3206abf39493dbdf1fc43a90ed9056cab3ad837be58b6bd18ead31**. All425 manifest entries were checked against the ZIP bytes. A fresh extraction regenerated the entire body from the codec, passed the standalone all-pairs audit and the second verifier, and reproduced identical core inputs.

[Fresh exact replay](sandbox:/mnt/data/CN11_ARCHIVE_EXACT_REPLAY.json), [fresh second-implementation replay](sandbox:/mnt/data/CN11_ARCHIVE_SECOND_REPLAY.json), and [complete handoff file](sandbox:/mnt/data/CN11_P50_R2033_Q10_HANDOFF.md).

Save the following two complete blocks as `self_contained.py` and `standalone_recipe.json`; run

```
python -S self_contained.py standalone_recipe.json replay
```

Expected: `SELF_CONTAINED_EXACT_GLOBAL_PASS`, C12180, class[1,1,0]. Do not use Python `-O`, because the verification gates are assertions. The complete blocks are sufficient without any downloaded source table.

## Appendix A — complete reconstruction and global verifier

```python
#!/usr/bin/env python3
"""Complete integer reconstruction and exact global certificate; Python standard library.
Usage: python -S self_contained.py recipe.json OUTPUT_DIRECTORY
"""
import base64,zlib,json,struct,hashlib,gzip,csv,io,math,sys
from pathlib import Path
from collections import defaultdict,Counter,deque
from fractions import Fraction

def sha(b):return hashlib.sha256(b).hexdigest()
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def det(a,b,c):return dot(a,cross(b,c))
def packed(rows):return b''.join(struct.pack('<'+'q'*len(r),*r) for r in rows)
def connected(adj,start):
 seen={start};todo=[start]
 for v in todo:
  for w in adj[v]:
   if w not in seen:seen.add(w);todo.append(w)
 return seen
class Reader:
 def __init__(self,s,h):self.b=zlib.decompress(base64.b85decode(''.join(s.split())));assert sha(self.b)==h;self.p=0
 def u(self):
  n=shift=0
  while True:
   b=self.b[self.p];self.p+=1;n|=(b&127)<<shift
   if b<128:return n
   shift+=7
 def s(self):
  n=self.u();return n//2 if n%2==0 else -(n+1)//2
 def end(self):assert self.p==len(self.b)
def writecsv(path,header,rows):
 with path.open('wb') as raw:
  with gzip.GzipFile(fileobj=raw,mode='wb',filename='',mtime=0) as g:
   with io.TextIOWrapper(g,encoding='ascii',newline='') as t:
    w=csv.writer(t,lineterminator='\n');w.writerow(header);w.writerows(rows)
def certify(J,F,D,R,H,expected=(1,1,0)):
 V=len(J);T=len(F);assert len(set(J))==V and len(set(map(lambda f:tuple(sorted(f)),F)))==T
 assert all(len(set(f))==3 and min(f)>=0 and max(f)<V for f in F)
 edges=defaultdict(list);links=[defaultdict(set) for _ in J];adj=[set() for _ in F]
 N=[];W=0;M=[0,0,0];CW=0;CM=[0,0,0]
 for fi,(a,b,c) in enumerate(F):
  n=cross(sub(J[b],J[a]),sub(J[c],J[a]));assert dot(n,J[a])>0;N.append(n)
  for i,j,k in [(a,b,c),(b,c,a),(c,a,b)]:
   edges[tuple(sorted((i,j)))].append((fi,i,j));links[i][j].add(k);links[i][k].add(j)
  d=det(J[a],J[b],J[c]);e=det(R[a],R[b],R[c]);assert d>0 and e>0;W+=d;CW+=e
  for k in range(3):M[k]+=d*(J[a][k]+J[b][k]+J[c][k]);CM[k]+=e*(R[a][k]+R[b][k]+R[c][k])
 assert CM==[0,0,0] and CW*D**3==W*H**3
 assert all(4*W*(H*J[i][k]-D*R[i][k])==H*M[k] for i in range(V) for k in range(3))
 parent=list(range(T))
 def root(i):
  while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
  return i
 flat=0
 for key,entries in edges.items():
  assert len(entries)==2
  (f,i,j),(g,jj,ii)=entries;assert i==ii and j==jj;adj[f].add(g);adj[g].add(f)
  k=next(v for v in F[g] if v not in key);d=dot(N[f],sub(J[k],J[i]));assert d<=0
  if d==0:assert dot(N[f],N[g])>0;parent[root(g)]=root(f);flat+=1
 assert V-len(edges)+T==2 and len(connected(adj,0))==T
 for link in links:
  assert link and all(len(s)==2 for s in link.values());assert len(connected(link,next(iter(link))))==len(link)
 groups=defaultdict(list)
 for f in range(T):groups[root(f)].append(f)
 groups=sorted(groups.values(),key=min);owner={f:g for g,fs in enumerate(groups) for f in fs};cycles=[];inc=[[] for _ in J]
 # Every maximal face is independently proved an actual exposed hull facet.
 for g,fs in enumerate(groups):
  fi=fs[0];n=N[fi];anchor=J[F[fi][0]];boundary=[]
  for f in fs:
   a,b,c=F[f]
   for i,j in [(a,b),(b,c),(c,a)]:
    other=next(q[0] for q in edges[tuple(sorted((i,j)))] if q[0]!=f)
    if owner[other]!=g:boundary.append((i,j))
  nxt=dict(boundary);assert len(nxt)==len(boundary);v=min(nxt);cycle=[]
  while v not in cycle:cycle.append(v);v=nxt[v]
  assert v==cycle[0] and len(cycle)==len(boundary) and len(fs)==len(cycle)-2
  eq=set()
  for i,p in enumerate(J):
   d=dot(n,sub(p,anchor));assert d<=0
   if d==0:eq.add(i)
  assert eq==set(cycle)==set(v for f in fs for v in F[f])
  for i,j in boundary:
   assert all(dot(n,cross(sub(J[j],J[i]),sub(J[k],J[i])))>0 for k in cycle if k not in (i,j))
  area=[sum(N[f][k] for f in fs) for k in range(3)]
  assert area==[sum(cross(J[i],J[j])[k] for i,j in boundary) for k in range(3)]
  for i in cycle:inc[i].append(n)
  cycles.append(cycle)
 for ns in inc:
  a=ns[0];b=next(n for n in ns if cross(a,n)!=(0,0,0));assert any(det(a,b,n)!=0 for n in ns)
 # Degree-one generic ray is checked in addition to all-pairs support.
 hits=[];ray=(3,11,17)
 for fi,(a,b,c) in enumerate(F):
  ss=[det(ray,R[b],R[c]),det(R[a],ray,R[c]),det(R[a],R[b],ray)]
  assert not(min(ss)==0 and max(ss)>0)
  if min(ss)>0:hits.append(fi)
 assert len(hits)==1
 vertex=[None]*V;side=[[] for _ in groups];true=[];saddles=[];degenerate=[];zeros=0
 for key,((f,i,j),(g,_,_)) in sorted(edges.items()):
  if owner[f]==owner[g]:continue
  true.append((i,j,owner[f],owner[g]));d=sub(R[j],R[i]);c=cross(R[i],R[j])
  a=dot(R[i],d);b=-dot(R[j],d);u=dot(N[f],c);v=-dot(N[g],c)
  zeros+=sum(x==0 for x in (a,b,u,v));vertex[i]=a if vertex[i] is None else max(vertex[i],a);vertex[j]=b if vertex[j] is None else max(vertex[j],b)
  side[owner[f]].append(u);side[owner[g]].append(v);pr=[-a,-b,u,v]
  if min(pr)>0:saddles.append(key)
  elif min(pr)==0:degenerate.append(['edge',key])
 stable=[g for g,s in enumerate(side) if min(s)>0];unstable=[i for i,p in enumerate(vertex) if p<0]
 degenerate += [['face',g] for g,s in enumerate(side) if min(s)==0]+[['vertex',i] for i,p in enumerate(vertex) if p==0]
 assert not degenerate and (len(stable),len(unstable),len(saddles))==expected
 report={'status':'SELF_CONTAINED_EXACT_GLOBAL_PASS','V':V,'E':len(true),'F':len(groups),'C':2*len(true),'class':list(expected),'triangles':T,'coplanar_diagonals':flat,'face_sizes':dict(Counter(map(len,cycles))),'stable_cycle':cycles[stable[0]],'unstable_vertex':unstable[0],'unstable_degree':sum(unstable[0] in e[:2] for e in true),'degenerate_equilibria':degenerate,'zero_true_edge_primitives':zeros,'centred_first_moment_numerators':CM,'all_pair_support_tests':V*len(groups),'ray':[3,11,17],'ray_triangle':hits[0],'all_vertices_extreme':True,'all_vertex_links_single_cycles':True}
 return report,cycles,true,W,M

def main(path,outdir):
 rec=json.loads(Path(path).read_text());D=rec['D'];reader=Reader(rec['points_b85'],rec['points_stream_sha256']);J=[]
 for _ in range(rec['pairs']):
  x,y,z=reader.s(),reader.s(),reader.s();assert y or z;J.extend([(x,y,z),(x,-y,-z)])
 J.append((reader.s(),0,0));reader.end();assert len(J)==rec['V'] and sha(packed(J))==rec['points_matrix_sha256']
 reader=Reader(rec['triangles_b85'],rec['triangles_stream_sha256']);F=[];a=0
 for _ in range(rec['triangles']):a+=reader.u();F.append((a,a+reader.u(),a+reader.u()))
 reader.end();assert sha(packed(F))==rec['triangles_matrix_sha256']
 W=0;M=[0,0,0]
 for a,b,c in F:
  d=det(J[a],J[b],J[c]);assert d>0;W+=d
  for k in range(3):M[k]+=d*(J[a][k]+J[b][k]+J[c][k])
 assert W>0 and M[1:]==[0,0]
 H=4*D*W;R=[tuple(4*W*x-M[k] for k,x in enumerate(v)) for v in J];g=H
 for row in R:
  for x in row:g=math.gcd(g,x)
 H//=g;R=[tuple(x//g for x in row) for row in R]
 report,cycles,edges,W,M=certify(J,F,D,R,H)
 out=Path(outdir);out.mkdir(parents=True,exist_ok=True)
 writecsv(out/'vertices.csv.gz',['ix','iy','iz','b'],[(*v,0) for v in R]);writecsv(out/'triangles.csv.gz',['i','j','k'],F)
 writecsv(out/'raw_vertices.csv.gz',['ix','iy','iz'],J);writecsv(out/'true_edges.csv.gz',['i','j','face_i','face_j'],edges)
 (out/'definition.json').write_text(json.dumps({'version':1,'coordinate_type':'rational','D':str(H),'generic_ray':[3,11,17]},indent=2)+'\n')
 with gzip.open(out/'maximal_faces.json.gz','wt') as f:json.dump(cycles,f,separators=(',',':'))
 centre=[Fraction(x,4*D*W) for x in M];vol=Fraction(W,6*D**3)
 report.update(D0=D,W=str(W),M=list(map(str,M)),H=str(H),centroid_subtracted=[[str(x.numerator),str(x.denominator)] for x in centre],volume=[str(vol.numerator),str(vol.denominator)])
 report['input_sha256']={n:sha((out/n).read_bytes()) for n in ['vertices.csv.gz','triangles.csv.gz','definition.json']}
 (out/'self-contained-report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main(*sys.argv[1:])
```

## Appendix B — complete absolute coordinates and triangles


[Encoded source block omitted; the code in this passage is incomplete.]


**Final result: an exactly homogeneous own-centred strict (1,1,0) convex polyhedron with (V,E,F)=(2033,6090,4059) and C12180. The C<1000 objective remains open.**
