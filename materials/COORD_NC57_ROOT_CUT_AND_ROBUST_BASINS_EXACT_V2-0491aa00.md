# material-0491aa00d730

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# NC57 rooted escape cuts and robust polar basins: exact source V2

## Identity, dependency and status
This is a new exact analysis of the unchanged NC57 C372_ALT_FULL_G4 and C378_ALT_POLY_G6 bodies. It is not a new polyhedron or a new own110 construction. Canonical own110 remains C622.

Complete exact input dependency: immutable NC57 result figure-0398, 73935 bytes, SHA256 b6c84be62ea56d1c11575d4d6309563f525d734f79b0ad2a299f0b7abd2ccdd3. Its full literal RECOVER_NC57.py source capsule reconstructs all 37 sources and the exact reports. This parent was read completely from cursor0 through eof with unchanged SHA in this coordinator turn. No originating sandbox is needed.

Input reports:
- proof/C372_ALT_FULL_G4/REPORT.json: 14190 bytes, SHA256 639b7dd56caf48ee99f1175e20b1f305100dc0fb3f75440dd20aba8df57b4cb5.
- proof/C378_ALT_POLY_G6/REPORT.json: 18534 bytes, SHA256 fc46fb08252486d5c2474d70c6834b2f4849f8de25bcf18ccb059a7aa9ced661.

All graph indices below are the literal REPORT point or face rows, NOT fresh Qhull facets, C384 ancestry, or C622 controls. Own-centred polar generators are q_f=n_f/(h_f-n_f.g), where g is the exact filled-solid centroid in the accepted report. This code validates support incidences and uses the accepted exact centroid; it does not claim a new independent hull/mass audit.

## Rooted graph bottleneck and exact cut certificate
For distinct nonzero vectors w_i define A_ij=w_i.(w_j-w_i)/||w_i||^2 for i!=j. Fix root r. Let b_i be the maximum over paths i->r of the minimum arc value on the path. Then mu=min_{i!=r} b_i equals min over nonempty B not containing r of max_{i in B,j outside B} A_ij.

Proof: any path starting in B exits B, so its bottleneck is no larger than the largest outgoing cut arc. Conversely reverse widest-path Dijkstra constructs a parent tree with all arcs at least mu. For B={i:b_i=mu}, every outside j has b_j>mu (the root has infinite capacity), so A_ij>mu would contradict b_i>=min(A_ij,b_j). Thus every outgoing arc is <=mu, with equality attained by a tree exit. The source verifies the full tree, settling order, each root-path capacity, and matching cut. Forty independent tiny directed graphs are also exhaustively checked over every nonempty root-excluded cut. This is an application of the max-min path/cut relation, not a claim to a new general graph theorem.

If r has largest norm, its arrows to all other distinct vectors are negative, because 2 w_r.(w_j-w_r)=||w_j||^2-||w_r||^2-||w_j-w_r||^2<0. Every positive escape strictly increases norm. A positive rooted tree excludes all other radial maxima. Applied to physical vertices this excludes other U; applied to own-centred polar generators it excludes other S. A new winning body would still require the stipulated complete exact hull/mass/strict-and-weak all-feature audits.

Exact results:
- C372 physical root59, mu=254521626473941809914957188738192/2317821673856362250481526238826466121 (about0.00010981070258544609). Polar root REPORT107, mu=-453944373204782266946937907098561493/4995640447241095882811290198239401026 (about-0.09086810349921773). Minimising polar cut has47 face rows; its unique maximum outgoing arc is REPORT31->32.
- C378 physical root50, mu=585096233350674605200505777476471901557390057800/7184866671923788812281431938464093475357051997634759 (about0.00008143452899927115). Polar root REPORT16, mu=-323970214553940750783974311468999526153302787099772195668727/4138127498452181142904411605020113165139823975229704791612330 (about-0.07828908477931579). Minimising polar cut has58 face rows; its unique maximum outgoing arc is REPORT125->124.

Every cut row, parent, settling order and exact rational capacity is deterministically reproduced in the outputs. These fixed-geometry negative cuts are not global impossibility results.

## Robust two-stable-equilibria exclusion
A further scoped geometric result survives arbitrary incidence and redundancy changes in the same labelled own-centred polar-generator family. Allow each coordinate of each q_i to change by at most eps, keep the origin interior of their convex hull, and add or delete no generators. The new physical body is the polar of this hull; when discussing homogeneous own-centroid bodies, these coordinates must be measured about that body's actual filled centroid, not a fixed old reference centre.

For i in B,j outside B, write f_ij=q_i.(q_j-q_i). For perturbations a,b in [-eps,eps]^3,
 f'_ij <= f_ij+eps(||q_j-2q_i||_1+||q_i||_1)+3 eps^2/4.
The quadratic remainder in each coordinate is a*b-a^2 <= eps*|a|-a^2 <= eps^2/4. The source checks that every upper bound is strictly negative. It also checks, for the old largest-norm root r outside B and every i in B,
 ||q'_r||^2-||q'_i||^2 >= ||q_r||^2-||q_i||^2-2eps(||q_r||_1+||q_i||_1)-3eps^2 >0.
Choose a largest-norm perturbed generator in B. Against every other distinct generator inside B its radial arrow is strictly negative; against every generator outside B the cut bound is negative. It is therefore an exposed radial maximum. The norm-gap bound places the global largest-norm generator outside B, giving a second distinct exposed radial maximum. Coincident redundant generator labels do not create extra equilibria and do not invalidate these two separated geometric points. Thus the physical polar has at least two strict stable equilibria. No assumption of preserved triangulation, facets being nonredundant, or preserved adjacency is used.

The exact certified radii are:
- C372: eps=21039/1000000=0.021039. At this radius the maximum cut bound is negative and every root-versus-cut norm gap is positive. The limiting next grid step is the sufficient norm-gap bound, not the cut bound.
- C378: eps=31347/1000000=0.031347. The next grid step fails the sufficient cut bound.
These are largest successful radii only for this explicit sufficient bound on the 1/1000000 grid, not sharp basin radii or exact distances to own110. They are NOT raw physical-vertex displacement bounds. Different own-centred charts, new/deleted polar generators, or larger deformations are outside this exclusion. The full rational bounds and attaining pairs are in the regenerated JSON.

## Reconstruction, verification and observed receipts
Use CPython3.13.5, standard library only, assertions enabled. No numerical package, optimisation seed, rounding, or unpreserved checkpoint is required. The finite self-test seed is explicitly913731; robustness grid denominator1000000.

First reconstruct the parent using its complete immutable capsule:
 python -B -S RECOVER_NC57.py NC57_SOURCE 4
Save the complete source block below as ROOT_CUT_EXACT_V2.py. Then:
 python -B -S ROOT_CUT_EXACT_V2.py NC57_SOURCE/proof/C372_ALT_FULL_G4/REPORT.json ROOT_CUT_V2_C372.json
 python -B -S ROOT_CUT_EXACT_V2.py NC57_SOURCE/proof/C378_ALT_POLY_G6/REPORT.json ROOT_CUT_V2_C378.json

Observed terminal lines:
 COORD_ROOT_CUT_EXACT_PASS 64 124 0.00010981070258544609 -0.09086810349921773 21039/1000000
 COORD_ROOT_CUT_EXACT_PASS 65 126 8.143452899927115e-05 -0.07828908477931579 31347/1000000

Exact source/output bytes and SHA256:
- ROOT_CUT_EXACT_V2.py:4932,3f97a294ba0d1f8cfb2a3a945c2b0236951627d14921acbaa282e9545a75c2d8.
- ROOT_CUT_V2_C372.json:18046,a19370985e4dd0858c0f6a33dbc7a24cade3461df6aef67b0e9fa913d3bf3b0b.
- ROOT_CUT_V2_C378.json:26212,a5d0a85aa32861b7bf70a322fbe0ad11d5a8e29926cb91562ebf954442dfee5b.
Hash these three files after execution and compare exactly. JSON is sort_keys=True,separators=(',',':'),one trailing newline. A hash identifies bytes; the full source and full immutable exact input dependency above supply them.

## Complete ROOT_CUT_EXACT_V2.py
```python
#!/usr/bin/env python3
"""Exact rooted radial-escape bottleneck / outgoing-cut dual certificates.
Stdlib only. Usage ROOT_CUT_EXACT.py REPORT.json OUTPUT.json
Input is a complete NC57 REPORT; all points/facet normals and centre are rational.
For exact defining identity see input hash in output. Graph labels are REPORT rows.
"""
import sys,json,hashlib,itertools
from pathlib import Path
from fractions import Fraction as Q

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def mat(W):
 return [[None if i==j else dot(a,sub(b,a))/dot(a,a) for j,b in enumerate(W)]for i,a in enumerate(W)]
def widest(A,root):
 n=len(A);cap=[None]*n;par=[None]*n;done={root};order=[root]
 for i in range(n):
  if i!=root:cap[i]=A[i][root];par[i]=root
 while len(done)<n:
  k=max((i for i in range(n)if i not in done),key=lambda i:(cap[i],-i));done.add(k);order.append(k)
  for i in range(n):
   if i not in done:
    c=min(A[i][k],cap[k])
    if c>cap[i]:cap[i]=c;par[i]=k
 return cap,par,order

def certificate(W):
 A=mat(W);root=max(range(len(W)),key=lambda i:dot(W[i],W[i]));cap,par,order=widest(A,root)
 ids=[i for i in range(len(W))if i!=root];mu=min(cap[i]for i in ids);B=[i for i in ids if cap[i]==mu];outside=[i for i in range(len(W))if i not in B]
 cut=max(A[i][j]for i in B for j in outside);assert cut==mu
 ranks={i:k for k,i in enumerate(order)}
 assert all(ranks[par[i]]<ranks[i]for i in ids)
 assert min(A[i][par[i]]for i in ids)==mu
 assert all(A[root][j]<0 for j in ids)
 for i in ids:
  k=i;v=None
  while k!=root:
   w=A[k][par[k]];v=w if v is None else min(v,w);k=par[k]
  assert v==cap[i]
 return dict(root=root,mu=str(mu),mu_float=float(mu),cut=B,cut_max=str(cut),parents=par,settle_order=order,capacities=[None if x is None else str(x)for x in cap],cut_bridges=[[i,j]for i in B for j in outside if A[i][j]==mu])

def selftest():
 # Independent exhaustive enumeration of all outgoing cuts on tiny directed graphs.
 import random
 r=random.Random(913731);cases=0
 for n in range(3,8):
  for _ in range(8):
   A=[[None if i==j else Q(r.randrange(-31,32),r.randrange(1,10))for j in range(n)]for i in range(n)]
   root=n-1;cap,par,order=widest(A,root);mu=min(cap[:-1]);brute=None
   for bits in range(1,1<<(n-1)):
    B=[i for i in range(n-1)if bits>>i&1];c=max(A[i][j]for i in B for j in range(n)if j not in B)
    brute=c if brute is None else min(brute,c)
   assert mu==brute;cases+=1
 return cases

def robust_basin(W,cert):
 # Same labelled generator family; origin must remain interior of its hull.
 # Independent componentwise perturbations bounded by eps.
 B=cert['cut'];outside=[j for j in range(len(W))if j not in B];r=cert['root']
 def l1(a):return sum(abs(x)for x in a)
 cross_data=[(dot(W[i],sub(W[j],W[i])),l1(sub(W[j],tuple(2*x for x in W[i])))+l1(W[i]),i,j)for i in B for j in outside]
 gap_data=[(dot(W[r],W[r])-dot(W[i],W[i]),2*(l1(W[r])+l1(W[i])),i)for i in B]
 def extrema(e):
  c=max((f+e*t+3*e*e/4,i,j)for f,t,i,j in cross_data)
  g=min((f-e*t-3*e*e,i)for f,t,i in gap_data)
  return c,g
 def passes(k):
  c,g=extrema(Q(k,1000000));return c[0]<0<g[0]
 assert passes(0)
 lo=0;hi=1
 while passes(hi):lo=hi;hi*=2
 while hi-lo>1:
  mid=(lo+hi)//2
  if passes(mid):lo=mid
  else:hi=mid
 assert lo>0 and passes(lo) and not passes(lo+1)
 e=Q(lo,1000000);c,g=extrema(e);c2,g2=extrema(Q(lo+1,1000000))
 return dict(eps=str(e),eps_float=float(e),grid_denominator=1000000,cut=B,root=r,
  max_cross_bound=str(c[0]),max_cross_pair=[c[1],c[2]],min_root_norm_gap_bound=str(g[0]),min_root_gap_index=g[1],
  next_grid_max_cross_bound=str(c2[0]),next_grid_min_root_norm_gap_bound=str(g2[0]),
  scope='Same labelled own-centred polar generators, componentwise displacement at most eps, origin interior; redundancy and incidence changes allowed; no additional or deleted generators. Not a raw physical vertex displacement bound.')

def main(src,dst):
 raw=Path(src).read_bytes();o=json.loads(raw);P=[tuple(map(Q,p))for p in o['points']];g=tuple(map(Q,o['centroid']))
 X=[sub(p,g)for p in P];pol=[]
 for f in o['faces']:
  a=P[f[0]];n=None
  for i,j in itertools.combinations(f[1:],2):
   t=cross(sub(P[i],a),sub(P[j],a))
   if any(t):n=t;break
  assert n is not None
  h=dot(n,a)
  if dot(n,g)>h:n=tuple(-v for v in n);h=-h
  assert all(dot(n,p)<=h for p in P) and all(dot(n,P[i])==h for i in f)
  h-=dot(n,g);assert h>0;pol.append(tuple(v/h for v in n))
 out=dict(input_sha256=hashlib.sha256(raw).hexdigest(),test_cases=selftest(),primal=certificate(X),polar=certificate(pol))
 out['polar_robust_basin']=robust_basin(pol,out['polar'])
 Path(dst).write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
 print('COORD_ROOT_CUT_EXACT_PASS',len(P),len(pol),out['primal']['mu_float'],out['polar']['mu_float'],out['polar_robust_basin']['eps'])
if __name__=='__main__':main(*sys.argv[1:])
```
