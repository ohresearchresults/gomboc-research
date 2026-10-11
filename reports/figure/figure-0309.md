# figure-0309

Historical AI scientific report · saved 2026-09-05 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: unreviewed-encoded-blocks-omitted.

---

# Calm Nova 11 — certified rational compression of the actual 134131-vertex winner

## Result

**A new, fully materialized rational homogeneous convex polyhedron, R31291, passes two distinct exact verification implementations at its own ordinary-volume centroid.**

| Quantity | Assigned parent | R31291 |
|---|---:|---:|
| Actual extreme vertices V | 134131 | **31291** |
| True edges E | 402134 | **93866** |
| Maximal faces F | 268005 | **62577** |
| Mechanical complexity C=2E | 804268 | **187732** |
| Strict equilibrium class (S,U,H) | (1,1,0) | **(1,1,0)** |
| Unique stable face | 256-gon | **Rhombus / quadrilateral** |
| Ordinary-volume centroid | (0,0,0) | **Exactly (0,0,0)** |

The complexity reduction is **76.65802941308121%**, a factor of **4.284128438412204**. The new stable face is a rhombus, **not an exact square**. The final body is entirely rational; it is not just a floating endpoint or an algebraic body whose old centre was inherited.

**C<1000 was not achieved.** This is a certified major reduction, not a minimality result. No global impossibility, physical manufacturing tolerance, worldwide priority, or independent human peer-review claim is made.

## Source authority

The source was the actual Library file `POLYHEDRAL_GOMBOC_VERIFICATION.zip`, file_id `file_000000007de881f4837ea5182ada2fb8`, identified in the final journal objective. The older false J56 construction was not used. :contentReference[oaicite:0]{index=0}

Verified parent archive SHA256:
`0848b0aef0cafd5a3ae6a69cbf387760fb1ae79e01b65720abdc65b54ffe365a`

Verified `exact_polyhedron.npz` member SHA256:
`ac1e9893101e1be6c1be5d63d95538dc96894dfa8827b7b7b245fef4caef484d`

I reran the supplied exact audit on the original parent successfully. The separate standard-library implementation was recovered from Library file_id `file_00000000fed08210a8d6d70ceae4f8f7`, `polyhedral_gomboc_crosscheck.zip`, archive SHA256 `e2405c9444aecbc7a906232e94d167fb2a236f6fd313724454e2ee14ffba26dd`. Its `verify_gomboc.py` SHA256 is `91628f5d51ef956ccf55f80eec765501184023a55842e0af14bcae137237ac78`. This is the distinct implementation described in the journal, not another invocation of the first verifier. :contentReference[oaicite:1]{index=1}

## Exact definition of R31291

The complete literal recipe and executable reconstruction below carry **all new retained-index and coordinate choices**. They require only the identified inherited archives, which are also included in the delivered package. No earlier worker filesystem or numerical search rerun is required.

Starting from the parent's integer I/B table, execute the recipe's 3305 retained reconstruction events: 2990 rational-weight integer contractions and 315 literal row assignments. Every update is mirrored under the original C2 involution `(Ix,Iy,Iz,B) -> (Ix,-Iy,-Iz,B)`. Apply the retained-vertex bitset, obtaining exactly 31291 rows. These replay events define coordinates; intermediate replay stages are not asserted to be certified polyhedra.

The common source denominator is `D=109951162777600`. The reconstructed matrix with columns `(original_index,Ix,Iy,Iz,B)`, little-endian signed int64, has SHA256:
`cb9489d4248d0b5e89c358823ca29ce6d6da8d85ea986735c1154053330069bc`.

Use the exact rational parameter

`p/q = -35038107872515753597625145227816659886702 / 10000000000000000000000000000000000000000`.

Set `h=Dq` and integer points `A_i=(q Ixi-p Bi,q Iyi,q Izi)`. For an outward triangulation of their convex boundary, calculate in integers

`W=sum det(A_a,A_b,A_c)`

and

`M=sum det(A_a,A_b,A_c)(A_a+A_b+A_c)`.

The accepted body is exactly

`R31291=conv{(4W A_i-M)/(4hW)}`.

This subtracts the **actual ordinary-volume centroid** `M/(4hW)`. Here W is positive and My=Mz=0 exactly. Both verifiers independently reintegrate the translated body and obtain all three first moments literally zero.

After common-gcd reduction, the published denominator is

`H=91711167635932936926505859632906794232681362926822634918947521545217144089640368004942618689536000000000000000000000000000000000000000000`.

The subtracted centroid is `(g,0,0)`, with `g=K/H>0` and

`K=105428058994616427802629067699058538194994838715329272602994685597227051243632138939292160633`.

Its small size is not used instead of exact recentering. The numerical volume locator is `4.183421821929319`; the integer determinant formula defines the exact volume.

In sorted retained-row numbering, the stable face has outward cycle `[0,2,3,1]`, equivalently `[1,0,2,3]`, and plane `x=-100327/102400-g`. Its vertices are

```
0=(-100327/102400-g,-2429356428441/D,0)
1=(-100327/102400-g,0,-2429420799580/D)
2=(-100327/102400-g,0, 2429420799580/D)
3=(-100327/102400-g, 2429356428441/D,0).
```

The sole unstable vertex is local index **31290**, original index **134130**, at `(104473/102400-g,0,0)`, with true degree **152**. All other 62576 maximal faces are triangles. There are 62578 display triangles, 93867 triangulated edges, and exactly **one coplanar display diagonal**, excluded from the true-edge count.

### Separately certified quadratic precursor

The same reconstructed I/B table was first centred by its newly computed polynomial `Q(t)=C+B t+A t^2`:

```
C=178439218127449737269808702738176719688237261635289918
B=50927186674722801276426580921790504443583615958483452
A=644132797864917146125837948994357645932842967.
```

The exact x-moment numerator over `24D^4` is `-4Q(t)`; both transverse moment polynomials vanish identically. The volume numerator over `6D^3` is

`33364330216453250491338563982141676743142896+511767734492391049395002520899353178 t`.

The root bracket has denominator `10^90`, lower numerator

`-3503810787251575359762514522781665988670117193094515570125725795544737985613839885743134384`,

and upper numerator one larger. The root is approximately `-3.503810787251575359762514522781665988670117193...`. This precursor passed an exact audit. The final rational body is a different, separately recentered and separately verified object, not an inherited verdict at a rounded root.

## Verification actually completed

The first implementation reports `INDEPENDENT_EXACT_AUDIT_PASS`. The second reports **`VERIFIED_GOMBOC`**, class `[1,1,0]`, with **969961 exact predicate calls**. A fresh extraction of the delivered archive was also run through the standard-library verifier and passed.

Both implementations check the complete closed oriented connected manifold, single-cycle vertex links, positive radial determinants, degree-one radial covering, convex hinges, exact coplanar merging, maximal-face boundary cycles, actual vertex extremality, exact volume and centroid, and every maximal-face, vertex and true-edge equilibrium predicate. The second additionally checks winding one at every vertex. The first uses generic ray `(5,7,19)`; the second uses `(3,11,17)` and finds unique ray triangle 33680 in the canonical reconstruction. Radial embedding is established before global convexity is deduced from the convex piecewise-linear gauge; local hinge signs are not alone being called a global proof.

For a true edge i→j in one facet and j→i in the other, with outward normals n0,n1, the four quantities are

`a=vi·(vj-vi)`, `b=vj·(vi-vj)`, `c=n0·(vi×vj)`, `d=n1·(vj×vi)`.

A strict saddle requires **a<0, b<0, c>0, d>0**. Both line-foot tests and both incident-normal tests are evaluated. Euler's identity is only a cross-check. There are **zero degenerate equilibria** and **zero zero-valued true-edge primitives**.

The rational adapters change the arithmetic and centroid input interface, not the geometry gates: every predicate must be a constant integer polynomial and the recomputed moment vectors must be zero. The first verifier's obsolete literal assertion of 253 parent flat diagonals is removed; the actual coplanar components are recomputed. The second has no such hard-coded count. No convexity, extremality, or full-cone condition was disabled.

Two fresh deterministic reconstructions produced byte-identical canonical inputs:

```
15738c66a990ed9bf7e8d20f08fd08e63702737d0517803c55a13c6cafd9735d vertices.csv.gz
a903a1065b3f0db16518fce2372572df3da3c260b0e2ae5685fcb35779461ee2 triangles.csv.gz
3199d0a710f81a0a1a0772b43c8edf56d52df446df2a2bab873e722a6c0cb710 definition.json.
```

A regular tetrahedron is classified `(4,4,6)`. Wrong winner claims, open meshes, reversed orientation, nonzero centroid, duplicate vertices, and nonconstant predicates in the rational interface are rejected.

### Exact nonzero mechanical family

An additional integer audit certifies `diag(1,1+s,1+t) R31291` for **|s|,|t|≤2^-31**. All **375464=4E** nonzero true-edge primitives keep their signs. Invertibility preserves the convex face lattice; the centroid remains zero. This is a diagonal-map parameter box, **not** arbitrary independent-vertex or manufacturing tolerance.

For reproduction, write a primitive as the sum P of three coordinate products and let G be the sum of their absolute values. The script verifies, in integers, `|P|>((1+rho)^4-1)G` with `rho=2^-31` for every primitive. Under the stated diagonal maps each coefficient changes by at most this multiplier.

OBJ and ASCII STL were exported and read back with matching decimal vertices and triangles, and two incidences per display edge. They are display approximations; their rounded mechanics and physical manufacture are not certified.

## Search performed; nonwinners kept separate

The successful route combined moment-aware C2-paired vertex deletion, stable-cap reduction, weighted edge contraction, small radial replacements, simultaneous adjacent-pair cavity deletion, single-vertex cleanup, and a broader rational-weight contraction pass. Actual hulls and ordinary moments were rebuilt, not inherited from the parent.

Useful checkpoints were 44555 vertices after balanced deletion; 44303 after replacing the stable cap; 36853 after initial contraction/radial passes and four-sided cap; 32305 after simultaneous pair deletion; 31959 after cleanup; and **31291** finally. Floating proposals were used for discovery; only explicitly replayed endpoints are promoted as exact.

An unconstrained reference-centre deletion reached 41293 vertices with reference-relative `(1,1,0)`. Closing its actual moment equation using the physical x-bump required approximately t=-10.84837 and produced numerical class **(153,409,560)**. It was rejected. This is a physically retuned nonwinner, not an accepted own-centred body.

Independent Fibonacci/support completion and ascent-path completion returned larger numerical one-equilibrium bodies around 65–67 thousand vertices. Radius-ordered and pure-deletion pair passes did not beat the retained branch.

Larger stable-cap reconstruction with numerically closed ordinary moments also failed: cap shift 0.0004 gave 31119 vertices but class **(93,5,96)**; shift 0.0128 gave 24803 vertices but class **(55,5,58)**. These are smaller **nonwinners**, not certified reductions. Widening the cap while repairing only mass creates a genuine transition-equilibrium belt.

## Quantitative obstruction — carefully scoped

A 256-sided maximal face alone forces E≥512 and C≥1024: its 256 boundary edges and at least one distinct off-face incident edge at every boundary vertex. Replacing that face was necessary for C<1000.

A stronger bound applies only to **C2 symmetry, the present final cap/apex geometry, and triangular remaining maximal faces**. It is not a global homogeneous-Gömböc bound and does not explain the whole 31291-vertex endpoint.

Every nonunstable vertex v has a true neighbour w with v·(w-v)>0, hence strictly increasing radius. Choose these arrows C2-equivariantly. With one unstable vertex they terminate at apex A. The chosen paths from a maximum-radius cap vertex and its mate cannot meet before A: their depths to A agree, and an earlier common vertex would be C2-fixed. A is the only axial extreme vertex.

For a path with m edges, endpoint radii r,R, total endpoint angle Theta and consecutive angles theta_j,

`log(R/r)>sum[-log(cos theta_j)]>=sum(theta_j^2)/2>=Theta^2/(2m)`.

For this cap/apex, exact rational bounds are

`r>49/50`, `R<104473/102400`, `Theta>311/100`, `log(R/r)<2013/50000`.

The angle bound follows from |x_cap|>39/40, transverse radius<1/40, pi>157/50, and atan u<u. For the logarithm put s=4121/100352 and use

`s-s^2/2+s^3/3=122015509504265/3031791644442624<2013/50000`.

Because `(311/100)^2>240*(2013/50000)`, **m≥121**. Positive exact centroid subtraction strengthens the bounds. The two paths are disjoint except at A and cannot visit another cap vertex after their maximum-radius starts. Thus, with a four-sided cap, **V≥4+2m-1≥245**. If all other maximal faces are triangular, E=3V-7, giving **E≥728 and C≥1456 in this stated family**.

This does not exclude C<1000 after breaking C2, changing extremal geometry, or introducing genuinely nonsimplicial side faces. The current exact directed true-edge graph has shortest cap-to-apex escape lengths **[298,1808,1808,298]**, and maximum shortest length 1951 over all vertices. These are graph diagnostics, not lower bounds after new edges or shape changes; preserving the current witness tree is unnecessarily restrictive.

For four-sided cap plus triangular other faces, C<1000 requires V≤168. Under the same C2 argument, m≤82 would require `log(R/r)>Theta^2/164`. Present radial headroom is about 0.04024 versus about 0.0593 required at this angular span. This gives the source-conditioning direction a concrete target without asserting a global complexity floor.

## Continuation and deliverables

The accepted restart is the rational table in `geometry/`; its exact I/B precursor and root are in `source/`. The complete recipe below regenerates the original-index I/B checkpoint. The most valuable new moves are asymmetric communicating witness paths, materially increased radial headroom, or genuinely nonsimplicial side bands. A mixed vertex/support-plane coarsener is another untested way to escape the purely inscribed-cavity bias. These are proposed continuations, not completed experiments.

Further local deletion may still reduce C=187732; no optimality claim is made. Every promoted successor needs its own exact centroid, globally certified actual boundary, maximal faces, true edges, and full normal-cone audit.

[Exact rational body, both verifiers, deterministic replay, source archives, true face/edge tables, proofs, search scripts and display meshes](sandbox:/mnt/data/R31291_exact_rational_gomboc.zip). The archive has **13031670 bytes**, SHA256 **320aca1675371c2cbc607d3412017f1340be9bda9459ccf2c6f88950cfcb73aa**. All 64 manifest entries were checked against actual ZIP bytes. [Fresh extracted-archive standard-library replay](sandbox:/mnt/data/R31291_fresh_archive_replay.json). [Complete handoff file](sandbox:/mnt/data/R31291_research_handoff.md).

## Complete deterministic reconstruction

Save the following two code blocks as `reconstruct.py` and `recipe.json`. Use the two identified inherited archives, or their copies in the package:

```
python reconstruct.py recipe.json POLYHEDRAL_GOMBOC_VERIFICATION.zip rebuilt polyhedral_gomboc_crosscheck.zip
python rebuilt/verify_rational_first.py
python -S rebuilt/verify_rational_second.py rebuilt
```

NumPy/SciPy are used for archive access and a boundary proposal. Coordinate replay, repairs and centroid integration are integer operations. Independent acceptance is run on the exported rational CSV. Both actual fresh reconstructions needed zero exact triangle flips. The convex hull of the reconstructed rational points, not a particular Qhull triangulation, defines the body.

### reconstruct.py

```python
#!/usr/bin/env python3
"""Exact deterministic successor replay.
python reconstruct.py recipe.json PARENT.zip OUTPUT [CROSSCHECK.zip]
Qhull proposes triangles; integer operations and full verifiers decide acceptance.
"""
import base64,csv,gzip,hashlib,io,json,math,sys,zipfile
from pathlib import Path
from collections import defaultdict,deque
from fractions import Fraction
import numpy as np
from scipy.spatial import ConvexHull

def sha(b):return hashlib.sha256(b).hexdigest()
def unblob(s):return __import__('zlib').decompress(base64.b85decode(''.join(s.split())))
def member(z,name):
 names=[n for n in z.namelist() if n.split('/')[-1]==name]
 assert len(names)==1,(name,names)
 return z.read(names[0])
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def det(a,b,c):return dot(a,cross(b,c))
def gzwrite(path,header,rows):
 with path.open('wb') as raw:
  with gzip.GzipFile(fileobj=raw,mode='wb',mtime=0,filename='') as stream:
   with io.TextIOWrapper(stream,encoding='ascii',newline='') as txt:
    wr=csv.writer(txt,lineterminator='\n');wr.writerow(header);wr.writerows(rows)

def exact_hull(N,H):
 approx=np.array([[x/H,y/H,z/H] for x,y,z in N]);h=ConvexHull(approx);assert len(h.vertices)==len(N)
 F=h.simplices.copy();q=approx[F];nn=np.cross(q[:,1]-q[:,0],q[:,2]-q[:,0]);bad=np.einsum('ij,ij->i',nn,h.equations[:,:3])<0;F[bad]=F[bad][:,[0,2,1]]
 F=[tuple(map(int,f)) for f in F];edge=defaultdict(set)
 for k,f in enumerate(F):
  for a,b in zip(f,f[1:]+f[:1]):edge[tuple(sorted((a,b)))].add(k)
 assert all(len(v)==2 for v in edge.values());todo=deque(edge);flips=0
 while todo:
  e=todo.popleft()
  if e not in edge:continue
  a,b=sorted(edge[e]);i,j=e
  if not any(F[a][r]==i and F[a][(r+1)%3]==j for r in range(3)):i,j=j,i
  k=next(v for v in F[a] if v not in e);l=next(v for v in F[b] if v not in e)
  if det(sub(N[j],N[i]),sub(N[k],N[i]),sub(N[l],N[i]))<=0:continue
  nt=[(k,i,l),(k,l,j)];assert all(det(*(N[v] for v in f))>0 for f in nt)
  assert tuple(sorted((k,l))) not in edge
  for fi in (a,b):
   f=F[fi]
   for u,v in zip(f,f[1:]+f[:1]):
    key=tuple(sorted((u,v)));edge[key].remove(fi)
    if not edge[key]:del edge[key]
  for fi,f in zip((a,b),nt):
   F[fi]=f
   for u,v in zip(f,f[1:]+f[:1]):key=tuple(sorted((u,v)));edge[key].add(fi);todo.append(key)
  flips+=1;assert flips<100000
 assert len(set(N[i][0] for i in range(4)))==1
 F=[f for f in F if not all(v<4 for v in f)]+[(0,2,3),(0,3,1)]
 assert all(det(*(N[v] for v in f))>0 for f in F)
 F=sorted(f[f.index(min(f)):]+f[:f.index(min(f))] for f in F)
 assert len(set(F))==len(F)==2*len(N)-4
 return F,flips

def reconstruct(recipe,parent,out):
 raw=Path(parent).read_bytes();assert sha(raw)==recipe['parent_zip_sha256'];z=zipfile.ZipFile(io.BytesIO(raw));data=member(z,'exact_polyhedron.npz');assert sha(data)==recipe['parent_npz_sha256'];src=np.load(io.BytesIO(data),allow_pickle=False)
 I=src['I'].copy();B=src['B'].copy();OI=I.copy();OB=B.copy();D=int(src['D']);assert D==recipe['D']
 lookup={(*map(int,r),int(B[k])):k for k,r in enumerate(I)};mate=np.array([lookup[(int(x),-int(y),-int(z),int(B[k]))] for k,(x,y,z) in enumerate(I)])
 mask=unblob(recipe['mask_b85']);events=unblob(recipe['events_b85']);assert sha(mask)==recipe['mask_raw_sha256'] and sha(events)==recipe['event_raw_sha256'];pos=0
 def vu():
  nonlocal pos
  v=0;s=0
  while True:
   c=events[pos];pos+=1;v|=(c&127)<<s
   if c<128:return v
   s+=7
 def vs():
  n=vu();return n//2 if n%2==0 else -(n//2)-1
 weights=[(1,2),(1,4),(3,4),(1,8),(7,8),(1,16),(15,16)]
 for _ in range(recipe['events']):
  kind=events[pos];pos+=1;u=vu()
  if kind==0:
   v=u+vs();n,d=weights[vu()];ni=(I[u]*(d-n)+I[v]*n)//d;nb=(int(B[u])*(d-n)+int(B[v])*n)//d
  else:
   assert kind==1;delta=[vs() for _ in range(4)];ni=OI[u]+delta[:3];nb=int(OB[u])+delta[3]
  I[u]=ni;B[u]=nb;I[mate[u]]=ni*np.array([1,-1,-1]);B[mate[u]]=nb
 assert pos==len(events)
 ids=np.flatnonzero(np.unpackbits(np.frombuffer(mask,dtype=np.uint8),bitorder='big')[:len(I)]);I=I[ids];B=B[ids]
 assert len(ids)==recipe['vertices']
 assert sha(np.c_[ids,I,B].astype('<i8').tobytes())==recipe['coordinate_matrix_sha256']
 p,q=map(int,recipe['rational_parameter']);H0=D*q
 N=[(int(x)*q-p*int(b),int(y)*q,int(zz)*q) for (x,y,zz),b in zip(I,B)]
 F,flips=exact_hull(N,H0);W=0;M=[0,0,0]
 for a,b,c in F:
  d=det(N[a],N[b],N[c]);W+=d
  for j in range(3):M[j]+=d*(N[a][j]+N[b][j]+N[c][j])
 assert W>0 and M[1:]==[0,0]
 H=4*W*H0;R=[tuple(4*W*v-M[j] for j,v in enumerate(n)) for n in N];g=H
 for row in R:
  for v in row:g=math.gcd(g,v)
 H//=g;R=[tuple(v//g for v in row) for row in R]
 out=Path(out);out.mkdir(parents=True,exist_ok=True)
 gzwrite(out/'vertices.csv.gz',['ix','iy','iz','b'],[(*r,0) for r in R]);gzwrite(out/'triangles.csv.gz',['i','j','k'],F)
 (out/'definition.json').write_text(json.dumps({'version':1,'coordinate_type':'rational','D':str(H),'generic_ray':[3,11,17]},indent=2)+'\n')
 np.savez_compressed(out/'source-coordinate-checkpoint.npz',ids=ids,I=I,B=B,F=np.array(F),t=np.longdouble(p)/q)
 centre=[Fraction(v,4*W*H0) for v in M]
 report={'status':'EXACT_RATIONAL_RECONSTRUCTION_REQUIRES_FULL_AUDIT','vertices':len(R),'triangles':len(F),'exact_flips':flips,'parameter':[str(p),str(q)],'centroid_subtracted':[[str(v.numerator),str(v.denominator)] for v in centre],'rational_denominator':str(H),'coordinate_matrix_sha256':recipe['coordinate_matrix_sha256']}
 (out/'reconstruction.json').write_text(json.dumps(report,indent=2)+'\n')
 return member(z,'verify.py').decode(),report

def adapt_verifiers(first_source, second_source, out):
    s = second_source
    backend = 'class Rational:\n    """No algebraic auxiliary root: every predicate must be constant."""\n    def __init__(self, definition):\n        need(definition.get(\'coordinate_type\') == \'rational\', \'rational_type\', definition)\n        self.calls = self.fallbacks = self.zeros = 0\n    def sign(self, p):\n        self.calls += 1\n        need(all(x == 0 for x in p[1:]), \'nonconstant_rational_predicate\', p)\n        s = sg(p[0] if p else 0)\n        self.zeros += (s == 0)\n        return s\n\n'
    s = s.replace('class Quadratic:', backend + 'class Quadratic:')
    s = s.replace('q = Quadratic(d)', 'q = Rational(d)')
    old = "    need(nx[2] != 0, 'x_moment_not_quadratic', nx)\n    content = gcd(gcd(abs(nx[0]),abs(nx[1])),abs(nx[2]))\n    primitive = [sg(nx[2])*v//content for v in nx]\n    need(primitive == [q.C,q.B,q.A], 'quadratic_not_actual_x_moment', primitive)\n"
    assert old in s
    s = s.replace(old, "    need(all(m == [0,0,0] for m in moments), 'rational_centroid_not_exactly_zero', moments)\n")
    s = s.replace("'quadratic_ascending':[q.C,q.B,q.A]", "'coordinate_type':'rational'")
    s = s.replace("'root_interval':[[q.lo.numerator,q.lo.denominator],[q.hi.numerator,q.hi.denominator]],", "'rational_denominator':str(D),")
    s = s.replace('Exact C2 quadratic-algebraic convex-polyhedron/Gomboc verifier.', 'Exact rational convex-polyhedron/Gomboc verifier (documented rational-input adapter).')
    (out / 'verify_rational_second.py').write_text(s)
    s = first_source
    a = s.index('work = np.load(')
    b = s.index('# Reintegrate oriented tetrahedra', a)
    load = "import gzip,csv\nwith (BASE/'definition.json').open() as stream:\n    definition=json.load(stream)\nassert definition['coordinate_type']=='rational'\nD=int(definition['D']); assert D>0\nwith gzip.open(BASE/'vertices.csv.gz','rt',newline='') as stream:\n    rows=csv.reader(stream); assert next(rows)==['ix','iy','iz','b']\n    data=[tuple(map(int,r)) for r in rows]\nassert all(r[3]==0 for r in data)\nI=np.array([r[:3] for r in data],dtype=object);B=np.zeros(len(I),dtype=object)\nwith gzip.open(BASE/'triangles.csv.gz','rt',newline='') as stream:\n    rows=csv.reader(stream);assert next(rows)==['i','j','k']\n    F=np.array([tuple(map(int,r)) for r in rows],dtype=np.int64)\nn_vertices=len(I);n_triangles=len(F)\nassert len(set(map(tuple,I)))==n_vertices\nassert all(len(set(map(int,tr)))==3 and min(tr)>=0 and max(tr)<n_vertices for tr in F)\nassert len(set(tuple(sorted(map(int,tr))) for tr in F))==n_triangles\n\ndef algebraic_sign(p0,p1=0,p2=0):\n    assert p1==p2==0\n    return (p0>0)-(p0<0)\n\n"
    s = s[:a] + load + s[b:]
    a = s.index('g = math.gcd(*map(abs, moment_x))')
    b = s.index('assert algebraic_sign(*volume) > 0', a)
    s = s[:a] + 'assert moment_x==[0,0,0] and moment_y==moment_z==[0,0]\n' + s[b:]
    s = s.replace('assert coplanar_count == 253', '# Maximal coplanarity is derived, not prescribed.')
    s = s.replace('"root_bracket_sign_change": True,', '"rational_coordinates": True,').replace('"root_is_simple_on_bracket": True,', '"centroid_exact": [0,0,0],')
    s = s.replace('"centroid_x_polynomial_rederived": True,', '"rational_moments_recomputed_exactly": True,')
    s = s.replace('("exact_polyhedron.npz", "root.json")', '("vertices.csv.gz", "triangles.csv.gz", "definition.json")')
    (out / 'verify_rational_first.py').write_text(s)

if __name__=='__main__':
 recipe=json.loads(Path(sys.argv[1]).read_text());first,report=reconstruct(recipe,sys.argv[2],sys.argv[3]);out=Path(sys.argv[3])
 if len(sys.argv)>4:
  raw=Path(sys.argv[4]).read_bytes();assert sha(raw)=='e2405c9444aecbc7a906232e94d167fb2a236f6fd313724454e2ee14ffba26dd'
  second=member(zipfile.ZipFile(io.BytesIO(raw)),'verify_gomboc.py').decode();assert sha(second.encode())=='91628f5d51ef956ccf55f80eec765501184023a55842e0af14bcae137237ac78'
  adapt_verifiers(first,second,out)
 print(json.dumps(report,indent=2))
```

### recipe.json — complete literal new data


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]


**Final determination:** R31291 is a certified exact rational own-centred strict (1,1,0) successor with **C=187732**. The practical C<1000 objective remains open; the exact scoped obstruction identifies restrictions that must change, not a global impossibility.
