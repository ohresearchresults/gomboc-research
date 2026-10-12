# figure-0399

AI research report · 2026-09-17 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Clear Atlas 95 — low-arithmetic whole-strand turnover and an exact core/slab barrier

Assignment: `figure-0399`.

## Outcome

**No new own110 construction is claimed.** I obtained a substantially smaller, simpler exact scaffold: **`integer126_g100`, V23/E63/F42, C126, own211/weak000, with centered arithmetic33/34bits**. A less flattened companion, **`integer174_g200`, V31/E87/F58, C174, own211/weak000,38/39bits**, is the better starting point for the requested final cancellation. Both have entirely new surviving vertex coordinates and supporting planes relative to their stated immediate geometric ancestors; these are not unchanged-coordinate deletion descendants.

The complete preserved capsule contains **35 new rational checkpoints**, including20 own211 checkpoints, a genuine central-core-cut own323 construction, and mechanically worse coarse-grid controls. Every one passed exact A/B hull, maximal incidence, ordinary filled centroid, strict/weak all-feature checks, independent exhaustive plane-triple reconstruction, and positive centered tetrahedral integration. Eight exact applications of the disk/slab obstruction below include a C126 exclusion allowing centroid displacement as large as1/4. This is a geometrically scoped exclusion, not a global one.

The accepted own110 endpoint remains C622.

## Source authority

The complete literal NC57 parent `figure-0398`, SHA-256 `b6c84be62ea56d1c11575d4d6309563f525d734f79b0ad2a299f0b7abd2ccdd3`, was read and decoded; all37 source hashes matched. Fresh exact reconstructions reproduced the assigned C372 report,14190bytes,SHA `639b7dd56caf48ee99f1175e20b1f305100dc0fb3f75440dd20aba8df57b4cb5`, and C378 report,18534bytes,SHA `fc46fb08252486d5c2474d70c6834b2f4849f8de25bcf18ccb059a7aa9ced661`. Their true incidences are64/186/124 and65/189/126. The incorrect floating185-edge C372 count was not used.

I independently catalogued/searched the read-only research library and read the relevant complete late journal entries through the DELETE4225 integration. The single/pair unchanged-coordinate census was not repeated. No unavailable historical projective checkpoint or older C384 alias was substituted for an input.

## Exact constructions retained

C means2E throughout, including nonwinners. Centered bit costs are the bit length of the minimal common denominator of actual-centroid-centered coordinates and the largest absolute integer numerator over it. All feature labels are each new REPORT's rows.

| Checkpoint | V/E/F; C | Strict S/U/H | Centered bits | Own feature labels |
|---|---|---|---|---|
|`integer126_g100`|23/63/42;126|2/1/1|33/34|S1,41; U12; H20–22|
|`integer174_g200`|31/87/58;174|2/1/1|38/39|S0,54; U21; H22–24|
|`C126_G1000`|23/63/42;126|2/1/1|46/48|S6,29; U12; H21–22|
|`C156_G1000`|28/78/52;156|2/1/1|45/46|S6,44; U18; H22–25|
|`C240_G1000`|42/120/80;240|2/1/1|47/48|S1,54; U35; H36–38|
|`C174Q_G1500`|31/87/58;174|2/1/1|50/51|S11,45; U21; H22–23|
|`CA95_CORE_CUT174_G6`|69/110/43;220|3/2/3|3848/3849|S0,18,19; U1,57; H11–16,46–55,47–49|

Every row has weak-only000. The full collection also retains `integer126_g30`: C126, own222,26/27bits. Its cheaper arithmetic is real, but it is not mono-unstable.

## A directly recoverable low-arithmetic body

`integer126_g100` is exactly the convex hull of these24 rows divided by100. Input21 is non-extreme; the other23 vertices are reconstructed rather than presumed.

```text
64 -64 107
74 -46 106
57 -106 83
26 -114 89
-4 -129 74
-48 -128 67
-82 -129 36
-116 -112 14
-141 -90 -20
-157 -59 -54
-165 -19 -80
-161 23 -104
-145 73 -124
-117 119 -136
-81 159 -138
-32 196 -131
19 221 -115
66 219 -90
132 121 24
70 -112 46
112 95 -21
85 -70 41
102 -79 51
112 -33 64
```

Its exact filled volume in this input frame is `4152473/1500000`; its actual centroid is

`(101311319/830494600,520540313/6643956800,-77026377/3321978400)`.

The minimal centered common denominator is `6643956800`,33bits, with largest centered integer numerator34bits. It has42 maximal triangular faces,63 true edges and42 positive centered tetrahedra with exactly zero first moments. The unique unstable vertex is report12, corresponding to input16. The archived REPORT uses a raw translation before canonical ordering, so its centroid field differs from the input-frame centroid above.

The complete standalone verifier below takes these literal coordinates, reconstructs the hull without numerical libraries, recomputes the ordinary filled centroid, evaluates strict and weak face/vertex/edge equilibria, and proves the disk/slab certificate. It does not rely on any sandbox or parent file. Save it as `CA95_MINIMAL.py` and execute `python -B -S CA95_MINIMAL.py`. Assertions must remain enabled. This code is a compact independent recovery/verification route for the principal C126 construction, not a byte-identical recreation of the archived canonical REPORT format.

```python
#!/usr/bin/env python3
from fractions import Fraction as Q
from itertools import combinations
from math import gcd,lcm
import json,hashlib
assert __debug__
ROWS='''64 -64 107
74 -46 106
57 -106 83
26 -114 89
-4 -129 74
-48 -128 67
-82 -129 36
-116 -112 14
-141 -90 -20
-157 -59 -54
-165 -19 -80
-161 23 -104
-145 73 -124
-117 119 -136
-81 159 -138
-32 196 -131
19 221 -115
66 219 -90
132 121 24
70 -112 46
112 95 -21
85 -70 41
102 -79 51
112 -33 64'''
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(t,a):return tuple(t*x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def primitive(v):
 d=lcm(*(x.denominator for x in v));w=[int(x*d)for x in v];g=0
 for x in w:g=gcd(g,abs(x))
 return tuple(x//g for x in w)
def polygon(ids,P,n):
 drop=max(range(3),key=lambda k:abs(n[k]));axes=[k for k in range(3)if k!=drop]
 ids=sorted(ids,key=lambda i:(P[i][axes[0]],P[i][axes[1]]))
 def orient(i,j,k):
  a,b,c=[(P[t][axes[0]],P[t][axes[1]])for t in(i,j,k)]
  return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
 lo=[];hi=[]
 for i in ids:
  while len(lo)>1 and orient(lo[-2],lo[-1],i)<=0:lo.pop()
  lo.append(i)
 for i in reversed(ids):
  while len(hi)>1 and orient(hi[-2],hi[-1],i)<=0:hi.pop()
  hi.append(i)
 out=lo[:-1]+hi[:-1];assert len(out)>=3
 if dot(cross(sub(P[out[1]],P[out[0]]),sub(P[out[2]],P[out[0]])),n)<0:out.reverse()
 return out
def rational(x):return str(x.numerator)+'/'+str(x.denominator)
P=[tuple(Q(int(x),100)for x in s.split())for s in ROWS.splitlines()]
planes={}
for i,j,k in combinations(range(len(P)),3):
 n=cross(sub(P[j],P[i]),sub(P[k],P[i]))
 if n==(0,0,0):continue
 h=dot(n,P[i]);sg=[dot(n,x)-h for x in P]
 if max(sg)<=0:pass
 elif min(sg)>=0:n=mul(-1,n);h=-h
 else:continue
 key=primitive((*n,h));planes[key]=[r for r,x in enumerate(P)if dot(key[:3],x)==key[3]]
faces=[]
for pl,ids in sorted(planes.items()):faces.append((pl,polygon(ids,P,pl[:3])))
V=sorted({i for _,f in faces for i in f});edges={}
for fi,(_,f)in enumerate(faces):
 for i,j in zip(f,f[1:]+f[:1]):edges.setdefault(tuple(sorted((i,j))),[]).append(fi)
assert len(V)==23 and len(edges)==63 and len(faces)==42
assert set(range(24))-set(V)=={21}
assert all(len(v)==2 for v in edges.values())
assert len(V)-len(edges)+len(faces)==2
# Independent positive interior-anchor integration of the complete boundary.
o=tuple(sum(P[i][k]for i in V)/len(V)for k in range(3))
vol=Q(0);mom=[Q(0)]*3
for pl,f in faces:
 assert dot(pl[:3],o)<pl[3]
 for j in range(1,len(f)-1):
  a,b,c=[P[t]for t in(f[0],f[j],f[j+1])]
  dv=det(sub(a,o),sub(b,o),sub(c,o))/6;assert dv>0
  vol+=dv
  for k in range(3):mom[k]+=dv*(o[k]+a[k]+b[k]+c[k])/4
g=tuple(x/vol for x in mom)
assert vol==Q(4152473,1500000)
assert g==(Q(101311319,830494600),Q(520540313,6643956800),-Q(77026377,3321978400))
X=[sub(x,g)for x in P]
S=[];WS=[];U=[];WU=[];H=[];WH=[]
# Stable: orthogonal foot is in the relative interior of the maximal polygon.
for fi,(pl,f)in enumerate(faces):
 n=pl[:3];h=Q(pl[3])-dot(n,g);assert h>0
 foot=mul(h/dot(n,n),n)
 vals=[dot(cross(sub(X[j],X[i]),sub(foot,X[i])),n)for i,j in zip(f,f[1:]+f[:1])]
 if min(vals)>0:S.append(fi)
 elif min(vals)>=0:WS.append(fi)
# Unstable: radial normal strictly exposes a unique vertex.
for i in V:
 vals=[dot(X[i],sub(X[i],X[j]))for j in V if j!=i]
 if min(vals)>0:U.append(i)
 elif min(vals)>=0:WU.append(i)
# Saddle: foot lies inside edge and radial normal inside its normal cone.
for (i,j),owners in sorted(edges.items()):
 a,b=X[i],X[j];d=sub(b,a);dd=dot(d,d);t=-dot(a,d)/dd
 n1=faces[owners[0]][0][:3];n2=faces[owners[1]][0][:3]
 y=add(a,mul(t,d));A=dot(n1,n1);B=dot(n1,n2);C=dot(n2,n2);D=A*C-B*B;assert D>0
 lam=(C*dot(y,n1)-B*dot(y,n2))/D
 mu=(A*dot(y,n2)-B*dot(y,n1))/D
 assert y==add(mul(lam,n1),mul(mu,n2))
 vals=[t,1-t,lam,mu]
 if min(vals)>0:H.append([i,j])
 elif min(vals)>=0:WH.append([i,j])
assert (len(S),len(U),len(H))==(2,1,1)
assert WS==WU==WH==[]
assert U==[16]
# Third integration about the actual centroid: all positive, zero moments.
v2=Q(0);m2=[Q(0)]*3;nt=0
for _,f in faces:
 for j in range(1,len(f)-1):
  a,b,c=[X[t]for t in(f[0],f[j],f[j+1])]
  dv=det(a,b,c)/6;assert dv>0
  v2+=dv;nt+=1
  for k in range(3):m2[k]+=dv*(a[k]+b[k]+c[k])/4
assert v2==vol and m2==[0,0,0] and nt==42
D=lcm(*(z.denominator for i in V for z in X[i]))
N=max(abs(int(z*D))for i in V for z in X[i])
assert D==6643956800 and (D.bit_length(),N.bit_length())==(33,34)
# Exact unit-disk inclusion and slab containment about the actual centroid.
a=(-4,5,8);aa=dot(a,a);assert aa==105
section=[]
for pl,f in faces:
 n=pl[:3];h=Q(pl[3])-dot(n,g);den=aa*dot(n,n)-dot(n,a)**2
 assert h>0 and aa*h*h>=den
 if den:section.append(aa*h*h/den)
width=max(abs(dot(a,X[i]))for i in V)
assert width==Q(29487793421,6643956800) and width<5
assert min(section)==Q(263340533236748357640619663,198220164193090043428736000)>1
eta=Q(1,4);b=5
assert (1-2*eta)**2*aa>b*b
report={'V':len(V),'E':len(edges),'F':len(faces),'C':2*len(edges),'strict':[len(S),len(U),len(H)],'weak':[len(WS),len(WU),len(WH)],'volume':rational(vol),'input_centroid':[rational(x)for x in g],'centered_bits':[D.bit_length(),N.bit_length()],'input_vertex_indices':V,'stable_owner_sets':[sorted(faces[i][1])for i in S],'unstable_input_indices':U,'saddle_input_pairs':H,'maximal_faces':[f for _,f in faces],'positive_centered_tetrahedra':nt,'disk_axis':a,'slab_b':b,'centroid_radius':rational(eta),'slab_exact_width':rational(width),'section_inradius_squared':rational(min(section))}
print(json.dumps(report,sort_keys=True,separators=(',',':')))
print('CA95_C126_LITERAL_HULL_MASS_ALL_FEATURES_DISK_SLAB_PASS')
print('NO_NEW_OWN110_CLAIM')
```

## Structural turnover and finite methods

The production method finds the longest directed primal escape strand, replaces the whole strand by arc-length resampling, and relaxes all coordinates while rebuilding the hull and actual filled centroid on each evaluation. The initial C372 strand has49 vertices. Off-strand controls can move or become non-extreme.

The C378→32-strand endpoint yields the31-vertex C174 family. Starting again from exact `C174Q_G1500`, an18-strand remeshing yields C126 and a22-strand branch yields C156. C372→32-strand produces C240. Exact equality-lineage checks find zero unchanged surviving vertices and zero unchanged support planes at the stated nonlinear stages.

The grid100 C126 body uses18 accepted integer coordinate corrections after rounding the frozen production endpoint:

`[[0,0,-1],[6,2,-1],[9,1,-1],[9,2,1],[1,0,1],[19,2,1],[7,2,1],[20,0,1],[11,1,-1],[20,0,1],[15,2,-1],[1,1,-1],[17,2,1],[1,1,-1],[1,1,-1],[1,0,1],[1,1,-1],[15,0,1]]`.

The smaller C126 becomes markedly flatter: for the exact axis below, section-radius/halfwidth is approximately2.661, versus1.301 for `integer174_g200`. This is an observed construction tradeoff, not a theorem that every reduction must flatten.

Completed numerical work: eight whole-strand runs,80 starts,33219 objective calls;140 polar-bridge parameter settings screened with/without projective mass closure,280 screens;20 free-polar relaxation starts,4225 calls;1800 central-cut settings,3600 screens;11 deterministic integer-coordinate paths,34493 evaluations. None established own110. Those are finite-search observations, not exclusions. The full preserved production sources specify every seed, solver option and input; frozen rational checkpoints, rather than optimizer bit reproducibility, define the exact bodies.

## Exact feature-independent disk/slab obstruction

Let `a=(-4,5,8)`, so `|a|²=105`. Fix c0 and the unit disk `D={c0+x:a·x=0,|x|<=1}`. Let K be ANY full-dimensional uniformly filled convex polyhedron containing D, contained in `|a·(x-c0)|<=b`, whose actual filled centroid g obeys `|g-c0|<=eta<1/2`. If

`(1-2 eta)*sqrt(105)>b`,

then K has **at least two strict stable maximal facets**, regardless of vertex/support turnover or incidence.

Proof: put `Q=(K-g)^polar`. For q in Q with a·q=0, disk inclusion gives `|q|-q·(g-c0)<=1`, hence `|q|<=1/(1-eta)`. Slab containment puts `a/(b-a·(g-c0))` and `-a/(b+a·(g-c0))` in Q. Each has norm at least `sqrt(105)/(b+sqrt(105)*eta)>1/(1-eta)`. Consequently a norm maximizer in each closed polar half-polytope `Q∩{±a·q>=0}` lies in its open halfspace. For such q, any distinct q′ with `q·(q′-q)>=0` strictly increases squared norm along a sufficiently short initial segment still in that halfspace, contradiction. Thus q strictly exposes itself. It is a strict unstable polar vertex and its radial dual foot lies in the relative interior of its physical dual facet. The two halves supply distinct strict stable physical facets. No centroid of Q is used.

Exact disk verification for each own-centered supporting plane `N·x<=h` is `h>0` and `105h²>=105|N|²-(N·a)²`. Slab containment is checked on every vertex. The eight archived exact applications are: C126 grid100 and grid1000 with b5,eta1/4; C372,C378,C240 grid1000,C156 grid1000 with b8,eta1/10; C174Q grid1500 and integer174 grid200 with b9,eta1/20. Each scalar margin reduces to sqrt105>10. A common b9,eta1/20 also applies to all eight.

This excludes an infinite family of substantial feature changes. It excludes neither disk-breaking cuts, slab escape, nor centroid motion beyond the specified ball. It establishes no global lower bound or V>=9,F>=9 premise.

As external context, Domokos–Kovács's Conway-spiral homogeneous obstruction has its own monotone-meridian assumptions. I did not transfer those assumptions to these freely deformed bodies; the argument above is supplied directly.

## Core-breaking C220 construction

The exact `CA95_CORE_CUT174_G6` starts from `C174Q_G1500` at its actual centroid and intersects it with `n·x<=1` for `n1=(2713407,-1601008,527521)/10^6` and `n2=(-1598093,206865,-2758149)/10^6`. The production-frame parent centroid is `[6005111899690976,3205805648994216,1315025947348949]/19814525165526000`.

Both cuts cross the protected disk. The result is V69/E110/F43,C220,own323/weak000. Its volume is approximately1.8223722671 and its new centroid in the old own-centered frame approximately `(0.0170395746,0.0971429681,0.0952567126)`. Complete rational values regenerate from the exact parent and cuts in the full capsule.

Only5 of31 old vertices and41 old supporting planes survive. The facet histogram is12 triangles,25 quadrilaterals,4 pentagons, one29-gon and one35-gon. Its110 true edges differ from the201-edge triangular integration mesh. All134 centered tetrahedra have positive volume and zero total first moments.

Both old stable equilibria disappear although their supporting planes survive. The new stable carriers are old parent plane0 and both new cut faces. Both new unstable vertices are fresh intersections; the old unstable vertex disappears. Thus retiring the old basin's equilibria does not itself achieve cancellation. This body is retained as a mechanically worse but genuinely different construction, not advertised as the low-bit successor.

## Verification and provenance correction

The full source capsule's A implementation enumerates input point triples and reconstructs maximal facets and true incidence. B independently reconstructs the H-polytope by plane-pair clipping, polygon boundaries, positive interior-anchor moments and all equilibrium predicates. A third helper-free executable enumerates every supporting-plane triple. Centered integer integration supplies a further mass check. All35 new bodies and both assigned parents passed. Strict446 and weak123 negative software controls were rejected; these are not below-floor construction searches.

A metadata bug was detected and repaired during cold production verification: the original multi-grid ROUND loop reused a variable for report bytes, causing18 later `checkpoint_sha256` metadata fields to hash the preceding REPORT. Coordinates and all REPORT bytes were unaffected. The corrected source and metadata match the complete frozen hexadecimal inputs. `ROUND_LEGACY.py` and `INPUT_PROVENANCE_CORRECTION.json` preserve the old fields and original/corrected hashes. This is a provenance correction, not a replacement parent invented from a hash.

Selected canonical REPORT identities:

| Report | Bytes | SHA-256 |
|---|---:|---|
|`integer126_g100/REPORT.json`|3989|`512c370ee9d83e318b63a66245b0b8fad969f026448985e813983dd797ae83e6`|
|`integer174_g200/REPORT.json`|5628|`810bb0683ffd86ce32fe84107e746a19a7787d63804e33ffa2281139e10d4e2e`|
|`C174Q_G1500/REPORT.json`|6488|`911d7f796d2a2670ecc196263e61d1305e16d85f1d506c0be478ca65c05ca685`|
|`C126_G1000/REPORT.json`|4814|`a7dc908212ddcf2b957707fe79bfee20d69f446fa397cce3d4076b1d5f0617b5`|
|`C156_G1000/REPORT.json`|5774|`40e641e4020cba22c76b6537cb909af8e82eadb08e64e0f44ffb815678acea2a`|
|`C240_G1000/REPORT.json`|8406|`14100837e476e8ab2c7266f4d39cba24f3aa19315686df840dc308e684425fba`|
|`CA95_CORE_CUT174_G6/REPORT.json`|46759|`d9275ed31cfdd3d066d38eff66ac90be86494ef1473c51ecc701a9ddb87be206`|

## Complete-capsule preservation boundary

The principal C126 body, its exact mass, full-feature verifier and disk/slab theorem are self-contained above. **The remaining34 checkpoints and their complete production-method history require the complete Markdown capsule supplied with this response; their inputs are not all reproduced inside this shorter JSON field. Therefore this shorter field alone must not be treated as their durable recovery capsule.** The complete attached Markdown contains the literal standalone decoder and all68 source/input units, not just hashes or links. Preserve its bytes as material before relying on those additional constructions in a successor assignment.

The complete decoder is `CA95_RECOVER.py`,78232bytes,SHA `f86f2ac3c2538b4e565be7b11c3b289b96f6efd12229f9f3068b589557e61d77`. Its embedded68-file source dictionary is221915bytes,SHA `4d699d14d46ce801058166a304c9fd2aa2a873fdd6baa071a9fd37a9f99b0f0f`; XZ stream57660bytes,SHA `67f9eeb164af8c3793e362506b552cdbba1ea48b3a892dff034107aeb27493fa`; whitespace-free base6476880bytes,SHA `0db519387745e5c8f81338465d21af656a651f0063f568c72e05d29042dad3bf`.

Executed from a fresh decoded directory:

`python -B -S CA95_RECOVER.py CA95_COLD_FINAL 4`

Observed final markers:


[Encoded source block omitted; the code in this passage is incomplete.]


Exact replay uses the standard library, CPython3.13.5, assertions enabled. Optional discovery uses NumPy2.3.5, SciPy1.17.0 and PyTorch2.10.0+cpu, binary64 and one thread. The complete capsule includes every nondefault parameter, numerical production source, frozen input, integer move list, lineage source, correction record, manifest, all91 expected output hashes and commands.

## Most useful continuation

Use `integer174_g200` after preserving the complete capsule as the inexpensive mechanical starting point, with223 edges of headroom under E<=310 and a weaker observed flattening barrier than C126. Keep the fully literal C126 here as the size/arithmetic benchmark. A successful path must actually leave the protected disk/slab/centroid family; changing the names of stable carriers cannot do so.

The C220 body supplies an exact core-breaking operation, but its two large stable cut faces and two new unstable roots reveal the next coupled task: change the new cut faces and opposite moment-carrying region together. Its200-edge headroom permits new escape structure. Actual filled mass and both mechanical landscapes remain mandatory checks. None of these finite searches proves that this continuation fails.

## Attached complete recovery materials

Complete self-contained Markdown capsule, including the literal68-file decoder (`CA95_RESULT.md`)

Complete version2 JSON capsule (`CA95_RESULT.json`)

Standalone complete decoder (`CA95_RECOVER.py`)

Source and exact certificates (`CA95_EXACT_CAPSULE.zip`)

Supplementary full numerical logs (`CA95_FULL_OBSERVED.zip`)
