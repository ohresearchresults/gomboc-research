# figure-0593

AI research report · 2026-09-28 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Keen Lynx 13 — whole-P cancellation, four exact nonwinners, and a carrier-release bridge

Branch: `[internal-source-reference]`. This is a continuation handoff, not a branch-closure instruction.

## Result

**The entire physical P basin has been removed on actual homogeneous bodies within E249. No strict110 body was obtained.** Four retained exact endpoints have strict `(S,U,H)=(2,1,1)`, additional weak `(0,0,0)`, primitive-zero counts `(0,0,0)`, exactly `P=[]`, and exactly one positive Q bar. Thus the surviving obstruction is a polar/stable basin, not an unreported tiny physical bar.

The most useful endpoints are the low-edge **C334 carrier-release bridge** and the **C468/H80** body with sole Q depth about 0.19449543. The C354 body has particularly small exact mass coordinates. These are nonwinners; none is an own110 record.

I read the complete supplied journal through EOF, including its branch memory, and all four exact materials. Their byte counts and SHA-256 values matched the manifest. No missing external source, C622 construction, research connector or historical workspace was used. The literal parent used in computation was `J115_RELAY3_G6.txt`, SHA-256 `aa3003eb12e1b6258123c8fd3906bace48b474db6bed2348caa8a1930562a9bc`. Its exact replay returned `124/186/64`, strict121/weak000, P depth approximately 0.419325156574125, Q empty. G8 was not substituted. The supplied journal identifies the G6 and G8 bodies as distinct exact objects. fileciteturn1file0L28-L29

## Exact retained bodies

Here C means `2E`, consistently with the supplied auditor. Vertex IDs use the auditor's lexicographic ordering of primitive homogeneous integer coordinates; face IDs are input-support IDs. Different quantizations do not inherit vertex IDs.

| Exact name | V/E/F; C | Definition | All S | All U | All H |
|---|---|---|---|---|---|
| `KL13_BARRIER2_G6` | 61/177/118; 354 | Convex hull of 61 integer triples divided by 10^6 | [9,100] | [2] | [[25,41]] |
| `KL13_RETIRED84` | 85/167/84; 334 | Retain the specified 84 exact supporting planes of the preceding V-hull | [1,71] | [16] | [[35,49]] |
| `KL13_MIXED_G7` | 69/188/121; 376 | Convex hull of 62 integer V-controls/10^7, intersected with one integer H-cut/10^7 | [11,83] | [9] | [[4,51]] |
| `KL13_H80_G5` | 156/234/80; 468 | 80 literal integer normals, common right-hand side 100000 | [2,5] | [14] | [[19,110]] |

For **every row**, all additional-weak equilibrium lists are empty, all primitive-zero counts are zero, and all positive P bars form the empty list. The following table is the **complete** positive-Q output, not a filtered selection. In the three rightmost columns, an integer a denotes the rigorously checked open interval `(a,a+1)/10^15`. Birth and death are squared radii in the actual-centred polar; depth is `(birth-death)/birth`.

| Body | Q root | Q death edge | Birth lower numerator | Death lower numerator | Depth lower numerator |
|---|---:|---|---:|---:|---:|
| BARRIER2_G6 | 100 | [70,97] | 2179067911216627 | 1494105331962623 | 314337417263683 |
| RETIRED84 | 71 | [45,68] | 2173747114683805 | 1496020603217429 | 311777992429886 |
| MIXED_G7 | 83 | [80,98] | 2232133483476764 | 1602273202829004 | 282178590711650 |
| H80_G5 | 5 | [48,49] | 2126438000406148 | 1712855519453866 | 194495433618703 |

### Actual homogeneous mass and centre

Density is one, so mass equals volume. The same interval convention `(a,a+1)/10^15` applies to every entry below, including negative centre coordinates. The recovery program computes and writes the complete exact rational values, not only these intervals.

| Body | Volume lower numerator | gx lower numerator | gy lower numerator | gz lower numerator |
|---|---:|---:|---:|---:|
| BARRIER2_G6 | 2828412670706856 | -24049455008867 | -20952635660335 | 14198845925779 |
| RETIRED84 | 2836768606442852 | -24299733737482 | -20318781053159 | 13658902121670 |
| MIXED_G7 | 2748058064031089 | 234078477084 | 410348196080 | -12220845464662 |
| H80_G5 | 2673829792833309 | -17095475025571 | -17812635695522 | -22787363883168 |

The small-coordinate V61 fixture has exact volume `16970476024241138783/6000000000000000000` and exact centre

`(-204065349812019641852751/8485238012120569391500000, -1422304804473457664783057/67881904096964555132000000, 963844697421342451474013/67881904096964555132000000)`.

Its volume numerator/denominator bit lengths are 64/63; the largest centre numerator/denominator bit lengths are 81/86. The mixed body's largest centre numerator/denominator bit lengths are 751/763. These are useful arithmetic alternatives to the more deeply intersected H80 body; a smaller remaining Q does not make the other fixtures dispensable.

## Constructive mechanism and what changed

The successful direction was not another tiny direct cut of the original host. I constructed opposed finite physical routes from the old unwanted maximum toward the old elder, then retired physical carrier vertices, rebuilt the actual mass, and repaired the complete physical outgoing-witness forest. The route construction alone did not preserve the old centre or solve the problem: intermediate bodies acquired additional equilibria. Further polar-root repair and free-vertex deformation produced a genuine actual-mass U1 body. Subsequent deformation reduced its surviving Q basin and gave the exact V61 fixture.

A numerical reference route used short/long arc subdivision counts 16/32, transverse bow coefficients -0.3/+0.3, radial-slack exponent 0.5 on both arcs, and zero second-harmonic bow. For endpoints u,z, directions were normalized combinations of the great-circle direction and the transverse bow. With consecutive directional dot products c_j>0, cumulative cost was `L_j=sum_{i<=j}(-log c_i)` and radii were `|u| exp(L_j + (log(|z|/|u|)-L_n) t_j^p)`. This creates reference positive chords when the slack is positive. It is not a uniform-mass certificate. The retained exact endpoints below are recovered from their full literal inputs, not from an assumed bit-identical replay of floating optimization.

The decisive budget operation was **retire first, then release a different set of geometric constraints**. Starting from the exact V61 body, retirement of 34 exact supporting planes produced RETIRED84. It has both V<=85 and F<=85, while retaining own211 and P empty. It is therefore a useful bridge between whole-V and whole-H parameterizations. Releasing its H normals, rebuilding physical mass at every step, and applying a nonroot-clearance barrier eventually produced the H80 endpoint. This motion changed the old supports, rather than repeatedly spending an extra face to preserve a fixed host.

The budget statement is elementary and does not require a simple-polyhedron assumption: Euler and the minimum degree of the primal and dual graphs give `E<=3V-6` and `E<=3F-6`. Therefore V<=85 is sufficient for unrestricted generic V release within E249, and F<=85 is sufficient for generic H release. Neither is a necessary bound on all eligible bodies. RETIRED84 is simultaneously small enough for both releases. Its 37 nonsimple vertices and maximum degree eight explain why its current E167 is much smaller than either generic upper bound.

The mixed endpoint separately verifies the requested mixed-geometry freedom. Its maximal-face histogram is **112 triangles, eight quadrilaterals and one octagon**. Consequently its true edge count is `(112*3+8*4+8)/2=188`. Triangulating those coplanar faces introduces **13 diagonals** and would incorrectly report E201. It has 55 nonsimple vertices, maximum degree 14. The exact recovery preserves the V-hull and the cut as separate rational inputs; it does not independently round their newly intersected vertices.

The supplied numerical continuation differentiates the physical uniform centroid, not a transported centre or polar mass. It minimizes the remaining Q depth plus a barrier on all physical nonroot outgoing chords and all polar nonroot outgoing chords except the permitted unwanted stable root. Each trial rebuilds the hull and its actual mass. Its smooth continuation below epsilon is a search device; only the exact auditors establish class and absence of weak equilibria. Numerical display thresholds and unsuccessful line searches were never treated as exact cancellation.

## A new exact fixed-host exit bound

This bound is for **H80_G5 at its own audited centre**, not an imported R82 or C2 obstruction.

Let u be polar point 5, and keep old polar elder 2. The exact old positive-chord graph has 36 vertices which can reach elder 2. Of these, only `[1,2,12,17,18]` have radius greater than |u|. Every other old point outside the elder component also has radius at most |u|. For each of the five possible longer endpoints z, exact integer tests prove

`|z|/|u| < 323/250`, and `angle(u,z) > 59/25` radians.

The angle test uses `u.z<0` and `(u.z)^2 > (71/100)^2 |u|^2 |z|^2`; the rational alternating Taylor lower sum through x^10 proves `cos(59/25)>-71/100`. No floating inverse trigonometry is used in the certificate.

A strict positive-chord n-link chain must satisfy `R*cos(phi/n)^n>1`: each chord forces a strictly increasing radius, and convexity of log(sec) bounds the product of the required radial increases. At ten links, the exact rational upper bound is

`(323/250) * (1-(59/250)^2/2+(59/250)^4/24)^10 < 0.975398 < 1`.

The necessary product increases with link count in its admissible range. Therefore **no chain of at most ten links** can exit u to an old vertex in the old elder component. In an old-elder-rooted positive-chord relay tree, the first old exit consequently requires at least eleven links, with at least ten new internal points.

This is deliberately scoped. It does **not** exclude changing old supports, changing the actual centre, creating a new elder, retiring old carrier geometry, or a finite body with E<=249. In particular, it is not a face-budget impossibility theorem. It explains why another very short, fixed-host old-elder relay is the wrong continuation for this particular endpoint, while carrier release and moving-host geometry remain open.

## Verification, recovery and continuation

All four endpoints passed the supplied `exact115.cpp` auditor. I then implemented the separate pure-Python exact auditor below. On all four bodies, the two implementations agree exactly on every vertex coordinate, volume, centroid, all strict/weak and primitive-zero counts, all equilibrium IDs, and every positive bar's root, merger edge, birth, death and depth. Their maximal face sets and true edge sets also agree; only cyclic face rotations and edge output ordering differ. The V61 body additionally passed a direct V-input mass/mechanics/bar implementation, without obtaining its coordinates from H intersections.

The Python auditor below uses integer plane enumeration, exact boundedness tests, exact maximal-face cycles, two mass decompositions, local and nonlocal mechanical tests, and persistence on true primal/dual edge graphs with **no bar floor**. It deliberately requires every submitted H row to be an active maximal support; all four literal fixtures satisfy that premise. It uses only the Python standard library. Tested Python version: 3.13.5. The earlier C++ replay used g++ 14.2.0 and GMP 6.3.0.

Save the following three complete files with their indicated names. Run:

```bash
python recover_kl13.py
```

This regenerates the four exact H inputs, the V and mixed-control inputs, complete rational audit JSONs, and the exact exit certificate. It was rerun successfully in a clean directory containing only these three files. The expected last marker is:

```text
KL13_FOUR_EXACT_NONWINNERS_PASS
```

For numerical continuation from the exact low-Q fixture:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python continue_kl13.py KL13_H80_G5.txt next.json 1200 0.00001 0.0000001 0.0000001
```

The continuation dependencies tested here are NumPy 2.3.5, SciPy 1.17.0 and torch 2.10.0+cpu. A 25-iteration smoke run of this standalone unit was executed. Its output is a numerical nomination, not another promoted exact endpoint. Rationalize and exact-audit any proposed successor; do not infer success from an empty displayed bar list or the optimizer status.

The most useful next construction is to exploit the two small feature counts of RETIRED84 for a genuinely different V release, or continue moving the H80 host while using mixed geometry to protect the complete physical forest. The current exact results do not establish convergence to own110. The remaining positive Q is substantial and must be removed on the same final homogeneous body.

## Complete source capsule

### exact_kl13.py

UTF-8/LF bytes: 7560. SHA-256: `2e83f7069ca318a18838697e021f2c3977d76c2df61e1686ad81a3ddb94a6dd4`.

```python
"""Pure-Python exact homogeneous-polyhedron verifier.
No floating point, Qhull, GMP or prior audit is used. H input rows are (n,h),
meaning n.x<=h with h>0. Maximal faces, true edges and every positive bar
are reconstructed using integers/Fraction. Python 3.13.5 was tested.
"""
import itertools,math,json,sys
from fractions import Fraction as Q
from functools import cmp_to_key
from pathlib import Path
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(c,a):return tuple(c*x for x in a)
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def primitive(row):
 d=math.gcd(*row);return tuple(x//d for x in row)
def support_planes(points,D):
 pts=sorted(set(map(tuple,points)));out=set()
 for a,b,c in itertools.combinations(pts,3):
  n=cross(sub(b,a),sub(c,a))
  if n==(0,0,0):continue
  h=dot(n,a);pos=neg=False
  for v in pts:
   z=dot(n,v)-h;pos|=z>0;neg|=z<0
   if pos and neg:break
  if pos and neg:continue
  if pos:n=mul(-1,n);h=-h
  assert h>0
  out.add(primitive(tuple(D*x for x in n)+(h,)))
 return sorted(out)
def intersections(rows):
 assert all(r[3]>0 for r in rows);vertices=set();bounded=set()
 for a,b,c in itertools.combinations(rows,3):
  n0,n1,n2=a[:3],b[:3],c[:3];c0,c1,c2=cross(n1,n2),cross(n2,n0),cross(n0,n1);d=dot(n0,c0)
  if not d:continue
  if d<0:c0,c1,c2=mul(-1,c0),mul(-1,c1),mul(-1,c2);d=-d
  for ax in range(3):
   w=[c0[ax],c1[ax],c2[ax]]
   if min(w)>=0:bounded.add((ax,1))
   if max(w)<=0:bounded.add((ax,-1))
  num=add(add(mul(a[3],c0),mul(b[3],c1)),mul(c[3],c2))
  if all(dot(r[:3],num)<=r[3]*d for r in rows):vertices.add(primitive(num+(d,)))
 assert len(bounded)==6,'No boundedness certificate'
 return sorted(vertices)
def cycle(ids,v,n):
 axes=[j for j in range(3) if j!=max(range(3),key=lambda k:abs(n[k]))];c=[sum(v[i][k] for i in ids)/len(ids) for k in axes]
 xy={i:(v[i][axes[0]]-c[0],v[i][axes[1]]-c[1]) for i in ids}
 def half(t):return 0 if t[1]>0 or (t[1]==0 and t[0]>=0) else 1
 def cmp(i,j):
  a,b=xy[i],xy[j];ha,hb=half(a),half(b)
  if ha!=hb:return -1 if ha<hb else 1
  d=a[0]*b[1]-a[1]*b[0];assert d!=0
  return -1 if d>0 else 1
 cy=sorted(ids,key=cmp_to_key(cmp));a,b,c=[v[i] for i in cy[:3]]
 if dot(cross(sub(b,a),sub(c,a)),n)<0:cy.reverse()
 return cy
def census_flags(z):return all(x>0 for x in z),all(x>=0 for x in z) and any(x==0 for x in z),any(x==0 for x in z)
def bars(hom,edges,scale=Q(1)):
 A=[dot(t[:3],t[:3]) for t in hom];sq=[Q(a,t[3]**2) for a,t in zip(A,hom)];level=[]
 for i,j in edges:
  a,b=A[i],A[j];di,dj=hom[i][3],hom[j][3];c=dot(hom[i][:3],hom[j][:3])
  if a*dj-c*di<=0:level.append(sq[i])
  elif b*di-c*dj<=0:level.append(sq[j])
  else:level.append(Q(a*b-c*c,a*dj*dj+b*di*di-2*c*di*dj))
 par=list(range(len(hom)));birth=par.copy();out=[]
 def root(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 for k in sorted(range(len(edges)),key=lambda k:(-level[k],edges[k])):
  i,j=edges[k];ra,rb=root(i),root(j)
  if ra==rb:continue
  if (sq[birth[ra]],-birth[ra])<(sq[birth[rb]],-birth[rb]):ra,rb=rb,ra
  u=birth[rb]
  if sq[u]>level[k]:out.append(dict(root=u,edge=list(edges[k]),birth=str(scale*sq[u]),death=str(scale*level[k]),depth=str((sq[u]-level[k])/sq[u])))
  par[rb]=ra
 assert len({root(i) for i in range(len(hom))})==1
 return sorted(out,key=lambda r:(-Q(r['depth']),r['root'],r['edge']))
def audit(rows):
 rows=[tuple(map(int,r)) for r in rows];raw=intersections(rows);v=[tuple(Q(z,r[3]) for z in r[:3]) for r in raw];faces=[];edges={}
 for f,row in enumerate(rows):
  ids=[i for i,r in enumerate(raw) if dot(row[:3],r[:3])==row[3]*r[3]]
  assert len(ids)>=3,'This verifier requires all submitted H supports to be active'
  cy=cycle(ids,v,row[:3]);faces.append(cy)
  for a,b in zip(cy,cy[1:]+cy[:1]):edges.setdefault(tuple(sorted((a,b))),[]).append(f)
 assert all(len(fs)==2 for fs in edges.values())
 assert len(v)-len(edges)+len(faces)==2
 assert set(sum(faces,[]))==set(range(len(v)))
 tet=[(cy[0],b,c) for cy in faces for b,c in zip(cy[1:-1],cy[2:])];volume=Q(0);moment=(Q(0),)*3
 for ids in tet:
  a,b,c=[v[i] for i in ids];w=det(a,b,c)/6;assert w>0;volume+=w;moment=add(moment,mul(w/4,add(add(a,b),c)))
 g=mul(1/volume,moment);den=math.lcm(*(x.denominator for x in g));G=tuple(x.numerator*(den//x.denominator) for x in g)
 ph=[tuple(den*r[k]-r[3]*G[k] for k in range(3))+(den*r[3],) for r in raw];p=[sub(x,g) for x in v]
 # An independent interior-centred tetrahedral sum has identical volume and zero first moment.
 V2=Q(0);M2=(Q(0),)*3
 for ids in tet:
  a,b,c=[ph[i] for i in ids];w=Q(det(a[:3],b[:3],c[:3]),6*a[3]*b[3]*c[3]);assert w>0;V2+=w;M2=add(M2,mul(w/4,add(add(p[ids[0]],p[ids[1]]),p[ids[2]])))
 assert V2==volume and M2==(0,0,0)
 off=[r[3]*den-dot(r[:3],G) for r in rows];assert min(off)>0
 qh=[r[:3]+(h,) for r,h in zip(rows,off)];strict=[[],[],[]];weak=[[],[],[]];zeros=[0,0,0];neigh=[set() for r in raw]
 for a,b in edges:neigh[a].add(b);neigh[b].add(a)
 for i,a in enumerate(raw):
  num=ph[i][:3];tests=[-dot(num,sub(mul(a[3],raw[j][:3]),mul(raw[j][3],a[:3]))) for j in neigh[i]];s,w,z=census_flags(tests)
  if s:strict[1].append(i)
  if w:weak[1].append(i)
  zeros[1]+=z
 for f,cy in enumerate(faces):
  n=rows[f][:3];foot=mul(Q(off[f],den*dot(n,n)),n);tests=[dot(cross(sub(p[b],p[a]),sub(foot,p[a])),n) for a,b in zip(cy,cy[1:]+cy[:1])];s,w,z=census_flags(tests)
  if s:strict[0].append(f)
  if w:weak[0].append(f)
  zeros[0]+=z
 pe=sorted(edges);qe=[tuple(sorted(edges[e])) for e in pe]
 for a,b in pe:
  f,k=edges[(a,b)];n1,n2=rows[f][:3],rows[k][:3];d=sub(p[b],p[a]);dd=dot(d,d);T=-dot(p[a],d);x=add(p[a],mul(T/dd,d));ab=dot(n1,n2);X=dot(n2,n2)*dot(x,n1)-ab*dot(x,n2);Y=dot(n1,n1)*dot(x,n2)-ab*dot(x,n1);assert dot(n1,n1)*dot(n2,n2)>ab*ab;s,w,z=census_flags([T,dd-T,X,Y])
  if s:strict[2].append([a,b])
  if w:weak[2].append([a,b])
  zeros[2]+=z
 # Global nonlocal mechanical tests independently agree with the face/edge tests.
 pu=[];sw=[]
 for i,a in enumerate(raw):
  test=[dot(ph[i][:3],sub(mul(a[3],b[:3]),mul(b[3],a[:3]))) for j,b in enumerate(raw) if j!=i]
  if max(test)<0:pu.append(i)
  if max(test)==0:sw.append(i)
 assert pu==strict[1] and sw==weak[1]
 qs=[];qw=[]
 for i,a in enumerate(rows):
  aa=dot(a[:3],a[:3]);test=[dot(a[:3],b[:3])*off[i]-aa*off[j] for j,b in enumerate(rows) if j!=i]
  if max(test)<0:qs.append(i)
  if max(test)==0:qw.append(i)
 assert qs==strict[0] and qw==weak[0]
 P=bars(ph,pe);B=bars(qh,qe,Q(den*den));assert len(strict[0])+len(strict[1])-len(strict[2])==2
 return dict(V=len(raw),E=len(pe),F=len(faces),C=2*len(pe),volume=str(volume),centroid=list(map(str,g)),strict=list(map(len,strict)),weak=list(map(len,weak)),primitive_zeros=zeros,S=strict[0],U=strict[1],H=strict[2],vertices=[[str(z) for z in x] for x in v],faces=faces,edges=[list(e) for e in pe],P=P,Q=B,checks='PYTHON_EXACT_HULL_TWO_MASS_FORMULAS_LOCAL_GLOBAL_MECHANICS_FULL_BARS_PASS')
def read_h(path):
 lines=Path(path).read_text().splitlines();m,D=map(int,lines[0].split());rows=[tuple(map(int,s.split())) for s in lines[1:] if s.strip()];assert len(rows)==m
 return [r+(D,) if D else r for r in rows]
if __name__=='__main__':
 r=audit(read_h(sys.argv[1]));Path(sys.argv[2]).write_text(json.dumps(r,indent=2)+'\n');print('PYTHON_EXACT_PASS VEF='+str(r['V'])+'/'+str(r['E'])+'/'+str(r['F'])+' SUH='+ '/'.join(map(str,r['strict']))+' weak='+''.join(map(str,r['weak']))+' P='+str(len(r['P']))+' Q='+str(len(r['Q'])),flush=True)
```

### recover_kl13.py

UTF-8/LF bytes: 11271. SHA-256: `f728a3e8180f5b89349ed4d1a40e3d77f9cd53b0faea4c00f2ce0a5a4790843a`.

```python
"""Literal recovery and complete verification of the four KL13 exact bodies.
Save next to exact_kl13.py and run: python recover_kl13.py
Uses Python standard library only. Audit output contains full rational mass,
centroid, all vertices/maximal faces/true edges, equilibria and positive bars.
"""
import json,sys,math,hashlib
from pathlib import Path
from fractions import Fraction as Q
from fractions import Fraction as F
from exact_kl13 import audit,support_planes,read_h,dot
sys.set_int_max_str_digits(0)

V61 = {"D":1000000,"points":[[-898714,-645077,865098],[23974,-588137,439727],[-64656,429695,-701447],[40082,796079,-571407],[-493293,348842,-454921],[-379299,459692,-53159],[228575,706429,-676881],[-182605,838584,-378777],[-188704,702024,-590395],[817062,-221751,172199],[586860,-442466,328721],[380677,-591824,195547],[632827,340859,-631696],[876866,255723,-394987],[687250,-314826,343453],[339520,-669028,-381224],[406665,727,-689038],[295154,-429899,-647927],[931408,19168,-113180],[281685,-616713,-566366],[-68979,-359516,-846360],[-269444,-329456,-856697],[-86641,-834821,-764838],[-454672,-585686,-859572],[-368166,-829659,-750531],[-797823,-501790,-588181],[-480884,-909480,-617483],[-493291,-1008806,-470595],[-723256,-981265,-305626],[-795487,-1013135,-54429],[-888305,-953904,125044],[-935876,-887817,320184],[-946002,-806532,524185],[537047,525117,-672384],[480695,745940,-544320],[900240,442717,-219884],[642022,749925,-393550],[744969,747626,-230339],[704637,827882,-105562],[336086,988248,-95375],[655100,889082,25289],[634975,902775,145630],[593476,916834,256515],[539858,924175,365315],[474747,923287,472794],[402523,910181,578651],[338745,872779,688831],[276801,818289,794679],[179700,789034,863814],[88583,733840,938397],[-2008,664948,1005876],[-81166,583746,1064050],[-149090,489860,1114563],[-241581,381359,1154635],[-324910,248309,1185909],[-413255,119915,1192976],[-494224,-38132,1185540],[-575330,-137959,1151832],[-670157,-292287,1090266],[-740762,-478925,959914],[335515,472135,-724818]]}
MIX = {"D":10000000,"points":[[-8209770,-6605337,8472771],[1041269,-5577551,3967443],[652240,5320490,-6765974],[1602589,8792338,-5361686],[-4373325,3537202,-4829396],[-2849831,5596742,-793220],[3585512,7850773,-6336517],[-1338691,9033597,-3596117],[193306,8483819,-5592115],[8723093,-1713688,1264840],[6648444,-3837469,2755582],[4119827,-5570966,1557168],[7171067,3991549,-6011988],[9147145,2698627,-3725097],[7691714,-2279411,2885979],[2931712,-6675026,-4526328],[4482073,-156548,-6654722],[3487476,-3805664,-6226208],[9483835,203106,-1134744],[3664785,-4942616,-5380927],[-2985429,-6176723,-9300863],[-3382654,-3854176,-8992985],[-577855,-8259114,-7515131],[-5667134,-4934308,-8595984],[-4608889,-7942422,-7557151],[-7825292,-3699780,-6744886],[-6163618,-8443028,-6058988],[-5814442,-9968189,-4252454],[-7033463,-9983348,-2500145],[-7897654,-9850751,-502039],[-8547762,-9396373,1217223],[-8921854,-8778892,3166973],[-8913497,-7940509,5430473],[6177057,5766831,-6401530],[5515122,8088811,-4924011],[9323415,4744277,-1751579],[6829543,8010953,-3546612],[7630859,7982010,-2017398],[7085763,8750268,-978340],[3738705,10243711,-1127831],[6437928,9376746,59810],[6059909,9615405,1144018],[5552531,9798910,2179573],[4972256,9891203,3186665],[4348630,9871397,4182977],[3690691,9737488,5154456],[3138456,9414725,6136102],[2610508,8952741,7095578],[1834801,8645292,7757252],[375353,7637078,9050359],[-304528,6957023,9644084],[-927418,6145597,10202349],[-1502880,5189091,10719665],[-2261001,4069706,11149898],[-2958749,2694735,11505891],[-3687831,1370055,11626923],[-4305277,-171892,11612512],[-5147073,-1335288,11286305],[-6072125,-2978653,10676174],[-6865880,-5081125,9274225],[4902551,6236748,-6716787],[1089047,8203259,8415625]],"cuts":[[4745850,-1050519,-11662438]]}
KEEP = [0,1,2,4,5,6,7,8,13,14,17,18,19,21,23,24,25,26,27,29,31,32,36,37,38,39,40,41,42,43,46,47,50,51,52,55,56,58,60,61,62,64,65,67,69,70,71,72,73,74,77,78,79,80,82,83,84,85,86,87,88,89,90,91,93,94,95,96,97,98,99,100,101,103,104,105,106,107,108,112,114,115,116,117]
H80 = '''80 100000
38646 -114692 77132
-160798 74612 10769
-162910 88141 27756
41214 -104608 88928
49825 -121086 61273
59728 -125093 44328
13307 -131099 32198
-18243 25368 -127440
-36392 33796 -123083
-29403 67108 -79353
17047 87686 -42417
-4715 101289 -23737
-105798 64562 -73533
-1195 15447 -128894
30716 52988 -77761
-37746 108916 31810
-77410 111833 34293
-95387 108136 35699
-125718 100402 35196
-55663 43515 -114769
-77881 53608 -100379
97187 -100952 -11883
101220 1967 91251
101605 -91456 -26822
115391 24161 60951
106850 20247 79306
90531 -109176 2431
59213 -58904 114605
49034 -77465 109258
41910 -93343 100082
82148 -115921 16473
71923 -121346 29663
87055 -58417 -82984
76185 25199 -65281
79946 -49643 -93349
54456 -25568 -114910
45329 -18387 -119301
93943 -66347 -70737
99395 -74105 -56927
102819 3806 -24683
85825 -1401 108555
73445 -20187 117531
65207 -38603 118814
103901 -80754 -41436
25214 -123211 6865
72247 -40714 -102064
63328 -32995 -109277
110215 32017 44682
13790 5486 -127839
36084 -10943 -122549
-5011 -40218 -82113
-9079 -70219 -49396
-41778 -44933 -58379
-79768 -29889 -24224
-97409 -10747 -15321
-122481 20286 -4120
-41533 -55813 -44537
-35844 -70036 -24770
-65733 -42597 -29431
-9266 -107013 21398
49284 52840 -67748
33064 85462 -33198
74527 46107 -49587
76896 58033 -9186
91580 48879 23226
56304 71120 -25414
40360 85028 -23303
71376 64063 1579
33189 90697 -2762
19028 97890 8370
10072 100049 15915
-2448 103198 20965
54861 55781 58210
7587 76913 52414
35930 42105 79204
63839 2877 105928
-66039 76052 55337
71219 -18559 116592
-110167 74100 46866
-55206 17020 71233
'''
EXPECTED = {'KL13_BARRIER2_G6': {'VEF': [61, 177, 118], 'S': [9, 100], 'U': [2], 'H': [[25, 41]], 'mass': 2828412670706856, 'g': [-24049455008867, -20952635660335, 14198845925779], 'bar': [100, [70, 97], 2179067911216627, 1494105331962623, 314337417263683]}, 'KL13_RETIRED84': {'VEF': [85, 167, 84], 'S': [1, 71], 'U': [16], 'H': [[35, 49]], 'mass': 2836768606442852, 'g': [-24299733737482, -20318781053159, 13658902121670], 'bar': [71, [45, 68], 2173747114683805, 1496020603217429, 311777992429886]}, 'KL13_MIXED_G7': {'VEF': [69, 188, 121], 'S': [11, 83], 'U': [9], 'H': [[4, 51]], 'mass': 2748058064031089, 'g': [234078477084, 410348196080, -12220845464662], 'bar': [83, [80, 98], 2232133483476764, 1602273202829004, 282178590711650]}, 'KL13_H80_G5': {'VEF': [156, 234, 80], 'S': [2, 5], 'U': [14], 'H': [[19, 110]], 'mass': 2673829792833309, 'g': [-17095475025571, -17812635695522, -22787363883168], 'bar': [5, [48, 49], 2126438000406148, 1712855519453866, 194495433618703]}}
INPUT_SHA256 = {'KL13_BARRIER2_G6_H.txt': 'fb020854af52107be86d30198890842ff47ec1e8762b823ac899f529a60216b5', 'KL13_RETIRED84_H.txt': 'ca9d91943a6cebc9853f4b79c1bc467df314e3d0ca2142cb41b722cc92bc972f', 'KL13_MIXED_G7_H.txt': '29c958ccb9e1c3918f25fb01723a62850ea94031bc7c63f2719947ef9045fa84', 'KL13_H80_G5.txt': '97bf66b9c4c75e8a2fc5d93367eeb7b735dbea71932b23b067b822d7add5525e'}

def write_h(path,rows):
    Path(path).write_text(str(len(rows))+' 0\n'+''.join(' '.join(map(str,row))+'\n' for row in rows))
def interval(x,a):
    x=Q(x);assert Q(a,10**15)<x<Q(a+1,10**15)

def exit_bound(inp,auditfile,out):
 lines=Path(inp).read_text().splitlines();m,D=map(int,lines[0].split());N=[tuple(map(int,s.split())) for s in lines[1:] if s.strip()];assert len(N)==m==80 and D==100000 and all(len(n)==3 for n in N)
 a=json.load(open(auditfile));assert a['strict']==[2,1,1] and a['weak']==[0,0,0] and a['S']==[2,5]
 g=list(map(F,a['centroid']));den=math.lcm(*(x.denominator for x in g));G=[x.numerator*(den//x.denominator) for x in g];B=[D*den-dot(n,G) for n in N];assert min(B)>0;A=[dot(n,n) for n in N]
 # q_i=den*N_i/B_i; all sign tests below cancel common positive factors.
 positive=[[dot(N[i],N[j])*B[i]>A[i]*B[j] for j in range(m)] for i in range(m)]
 root,elder=5,2;assert not any(positive[root]) and not any(positive[elder]);assert all(any(positive[i]) for i in range(m) if i not in [root,elder])
 reach={elder}
 while True:
  r=reach|{i for i in range(m) if any(positive[i][j] for j in reach)}
  if r==reach:break
  reach=r
 assert root not in reach
 assert all(A[i]*B[root]**2<=A[root]*B[i]**2 for i in range(m) if i not in reach)
 too_short=[];large=[]
 for j in sorted(reach):
  left=A[j]*B[root]**2;right=A[root]*B[j]**2
  if left<=right:too_short.append(j);continue
  C=dot(N[root],N[j]);assert left*250**2<right*323**2
  assert C<0 and 10000*C*C>5041*A[root]*A[j]
  large.append(j)
 # cos(59/25)>-71/100, by the alternating Taylor lower sum through x^10.
 x=F(59,25);lower=sum((-1)**k*x**(2*k)/math.factorial(2*k) for k in range(6));assert lower>F(-71,100)
 # At ten links, cos(phi/10) < 1-t^2/2+t^4/24, t=59/250.
 t=x/10;upper=1-t*t/2+t**4/24;ceiling=F(323,250)*upper**10;assert ceiling<1
 r=dict(root=root,elder=elder,old_elder_reachable=sorted(reach),norm_blocked=too_short,long_angle_endpoints=large,radius_ratio_upper='323/250',angle_lower='59/25',ten_link_product_upper=str(ceiling),excluded_link_counts=list(range(1,11)),scope='Fixed old polar points at the audited old centre; positive-chord exits to the existing elder component only. Not a finite-deformation, new-elder, actual-new-mass or edge-budget exclusion.')
 Path(out).write_text(json.dumps(r,indent=2)+'\n');print('KL13_EXACT_OLD_HOST_EXIT_BOUND_PASS reachable='+str(len(reach))+' long_angle='+str(large)+' excluded_links=1..10',flush=True)

def main():
    Path('KL13_BARRIER2_G6.json').write_text(json.dumps(V61,separators=(',',':'))+'\n')
    Path('KL13_MIXED_G7.json').write_text(json.dumps(MIX,separators=(',',':'))+'\n')
    base=support_planes(V61['points'],V61['D'])
    write_h('KL13_BARRIER2_G6_H.txt',base)
    write_h('KL13_RETIRED84_H.txt',[base[i] for i in KEEP])
    mixed=support_planes(MIX['points'],MIX['D'])+[tuple(n)+(MIX['D'],) for n in MIX['cuts']]
    write_h('KL13_MIXED_G7_H.txt',mixed)
    Path('KL13_H80_G5.txt').write_text(H80)
    for name,expected in INPUT_SHA256.items():assert hashlib.sha256(Path(name).read_bytes()).hexdigest()==expected,name
    for name,want in EXPECTED.items():
        inp=name+'.txt' if name=='KL13_H80_G5' else name+'_H.txt'
        r=audit(read_h(inp));assert [r[k] for k in ['V','E','F']]==want['VEF']
        assert r['strict']==[2,1,1] and r['weak']==[0,0,0] and r['primitive_zeros']==[0,0,0]
        for k in ['S','U','H']:assert r[k]==want[k]
        assert r['P']==[] and len(r['Q'])==1
        interval(r['volume'],want['mass'])
        for x,a in zip(r['centroid'],want['g']):interval(x,a)
        b=r['Q'][0];assert [b['root'],b['edge']]==want['bar'][:2]
        for k,a in zip(['birth','death','depth'],want['bar'][2:]):interval(b[k],a)
        if name=='KL13_BARRIER2_G6':
            original={tuple(Q(z,V61['D']) for z in x) for x in V61['points']}
            assert {tuple(map(Q,x)) for x in r['vertices']}==original
        out=name+'_PYTHON_AUDIT.json';Path(out).write_text(json.dumps(r,indent=2)+'\n')
        print(name+' EXACT_PASS VEF='+ '/'.join(map(str,want['VEF']))+' SUH=2/1/1 weak=000 P=0 Q=1',flush=True)
    exit_bound('KL13_H80_G5.txt','KL13_H80_G5_PYTHON_AUDIT.json','KL13_EXIT_BOUND.json')
    print('KL13_FOUR_EXACT_NONWINNERS_PASS',flush=True)
if __name__=='__main__':main()
```

### continue_kl13.py

UTF-8/LF bytes: 7323. SHA-256: `13113e6271bf7f3f05df487a73883832ceaa10284abf650ac214bc75e32f0c6e`.

```python
"""Numerical free-H actual-mass continuation from the exact H80 input.
This is a nomination producer, not an exact strict/weak certificate.
The chart rejects merged polar facets. Use the exact verifier for endpoints.
Tested: Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, torch 2.10.0+cpu.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import sys,json
from pathlib import Path
import numpy as np,torch
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import minimize
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def geometry(n):
    n=np.asarray(n,dtype=float)
    qh=ConvexHull(n)
    if qh.equations[:,3].max()>=-1e-10: raise ValueError('origin not inside polar')
    # Generic input assumption: dual hull facets are triangles. Reject any
    # nontriangular polar facet rather than counting triangulation diagonals.
    normals=qh.equations[:,:3]; offs=qh.equations[:,3]
    vs=-normals/offs[:,None]
    if len(vs)>1:
        from scipy.spatial.distance import pdist
        if pdist(vs).min()<1e-9: raise ValueError('nongeneric input: merged dual facet')
    tri=qh.simplices.copy()
    faces={}; polys=[]; total=0.; first=np.zeros(3)
    for j in qh.vertices:
        inds=np.where(np.any(tri==j,axis=1))[0]
        a=n[j]; axis=np.eye(3)[np.argmin(abs(a))]
        e=np.cross(a,axis); e/=np.linalg.norm(e); f=np.cross(a,e)
        c=vs[inds].mean(axis=0); delta=vs[inds]-c
        inds=inds[np.argsort(np.arctan2(delta@f,delta@e))]
        faces[int(j)]=inds.tolist()
        for b,cidx in zip(inds[1:-1],inds[2:]):
            ids=[inds[0],b,cidx]; x=vs[ids]
            d=np.linalg.det(x)/6
            if d<=0: raise ValueError('nonpositive tetrahedron')
            total+=d;first+=d*x.sum(axis=0)/4;polys.append(ids)
    g=first/total
    ed={}
    for j,ids in faces.items():
        for a,b in zip(ids,ids[1:]+ids[:1]):ed.setdefault(tuple(sorted((a,b))),[]).append(j)
    if any(len(a)!=2 for a in ed.values()):raise ValueError('bad edge incidence')
    pe=np.array(sorted(ed),int); qe=np.array([ed[tuple(x)] for x in pe],int)
    assert len(vs)-len(ed)+len(faces)==2
    assert np.max(vs@n.T-1)<1e-7
    p=vs-g; q=n/(1-n@g)[:,None]
    return dict(n=n,vertices=vs,triples=tri,faces=faces,edges=pe,dual_edges=qe,
                tetrahedra=np.asarray(polys,int),g=g,volume=total,p=p,q=q,active=qh.vertices)

def bars(x,edges):
    """0D superlevel persistence of ||x||^2 on the continuous edge graph.
    Includes every positive float difference; consumers must state any cutoff.
    Returns [(depth, birth vertex, death edge, squared birth, squared death)].
    """
    sq=np.einsum('ij,ij->i',x,x)
    d=x[edges[:,1]]-x[edges[:,0]];dd=np.einsum('ij,ij->i',d,d)
    t=np.clip(-np.einsum('ij,ij->i',x[edges[:,0]],d)/dd,0,1)
    z=x[edges[:,0]]+t[:,None]*d;level=np.einsum('ij,ij->i',z,z)
    order=np.argsort(-level,kind='stable');parent=np.arange(len(x));birth=np.arange(len(x));out=[]
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    for k in order:
        a,b=map(int,edges[k]);ra,rb=find(a),find(b)
        if ra==rb:continue
        if (sq[birth[ra]],-birth[ra])<(sq[birth[rb]],-birth[rb]):ra,rb=rb,ra
        bi=int(birth[rb]);death=float(level[k]);dep=(float(sq[bi])-death)/float(sq[bi])
        if dep>0:out.append((dep,bi,[a,b],float(sq[bi]),death))
        parent[rb]=ra
    return sorted(out,reverse=True)

def properties(n,m):
    nt=n; vv=torch.linalg.solve(nt[m['triples']],torch.ones((len(m['triples']),3,1))).squeeze(-1)
    tet=vv[m['tetrahedra']];vol=torch.linalg.det(tet)/6
    g=(vol[:,None]*tet.sum(dim=1)/4).sum(dim=0)/vol.sum()
    p=vv-g; q=nt/(1-nt@g)[:,None]
    return p,q,g

def scores(x):
    A=x@x.T-np.sum(x*x,axis=1)[:,None];np.fill_diagonal(A,-np.inf)
    return np.max(A,axis=1),np.argmax(A,axis=1)

def optimize(inp,out,mu=1e-4,maxiter=700,eps=1e-7,archive_floor=1e-5):
    r=json.load(open(inp)) if str(inp).endswith('.json') else None
    if r is not None:v=np.array(r['n'])
    else:
        lines=Path(inp).read_text().splitlines();count,D=map(int,lines[0].split());v=np.array([list(map(int,line.split())) for line in lines[1:] if line.strip()],float)/D;assert len(v)==count and v.shape[1]==3
    m=geometry(v);shape=v.shape;calls=0;bestQ=float('inf');hist=[]
    def fg(flat):
        nonlocal calls,bestQ
        calls+=1;vv=flat.reshape(shape)
        try:m=geometry(vv)
        except (ValueError,AssertionError,QhullError):return 1e6,np.zeros_like(flat)
        p0,q0=m['p'],m['q'];Q=[b for b in bars(q0,m['dual_edges']) if b[0]>1e-12];P=[b for b in bars(p0,m['edges']) if b[0]>1e-12];pr=int(np.argmax(np.sum(p0*p0,1)));qr=int(np.argmax(np.sum(q0*q0,1)));exclude={qr}
        if Q:main=max(Q,key=lambda x:x[0]);exclude.add(main[1])
        ip=np.array([i for i in range(len(p0)) if i!=pr]);iq=np.array([i for i in m['active'] if i not in exclude]);pc,pw=scores(p0);qc,qw=scores(q0);wp=pw[ip];wq=qw[iq]
        z=torch.tensor(flat,requires_grad=True);p,q,g=properties(z.reshape(shape),m)
        cp=(p[ip]*(p[wp]-p[ip])).sum(1)/(p[ip]*p[ip]).sum(1);cq=(q[iq]*(q[wq]-q[iq])).sum(1)/(q[iq]*q[iq]).sum(1);guards=torch.cat((cp,cq));safe=torch.clamp(guards,min=eps);below=(guards-eps)/eps
        penalty=torch.where(guards>=eps,-torch.log(safe),-np.log(eps)-below+.5*below*below).sum()
        loss=mu*penalty
        if Q:
            u=main[1];a,b=main[2];d=q[b]-q[a];t=torch.clamp(-(q[a]@d)/(d@d),0,1);x=q[a]+t*d;dep=1-(x@x)/(q[u]@q[u]);loss=loss+dep
        loss.backward();val=float(loss.detach());grad=z.grad.detach().numpy()
        if not np.isfinite(val) or not np.isfinite(grad).all():return 1e6,np.zeros_like(flat)
        minp=float(np.min(pc[ip]/np.sum(p0[ip]**2,1)));minq=float(np.min(qc[iq]/np.sum(q0[iq]**2,1)));SU=[int(sum(qc[m['active']]<-1e-10)),int(sum(pc<-1e-10))];big=max((x[0] for x in Q),default=0.)
        rec=dict(call=calls,energy=val,Q=big,SU=SU,VEF=[len(p0),len(m['edges']),len(m['active'])],minp=minp,minq=minq,Pcount=len(P),Qcount=len(Q));hist.append(rec)
        if SU[1]==1 and SU[0]<=2 and len(m['edges'])<=249 and min(minp,minq)>archive_floor and not P and len(Q)<=1 and big<bestQ:
            bestQ=big;Path(out).write_text(json.dumps(dict(n=vv.tolist(),points=m['vertices'].tolist(),c=dict(V=len(p0),E=len(m['edges']),F=len(m['active']),S=np.where(qc<-1e-10)[0].tolist(),U=np.where(pc<-1e-10)[0].tolist(),P=P,Q=Q,volume=m['volume'],centroid=m['g'].tolist()),mu=mu,eps=eps,calls=calls),indent=2)+'\n')
        if calls%50==0 or big==0:print(rec,flush=True)
        return val,grad
    res=minimize(fg,v.ravel(),jac=True,method='L-BFGS-B',options={'maxiter':maxiter,'maxls':40,'maxcor':25,'ftol':1e-14,'gtol':1e-9})
    Path(out+'.history.json').write_text(json.dumps(hist,indent=2)+'\n');Path(out+'.last.json').write_text(json.dumps(dict(n=res.x.reshape(shape).tolist()),indent=2)+'\n');print('H_BARRIER_TERMINAL',res.success,str(res.message),'nit',res.nit,'calls',calls,'bestQ',bestQ,flush=True)

if __name__=='__main__':
    optimize(sys.argv[1],sys.argv[2],mu=float(sys.argv[4]) if len(sys.argv)>4 else 1e-5,maxiter=int(sys.argv[3]) if len(sys.argv)>3 else 1200,eps=float(sys.argv[5]) if len(sys.argv)>5 else 1e-7,archive_floor=float(sys.argv[6]) if len(sys.argv)>6 else 1e-7)
```

## Exact artifact receipts

| File | Bytes | SHA-256 |
|---|---:|---|
| `KL13_BARRIER2_G6.json` | 1508 | `88306141dfaddc23564cd5cd1e0f9addd1b98711f49564427380592f813a40cd` |
| `KL13_BARRIER2_G6_H.txt` | 8333 | `fb020854af52107be86d30198890842ff47ec1e8762b823ac899f529a60216b5` |
| `KL13_RETIRED84_H.txt` | 5962 | `ca9d91943a6cebc9853f4b79c1bc467df314e3d0ca2142cb41b722cc92bc972f` |
| `KL13_MIXED_G7.json` | 1757 | `6f53e7b0f9c3c665aaeb515a25d788021d5ae13ef3abf5aa112953d62ce37ecc` |
| `KL13_MIXED_G7_H.txt` | 9884 | `29c958ccb9e1c3918f25fb01723a62850ea94031bc7c63f2719947ef9045fa84` |
| `KL13_H80_G5.txt` | 1587 | `97bf66b9c4c75e8a2fc5d93367eeb7b735dbea71932b23b067b822d7add5525e` |
| `KL13_BARRIER2_G6_PYTHON_AUDIT.json` | 16753 | `09f971f7f7d355d20b922fb05e4b5863fed3a17f48e5ddc509959ea63eff85d3` |
| `KL13_RETIRED84_PYTHON_AUDIT.json` | 57378 | `48957d17fd1735a975906c3fab96742a9c3ea6b61308419896002ff8debe47c4` |
| `KL13_MIXED_G7_PYTHON_AUDIT.json` | 22935 | `c27768127f0ab759cbba3b1bbe1316b16be859d844d4364c2f3376a43be8573d` |
| `KL13_H80_G5_PYTHON_AUDIT.json` | 104305 | `007fa00ef43c9ac5114f87102e2900098e9f23a667e70b18200e055a5259beab` |
| `KL13_EXIT_BOUND.json` | 1308 | `709018dc84842753364333e0d331c7b11855c30ae6e86791b989ba6383b37f1f` |

Supplementary copy of the source, inputs, both audit families and receipts: [KL13 handoff archive](sandbox:/mnt/data/KL13_HANDOFF.zip). The inline source capsule is sufficient to reconstruct the four retained bodies and certificates without this archive.
