# material-c3baf42e94e9

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# COORD_TRUNCATED_CUBE_FACE_CAP_FALSE_SMALL_LOSS_V1

## Status and purpose
A coordinator-derived exact nonwinner family and a search-objective diagnostic, NOT a new Gömböc or a record. It demonstrates that a squared fullpoint escape deficit can approach zero while EVERY actual vertex, facet and edge remains a strict equilibrium. The family stays uniformly three-dimensional and well scaled; the pathology is disappearing facets and clustering features, not only an extreme affine aspect ratio. Accepted record remains C622.

## Exact family and complete analytic proof
For rational 0<t<=1/2 let K_t be the convex hull of the 24 signed permutations of (1,1,1-t) and the six points +/-(1+t)e_i. All signs are independent. The 24-point truncated cube has six octagonal faces and eight corner-cut triangular faces. Each new axis point lies beyond just its corresponding octagon and inside every other old support, including the corner cuts because 1+t<3-t. The actual facets of K_t have the following normalized support normals q, with q.x<=1:

- 24 long cap triangles: q=(sigma e_i+t tau e_j)/(1+t), i!=j, sigma,tau in{-1,1}.
- 24 short cap triangles: q=(sigma e_i+a(tau e_j+kappa e_k))/(1+t), {i,j,k}={1,2,3}, a=t/(2-t), independent signs.
- Eight corner-cut triangles: q=(sigma,tau,kappa)/(3-t).

The cap planes remain supports when all six peaks are present: substituting another peak gives at most t or a for a noncorresponding cap plane, both below1; corner planes contain every peak strictly. The old vertices, listed triangle cycles and these planes therefore give actual V=30,E=84,F=56,C=168, with no coplanar refinement diagonals. The body is centrally symmetric and has exact filled centroid0. Its volume is

V(t)=8+8t-(16/3)t^3.

Indeed remove eight corner tetrahedra of volume t^3/6 from the cube, and add six pyramids of height t over octagons of area4-2t^2.

Every physical vertex is strictly unstable. All 24 old vertices have the same squared radius s=3-2t+t^2, so the dot escape from one to any other is -half their squared separation. The largest dot escape from an old vertex to a peak on one of its long coordinates is (1+t)-s=-(1-t)(2-t)<0; the short-coordinate case is 1-t^2-s=-2+2t-2t^2<0. Negative-sign cases are smaller. From an axis peak, every old vertex has aligned coordinate at most1, giving dot escape at most -t(1+t)<0; every other peak also has negative escape.

Every facet is strictly stable. By sign/permutation symmetry it suffices to check three representatives. A corner-cut plane foot is the relative-interior triangle barycenter. A long cap has apex (1+t,0,0) and base endpoints (1,1,+/-(1-t)); its foot is a convex combination of the apex and base midpoint with base weight b=t(1+t)/(1+t^2), strictly between0 and1. A short cap has base endpoints (1,1,1-t),(1,1-t,1), and its analogous base weight is b=2t(1+t)/((2-t)^2+2t^2). This is strictly between0 and1 because 4-6t+t^2>0 throughout0<t<=1/2. Hence all56 facets have relative-interior feet.

Every actual edge is a strict saddle, without appealing to an unverified index count. Instability of both endpoints makes the perpendicular foot fall strictly between them. For adjacent support planes n.x=h_n and m.x=h_m, the interior foot of each facet lies strictly inside the other halfspace. These two inequalities are exactly the two strict normal-cone primitives h_m||n||^2-h_n(n.m)>0 and h_n||m||^2-h_m(n.m)>0. Thus all four saddle primitives are positive. There are no weak-only equilibria. For the entire parameter interval the exact census is

(S,U,H)=(56,30,84), weak-only=(0,0,0).

## Small fullpoint escape is not proximity to a winner
For either the physical vertices or the actual centered-polar vertices define the angular fullpoint escape

e_i=max_{j!=i} x_i.(x_j-x_i)/(||x_i|| ||x_j-x_i||),

or its radial version e_i=max_{j!=i} x_i.(x_j-x_i)/||x_i||^2. In both clouds EVERY e_i<0, since every node is a strict maximum of the corresponding polytope. Nevertheless every row has e_i>=-t for both normalizations:

- At an old physical vertex, swap a long and short coordinate of the same signs. Its dot escape is -t^2 and the step has squared length2t^2.
- At a physical peak use an aligned old vertex. Its angular escape is -t/sqrt(2-2t+2t^2), and its radial escape is -t/(1+t).
- At a long polar cap normal flip its small signed coordinate. Its angular escape is -t/sqrt(1+t^2), radial -2t^2/(1+t^2).
- At a short polar cap normal flip one small signed coordinate. Its angular escape is -a/sqrt(1+2a^2), radial -2a^2/(1+2a^2).
- At a corner polar normal use a compatible long cap normal. The dot escape is -t/(3-t)^2; row norm sqrt(3)/(3-t) and step norm at least1/(3-t) give angular escape >=-t/sqrt(3). Radial escape is -t/3.

The old physical angular/radial bounds follow directly from squared row radius s>=9/4 and the displayed dot/step values. All the stated escapes are >=-t for0<t<=1/2.

After omitting one designated root in each cloud, 29+55=84 rows remain. The zero-target squared hinge objective satisfies

0<M_0=sum_i max(-e_i,0)^2<=84t^2 ->0,

while the exact counts never change. For a FIXED positive target gamma the correct statement is instead

84 gamma^2 < M_gamma=sum_i max(gamma-e_i,0)^2 <=84(gamma+t)^2.

Thus a fixed positive target prevents literal zero loss, but an arbitrary absolute small-loss threshold is still not a certificate.

## General objective/count threshold
For any full-dimensional convex polyhedron with its ACTUAL interior reference point, built from distinct actual vertices and distinct maximal-facet polar vertices, a strict unstable vertex or strict stable facet gives e_i<0 in its respective cloud; a weak such feature gives e_i=0. Each extra strict or weak extremum not omitted as the single cloud root contributes at least gamma^2 to M_gamma, strictly more for a strict extremum. Consequently

M_gamma >= gamma^2[(S-1)+(U-1)],

and the analogous bound includes any extra weak S/U features. If the omitted root in each cloud is selected as an argmin of e, it is strict: a maximum-radius point always has strictly negative escapes to every other distinct point. Therefore the rigorous threshold M_gamma<gamma^2 rules out additional strict AND weak S/U extrema. Actual hull, mass, distinct maximal faces, sign precision and edge checks remain necessary for accepting a construction; a floating objective or duplicate triangulated facets is not a substitute. In the current lead search gamma=1e-5 and losses around4e-10 do NOT meet this threshold1e-10. Likewise free-vertex gamma=.001 and loss about6e-6 do NOT meet1e-6.

## Exact recovery dependency and observed verification
Complete immutable parent: figure-0395,42825bytes,SHA2569fc14dd9e08f3f635aaab511cc93ca8219cc1b84ded8926c38cbabee87da3f86, read cursor0 through eof:true. It contains the entire standalone RECOVER_RL04.py,21536bytes,SHA4ee2e1affe6b26674edb33d204d059b3627026faaa77895e781a8870abc52487. Recover its literal script and run `python -B -S RECOVER_RL04.py PARENT_DIRECTORY`. No originating sandbox or Library item is needed. The present addition needs exactly RL04_CENTER.py22965bytes,SHAa0af63a1d7de9c872cb35b2c134da0eb788e1f0287fb4ddc33534d6fd83d7ef7, checked before import.

Save the complete code fence below, including its final newline, as LOSS_COUNTEREXAMPLE.py,2999bytes,SHA58e2d95fd31dca4cad04885429651d768353cba0a94779b021e04e8b59baae77. Execute under CPython3.13.5 standard library, assertions enabled:

`python -B -S LOSS_COUNTEREXAMPLE.py PARENT_DIRECTORY NEW_OUTPUT_DIRECTORY`

The code performs independent complete A/B actual hull/incidence/filled-centroid/every-feature audits and a separate56-positive-centered-tetrahedron mass check on t=1/10,1/100,1/1000,1/10000. It also verifies exact rational squared angular and radial bounds for all30+56 rows, symmetry, volume formula and zero primitive counters. The general interval proof above is analytic; four examples alone would not establish it.

Observed output receipts:
D10.json16832bytes,SHA726501f40ae38dac37316a1c27e2424f7777d1377616d6cf27114c0caf5f5918.
D100.json19039bytes,SHA8c2bb085e80f67d16d0c501e9dd597de986f2e52db125fb3026db395d250ceba.
D1000.json21074bytes,SHAae139dbef7181a27e82a755ab46439112e27e8d64c322ff1bbb8a5e2e4b61841.
D10000.json23233bytes,SHA3299c49314f3c52ebb0de0fd0599b378f6ab4d92db4ba816b954ee8304389391.
LOSS_COUNTEREXAMPLE_REPORT.json80337bytes,SHA26c957b7ab65f79b45d7f7794f064715e066b7287c72eec3e7b5831d127bdfd9.
Minimal centered denominator/max-coordinate bit costs respectively4/4,7/7,10/10,14/14. Every body has C168, not a sub-floor search.
Terminal: COORD_FALSE_SMALL_LOSS_FOUR_RATIONAL_CONTROLS_AB_MASS_ALL_FEATURES_PASS.

```python
#!/usr/bin/env python3
"""Rational, well-scaled false-small-loss family; independent hull/mass/features.
python -B -S LOSS_COUNTEREXAMPLE.py PARENT_DIRECTORY NEW_OUTPUT_DIRECTORY
All four specimens are nonwinner method controls, not target constructions.
"""
import sys,hashlib,importlib.util
from pathlib import Path
from fractions import Fraction as Q
from itertools import product,permutations
assert __debug__ and len(sys.argv)==3
p=Path(sys.argv[1])/'RL04_CENTER.py';b=p.read_bytes();assert len(b)==22965 and hashlib.sha256(b).hexdigest()=='a0af63a1d7de9c872cb35b2c134da0eb788e1f0287fb4ddc33534d6fd83d7ef7'
spec=importlib.util.spec_from_file_location('rl04_parent',p);r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
out=Path(sys.argv[2]);out.mkdir(exist_ok=False)
report={'identity':'COORD_TRUNCATED_CUBE_FACE_CAP_FALSE_SMALL_LOSS_V1','dependency_result':'figure-0395','specimens':{}}
for D in (10,100,1000,10000):
 t=Q(1,D);P=set()
 for small in range(3):
  for signs in product((-1,1),repeat=3):P.add(tuple(signs[k]*(D-1 if k==small else D)for k in range(3)))
 for i in range(3):
  for sign in (-1,1):P.add(tuple(sign*(D+1)if k==i else 0 for k in range(3)))
 assert len(P)==30
 a,b,rep=r.build(sorted(P),D)
 assert (rep['V'],rep['E'],rep['F'])==(30,84,56)and all(len(f)==3 for f in a['faces'])
 assert rep['own']['counts']==[56,30,84]and rep['own']['weak']==[0,0,0]and rep['own']['zeros']==[0,0,0]
 assert a['centroid']==(0,0,0)and a['moment']==(0,0,0)
 assert a['volume']==8+8*t-Q(16,3)*t**3
 assert {r.mul(p,-1)for p in a['P']}==set(a['P'])
 QQ=[r.mul(row[:3],Q(1,row[3]))for row in a['H']]
 rep['witnesses']={}
 for name,X in [('physical',a['P']),('centered_polar',QQ)]:
  W=[]
  for i,x in enumerate(X):
   A=r.dot(x,x);valid=[]
   for j,y in enumerate(X):
    if i==j:continue
    delta=r.sub(y,x);dot=r.dot(x,delta);B=r.dot(delta,delta)
    assert dot<0 # EVERY node is a strict maximum of its corresponding polytope.
    if dot+t*A>=0 and dot*dot<=t*t*A*B:valid.append((Q(dot*dot,A*B),j,dot,B))
   assert valid
   ratio,j,dot,B=min(valid);W.append(dict(row=i,witness=j,dot=dot,row_norm2=A,step_norm2=B,angular_deficit_squared=ratio,radial_deficit=-dot/A))
  rep['witnesses'][name]=W
 rep['parameter_t']=t;rep['volume_formula']='8+8t-(16/3)t^3';rep['zero_target_squared_loss_upper']=84*t*t;rep['positive_target_loss_lower_factor']=84;rep['positive_target_loss_upper_factor']='84*(gamma+t)^2'
 report['specimens'][str(D)]=rep
 data=r.pack(rep);(out/('D'+str(D)+'.json')).write_bytes(data)
 print('FALSE_SMALL_LOSS_EXACT_PASS',D,'VEF',[rep[k]for k in ('V','E','F')],'strict',rep['own']['counts'],'bits',rep['cost'],'bytes',len(data),'sha256',hashlib.sha256(data).hexdigest(),flush=True)
data=r.pack(report);(out/'LOSS_COUNTEREXAMPLE_REPORT.json').write_bytes(data)
print('LOSS_COUNTEREXAMPLE_REPORT.json',len(data),hashlib.sha256(data).hexdigest(),flush=True)
print('COORD_FALSE_SMALL_LOSS_FOUR_RATIONAL_CONTROLS_AB_MASS_ALL_FEATURES_PASS',flush=True)
```
