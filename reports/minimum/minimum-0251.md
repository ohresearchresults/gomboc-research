# minimum-0251

AI research report · 2026-09-26 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# H5_JOINT_SCHUR_FIVE_ARROW_AND_QUARTIC_SHEAR_REDUCTION_V1

## Result and scope

**The joint tangential-metric/shear problem admits a complete five-arrow reduction, and five is sharp on the literal actual-centroid H5 family.** The new reduction is over every SPD metric simultaneously, not a collection of fixed-G or fixed-shear controls. I also eliminated the tangential metric from the parent's normal-boundary formulation: for each fixed rational H5 shape, the complete U1 question becomes an explicit Boolean feasibility problem in the two unrestricted shear coordinates, using polynomial signs of degree at most four. Weak same-layer exits are retained.

An exact minimal five-arrow obstruction, with five rational SPD proper-subpacket witnesses and their full actual-inverse physical censuses, establishes sharpness. The geometry is the coordinator's existing shape A; the joint obstruction and the five physical metrics are new calculations. No genuine U1 or proper110 body was found. The quartic reduction was compiled and checked, but a global shear-plane CAD was **not** executed. Whole-H5 exclusion and the accepted bounds **34 <= C_min <= 622** remain unchanged. The inherited frontier is below lambda=3/5 outside the named macro/reflection and tubes. fileciteturn0file2L910-L919

## Input authority and completeness

I read the complete assignment fragment, both selected sources, and all 331389 bytes of the journal through EOF, including the branch memory and the entire literal parent. All three attached-file manifests matched:

```text
H5_CROSS_SPOKE_ELLIPSE_CAPS_AND_EXACT_SHEAR_CELLS_V1_proof.md
9833 bytes  e1102aa3d0a8d581e99aaad94ead3c50798d71cac91f834f3365338fa8643be4
h5_shear_cells.py.txt
9742 bytes  d4c753c4f64df7da26027452e6dcb528f690255841021c854a5a642bb0a5f89b
research-journal(20260926-192018).md
331389 bytes  324755e2de7748380af2980d935e57e997ec2f1b68f5daca24f2ca98c3cc5ef0
```

Parent identity: `minimum-0250`, SHA-256 `2cf87f1bc07e373e4dd87a52a48d1a91b98eb48ba17601cf28e76afe3e39c233`. I reproduced this digest exactly: take the journal's Markdown substring beginning at the parent's title through EOF, append one LF, and serialize `{'version':2,'result_markdown':text}` using `json.dumps({'version':2,'result_markdown':text},ensure_ascii=False,separators=(',',':'))`. The resulting envelope has 43879 bytes. Its three extracted source units also matched their advertised byte counts and hashes. There is no unresolved identity conflict or missing dependency for this handoff. Historical atlases were accepted as supplied research results, not independently replayed.

The parent already eliminates eta. I do not count that observation as new. The additions here are the **joint convex projection**, its sharp five-arrow alternative, and the explicit all-G quartic sign reduction. The literal geometry is seven basal vertices and three upper vertices; the nine maximal facet cycles and seventeen genuine edges are preserved in the complete source below. fileciteturn0file2L1044-L1076 fileciteturn0file2L1321-L1340

## 1. Complete joint convex cone and the sharp five-arrow theorem

### 1.1 Exact projection before choosing either G or shear

The theorem applies more generally to vertices `z_i=(x_i,h_i)` on two parallel planes `h_i in {0,1}`, at a fixed interior reference `g=(c,gamma)`, with `0<gamma<1`. The H5 application always uses the actual uniform volume centroid.

Write a metric, normalized by `tr G=1`, as

```text
M = [[G,b],[b^T,m]],       G>0,
f(G,b) = b^T G^-1 b,
m > f(G,b).
```

Thus `b=Gv` and `eta=m-f(G,b)`. For an arrow `e=(i,j)`, put

```text
a_i = x_i-c,   k_i=h_i-gamma,
delta_e=x_j-x_i,   sigma_e=h_j-h_i,
ell_e(G,b)=a_i^T G delta_e + (sigma_e a_i+k_i delta_e)^T b.
```

The original physical derivative is exactly

```text
D_e = ell_e + k_i sigma_e m.
```

For a same-layer arrow, its condition is `ell_e>=0`. For a cross-layer arrow, `c_e=-k_i sigma_e>0`; set `L_e=ell_e/c_e`. Its condition is `m<=L_e`.

Consequently, for **any finite selected packet J**, an SPD metric satisfying every original weak arrow exists if and only if there are `G>0`, `tr G=1`, and `b in R^2` satisfying

```text
ell_e(G,b) >= 0              for same-layer e in J,
L_e(G,b) > f(G,b)            for cross-layer e in J.       (1)
```

The cross inequalities in (1) are STRICT. Replacing them by weak inequalities would admit a singular normal boundary that need not lift. When J contains cross arrows, put

```text
r_J = min_cross (L_e-f)>0,
v=G^-1 b,   eta=r_J/2,   m=f+eta.
```

This constructs a genuine SPD metric satisfying all selected within-layer weak arrows and all selected cross-layer arrows strictly. If J has no cross arrow, choose any `m>f`.

### 1.2 Convexity, five-arrow completeness, and dual certificate

With `tr G=1`, the variables `(G,b)` have dimension four. Each same-layer condition in (1), intersected with `G>0`, is convex. Each cross condition is the open linear matrix inequality

```text
[[G,b],[b^T,L_e(G,b)]] > 0,
```

so it too is convex. Finite Helly in dimension four therefore gives the following theorem; no boundedness, conditioning hypothesis, or closure of the individual sets is required. The classical finite convex-set theorem used at this step is stated in the introduction of Frankl–Jung–Tomon's primary research paper. citeturn266368view0

**Five-arrow theorem.** For a fixed two-layer geometry and interior reference, a finite packet of original weak arrows is SPD-feasible if and only if every subpacket of at most five arrows is SPD-feasible.

The metrics witnessing the small subpackets may initially differ. Helly is exactly what promotes those separate witnesses to **one common physical metric** for the entire packet.

There is an equivalent negative certificate. Define

```text
A_e = sym((z_i-g)(z_j-z_i)^T).
```

If the packet is SPD-infeasible, some subpacket K with `|K|<=5` has nonnegative weights, not all zero, for which

```text
C = -sum_{e in K} w_e A_e  is PSD and nonzero.             (2)
```

To see the converse certificate existence, separate the open SPD cone from the polyhedral cone `{M: A_e:M>=0}`. The separator is a nonzero PSD matrix in the negative conical hull of the arrow tensors. Equation (2) contradicts SPD feasibility because `tr(MC)>0` but `tr(MC)=-sum w_e D_e<=0`.

Important boundaries: (2) need not be positive definite, nor have a uniform positive margin over a shape cell. The five-arrow theorem concerns **SPD metric feasibility**, not feasibility for arbitrary nonzero singular PSD metrics. A uniform multi-shape atlas may still need more than five rows in one certificate. At degenerate rational inputs I make no blanket rational-weight promise; the actual sharpness certificate below has positive integer weights and is PD.

For a complete rooted true-edge tree, these conditions are sufficient for U1: every selected arrow strictly increases squared norm, since the metric is SPD and the edge is genuine. All vertices flow to the root, which is the unique global norm maximum and hence strictly unstable. Every other vertex has its selected nonnegative exit. Thus for each fixed actual H5 shape,

```text
U1 exists
iff some rooted true-edge tree T has every five-subpacket SPD-feasible.
```

Literal enumeration gives 48790 rooted trees, with 501 compatible pairs, 4190 triples, 21859 four-subpackets and 73524 five-subpackets. These are raw labelled graph counts, not additions to any canonical registry.

### 1.3 Four-variable cubic inequalities and an all-G bounded-entry domain

Put

```text
G=[[a,c],[c,1-a]],  b=(u,w),
d=a(1-a)-c^2,
Q=(1-a)u^2-2cuw+aw^2.
```

Then (1) is the explicit four-variable system

```text
a>0,  d>0;
ell_e>=0                         for selected same-layer arrows;
d L_e-Q>0                        for selected cross arrows.        (3)
```

At fixed rational shape, the same-layer polynomials are affine and the cross polynomials have degree at most three. The apparent nonlinear inequalities define convex sets by the displayed LMI.

There is also a conditioning-free bounded-entry enclosure for every complete H5 U1 cone. The supplied cap identity bounds `m=Mzz` by `max_cross(r_i^T G r_i+d_e^T G d_e)`. fileciteturn0file0L31-L41 Here the raw horizontal vertices and their actual centroid lie in the unit triangle, `|h_i-gamma|>1/4`, and a basal-to-top displacement has squared Euclidean length at most `(1-lambda)^2+lambda^2<1`. Therefore

```text
0 < Mzz < 33,     ||b||^2 < 33,     tr G=1.               (4)
```

This is an all-G enclosure in **matrix entries**. It is not a lower eigenvalue bound, and does not bound the shear `v=G^-1 b` near singular G. Do not impose (4) when separately testing a within-layer-only subpacket: its unbounded b-domain must be retained for the five-arrow equivalence as stated. No covariance-normalized condition-number cap, S1 hypothesis, or reciprocal relaxation enters these results.

## 2. Five is sharp on an actual residual H5 geometry

Use the coordinator's shape A, which is below lambda=3/5 and outside the named macro/reflection and tiny tube:

```text
theta=(x,r,p,q,lambda)=(13/20,3/4,4/5,1/10,3/10).
```

The pre-existing source used this shape only for a fixed-G shear control. fileciteturn0file0L59-L63 Its literal rational vertices are

```text
0 (7/40,0,0)          1 (287/800,0,0)
2 (7/50,14/25,0)      3 (7/100,63/100,0)
4 (0,49/160,0)        5 (0,7/40,0)
6 (7/160,7/160,0)     7 (0,0,1)
8 (3/10,0,1)          9 (0,3/10,1).
```

Independent determinant integration in the new source gives

```text
Volume = 22241/240000,
g = (18537583/142342400, 13363403/71171200, 37841/88964).
```

Consider the five genuine arrows, in this order,

```text
0->6, 4->3, 5->7, 6->5, 9->4,
weights = (3,1,1,4,1).
```

For the actual centered arrow tensors, their negative weighted sum is exactly

```text
C = 1/227747840000 *
    [[  2643952766, -5433512387, -24157694400],
     [ -5433512387, 13427218908,  52816622400],
     [-24157694400, 52816622400, 227747840000]].
```

Its three leading principal minors are

```text
1321976383/113873920000
5977875711811661759/51869078624665600000000
67537319009374469/51869078624665600000000.
```

All are positive. Hence the five weak arrows are jointly impossible under **every nonzero PSD metric**, and in particular under every joint choice of SPD G, real shear and positive eta.

Every four-arrow deletion is nevertheless strictly feasible under a rational SPD metric. The table gives the six symmetric entries `(Mxx,Mxy,Mxz,Myy,Myz,Mzz)`, all divided by 1000. Each omitted arrow is negative and all four retained arrows are positive.

| Omitted arrow | Six integer metric entries | Actual strict (S,U,H) |
|---|---|---|
| 0->6 | (808,65,-2,190,-17,2) | (2,3,3) |
| 4->3 | (899,290,38,97,12,4) | (4,2,4) |
| 5->7 | (830,-100,150,130,-30,30) | (3,3,4) |
| 6->5 | (371,236,13,624,-26,6) | (3,3,4) |
| 9->4 | (777,293,-47,201,-58,22) | (2,4,4) |

Each full physical audit uses the actual inverse `N=M^-1`, all nine maximal facets, all seventeen true edges and all 68 primal/polar edge primitives. All five controls have **physical weak000 and 68 nonzero primitives**, giving 340 nonzero checks in total. The exact report regenerates every primitive, pole, inverse, strict equilibrium label and Schur coordinate. These are nonattaining physical controls, not U1 candidates.

This proves that a universal four-arrow substitute for the five-arrow theorem is false **inside the literal actual-centroid H5 family**, not just for formal vectors.

The packet lies in the complete rooted tree

```text
root 3;
0->6, 1->8, 2->3, 4->3, 5->7, 6->5, 7->8, 8->9, 9->4.
```

It is contained in exactly 81 raw labelled rooted trees: root counts `{1:9,2:18,3:36,7:9,8:9}`. All those cones are excluded at this geometry. This is a literal containment count, not a new whole-shape exclusion, a claimed nonoverlap with historical certificates, or a canonical-orbit subtraction.

## 3. Complete all-G elimination to quartic shear signs

### 3.1 The remaining planar problem

For each arrow define affine two-vectors in the unrestricted shear `v=(v1,v2)`:

```text
U_e(v)=a_i+k_i v,
W_e(v)=delta_e+sigma_e v.
```

Let

```text
C_e=U_e.W_e,
A_e=U_ex W_ex-U_ey W_ey,
B_e=U_ex W_ey+U_ey W_ex.
```

With `G=((1+t,u),(u,1-t))/2`, the projected derivative equals `(C_e+A_e t+B_e u)/2`; SPD means `t^2+u^2<1`. Each coefficient is a polynomial of degree at most two in shear. At eta=0 the selected constraints are same-layer `>=0` and cross-layer `>0`, exactly as required for positive-eta lifting.

For a triple J, let `F_J(v)` mean that these three mixed halfplanes meet the **open** G-disk. Finite Helly in dimension two gives the exact formula

```text
Phi_theta(v) = OR_{rooted trees T} AND_{J subset T, |J|=3} F_J(v),
U1 exists at shape theta  iff  EXISTS v in R^2: Phi_theta(v).       (5)
```

Checking triples together with the common disk includes every possible Helly obstruction: either three halfplanes, or the disk and at most two halfplanes. No common-G assumption is lost by (5). This is a complete joint reduction, not a claim that independently chosen G values themselves form a physical metric.

### 3.2 Exact mixed-halfplane predicate, including lower-dimensional strata

The executable `disk(rows,strict)` implements a quantifier-free predicate and returns a rational G witness at rational shear when one exists.

Temporarily close every halfplane and call their intersection P. If P is nonempty, its nearest point to the origin is one of: the origin; the perpendicular foot on one boundary line; or the intersection of two independent boundary lines. Test all these candidates, requiring squared norm **strictly less than one** and every closed inequality nonnegative.

At a surviving candidate q, consider its active rows. A small motion d must satisfy nonnegative active weak derivatives and positive derivatives for every active strict row. A complete finite direction list is the four signed coordinate axes and both perpendicular directions to each active nonzero normal. For each strict active row, test whether some direction in that list satisfies all active weak conditions and is positive for that row. If so, sum the selected directions. A sufficiently small exact rational step preserves inactive positive rows and the open disk while making all strict rows positive. If no such directions exist, that candidate cannot be perturbed appropriately.

Completeness follows by the nearest-point characterization and the generators of a planar polyhedral tangent cone. Full-plane and halfplane cones are covered by the signed axes; pointed cones and rays have boundary directions perpendicular to active normals. Constant zero rows, forced equalities, coincident lines, and tangencies to the excluded disk boundary are all retained. This resolves the mixed weak/strict predicate, not just its open two-dimensional sign cells.

### 3.3 All predicate changes are captured by degree-four polynomials

For each row and compatible pair, define

```text
N_i=A_i^2+B_i^2,                   T_i=N_i-C_i^2,
H_ij=A_i B_j-B_i A_j,
X_ij=B_i C_j-C_i B_j,              Y_ij=C_i A_j-A_i C_j,
I_ij=H_ij^2-X_ij^2-Y_ij^2,
F_ij=N_i C_j-C_i(A_i A_j+B_i B_j),
R_ijk=det [[C_i,A_i,B_i],[C_j,A_j,B_j],[C_k,A_k,B_k]].
```

The foot candidate uses `N_i>0`, `T_i>0`, and residual signs `F_ij`. The pair-intersection candidate uses `H_ij!=0`, `I_ij>0`, and residual signs `R/H`. Tangent-direction tests use only `A_i`, `B_i`, and `H_ij`. Thus the signs of `C,A,B,N,T,H,I,F,R` determine each `F_J`, even on zero strata.

The low degrees are structural, not generic degree-eight elimination bounds. Write the row tensor as

```text
sym(U_e W_e^T)=alpha_e vv^T+sym(v s_e^T)+K_e.
```

The quadratic parts are all proportional to `vv^T`. Moreover `vv^T` and every `sym(v s^T)` lie in a two-dimensional linear subspace. This cancels the degree-four-and-higher terms in the three-row determinant, so `deg R<=3`. The same rank-one structure gives `deg H<=3` and makes the Lorentz product `A_i A_j+B_i B_j-C_i C_j` have degree at most two. Consequently `deg F<=4`.

There are exact further factorizations, with `cross` the planar determinant:

```text
T_i = cross(U_i,W_i)^2,
I_ij = -4 cross(U_i,U_j) cross(U_i,W_j)
          cross(W_i,U_j) cross(W_i,W_j).
```

Every factor on the right is affine in shear. Thus `deg T<=2`, `deg I<=4`, and all required sign polynomials have degree at most four. These identities also hold when factors vanish identically.

The compiler instantiates (5) for the exact shape A. It produces 6364 tagged polynomials and 6192 distinct primitive polynomials including zero, with degree histogram

```text
zero:1, degree1:50, degree2:945, degree3:4189, degree4:1007.
```

Twelve tags are identically zero and are retained. It verifies all 34 square identities and all 501 four-affine-factor identities, 535 exact polynomial identities in total. Its rational predicate tests include twelve explicit mixed/degenerate disk cases, twenty independently checked positive projected rows from the five physical controls, and rejection of the full sharp packet at those control shears.

The 3332801-byte model contains the complete exact polynomial catalogue, orientation signs, compatible triples and all rooted trees. **It is a compiled complete reduction, not an evaluated global CAD or a claimed all-shear nonexistence result.** A sign-invariant decomposition must cover the whole real shear plane and its lower-dimensional strata; no guessed shear box or singular-G cutoff is licensed. Setting all selected flags strict gives the strict-escape variant with the same catalogue. Neither variant supplies S1 without a subsequent actual-inverse audit.

## 4. Executed reconstruction, pins, and continuation

The two exact units were executed normally and again in a fresh source-only directory. The three exact model/report files were byte-identical. The optional numerical locator was also executed on the pinned stack and regenerated the packet, all five rational proper-subpacket metrics and the integer stress. It found the packet at zero-based permutation position 481 after 4227 cached oracle calls, seed 20260926. Numerical negative margins were only discovery signals; the displayed rational matrices and exact assertions establish the claims.

Save the following three complete source blocks with a final LF. No parent file, journal, precomputed model, certificate array, or archive path is needed to reconstruct the new results.

```sh
python -B -S h5_joint5.py
python -B -S h5_joint_quartic.py
# Optional replay of numerical discovery:
OPENBLAS_NUM_THREADS=1 python -B h5_joint_discover.py
```

The exact units use CPython 3.13.5 and the standard library only, with assertions enabled. Discovery additionally uses NumPy 2.3.5 and SciPy 1.17.0, with one BLAS thread. Different numerical stacks need not reproduce locator choices; the exact fixtures and exact-unit outputs do not depend on the locator.

```text
SOURCE PINS
h5_joint5.py 7807
b31f42eca620bce96fe9e1fe7c962e029fe51eeee2d89dce06b1b7f826829ab7
h5_joint_quartic.py 7818
05489097eb195264f01b3137cc3a7da30898379d89720e94fea6a4edafbfe7d1
h5_joint_discover.py 3906
af2bd2c60b255f78a21dd58d25b9860fd52361c592de0b0e125e76085283b4bd

OUTPUT PINS
h5_joint5_report.json 46933
d2178961bbc7963390fd9eb0678849d68434b8b639321fd5a1abbbeda9cb6d53
h5_joint_quartic_model.json 3332801
f7314fd0929065ed47eb40f8765d1a722daf79b03539f1abab758481cfda814c
h5_joint_quartic_report.json 702
0e8e0c7afad057b7219b819930822865f54ca6d3f5e40930c0b6e0ccf4a2ef26
h5_joint_discovery_report.json 1018
0d868e5a02d88839f0f547249c940e2756b7fd7f30d8cad99edb1f2b18d2387d

TERMINAL MARKERS
H5_JOINT_FIVE_ARROW_SHARPNESS_EXACT_PASS
H5_JOINT_QUARTIC_REDUCTION_COMPILED_PASS
H5_JOINT_DISCOVERY_EXACT_RATIONALIZATION_PASS
```

The useful continuation is now joint rather than sliced: decide or geometrically cover the four-variable convex cubic packets, or perform exact sign decomposition for (5), starting with residual shapes outside the inherited exclusions. The factored circle-event polynomials can reduce the practical decomposition burden. A surviving complete tree, not merely a small packet, must be lifted with positive eta; a U1 metric must then receive its complete actual-inverse eta-pencil census. The exact minimal-five fixture rules out a proposed shortcut based on four-row compatibility alone. No full shape-region feasibility result, nonzero-PSD version of the general five-arrow bound, proper110 density result, global minimum improvement, or proof-assistant verification is asserted.

## 5. Complete runnable source

### h5_joint5.py

```python
"""H5 joint Schur cone, sharp five-arrow control; CPython 3.13.5, stdlib.
No U1 or proper110 witness, no whole-H5 exclusion.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
from pathlib import Path
from math import gcd,lcm
import hashlib,json

FACETS=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
        (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
EDGES=tuple(sorted({tuple(sorted((f[k],f[(k+1)%len(f)])))
                    for f in FACETS for k in range(len(f))}))
ARROWS=tuple(sorted(e for i,j in EDGES for e in ((i,j),(j,i))))
ADJ=tuple(tuple(j for a,j in ARROWS if a==i) for i in range(10))
EF=tuple(tuple(k for k,f in enumerate(FACETS) if i in f and j in f)
         for i,j in EDGES)
DUAL=tuple(sorted(e for i,j in EF for e in ((i,j),(j,i))))
THETA=('13/20','3/4','4/5','1/10','3/10')
PACKET=(1,12,17,19,31)
WEIGHTS=(3,1,1,4,1)
TREE=(1,5,7,12,17,19,24,29,31)
# Six entries xx,xy,xz,yy,yz,zz; divide every row by 1000.
PROPER=((808,65,-2,190,-17,2),(899,290,38,97,12,4),
        (830,-100,150,130,-30,30),(371,236,13,624,-26,6),
        (777,293,-47,201,-58,22))

def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def mv(M,a):return tuple(dot(r,a) for r in M)
def bil(a,M,b):return dot(a,mv(M,b))
def mat(r):
 a,b,c,d,e,f=r;return ((a,b,c),(b,d,e),(c,e,f))
def minors(M):
 a,b,c=M[0];_,d,e=M[1];_,_,f=M[2]
 return a,a*d-b*b,a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b

def inv(M):
 a,b,c=M[0];_,d,e=M[1];_,_,f=M[2];det=minors(M)[2]
 assert det>0
 N=tuple(tuple(x/det for x in r) for r in
         ((d*f-e*e,c*e-b*f,b*e-c*d),(c*e-b*f,a*f-c*c,b*c-a*e),
          (b*e-c*d,b*c-a*e,a*d-b*b)))
 assert all(sum(M[i][k]*N[k][j] for k in range(3))==int(i==j)
            for i in range(3) for j in range(3))
 return N

def body(theta=THETA):
 x,r,p,q,la=map(F,theta);s=1-la
 assert 0<x<1 and 0<r<1 and p>0 and q>0 and p+q<1 and 0<la<1
 B=((F(1,4),0),(1-3*x/4,0),(1-p,p),(q,1-q),(0,1-3*r/4),
    (0,F(1,4)),(F(1,16),F(1,16)))
 Z=tuple((s*a,s*b,F(0)) for a,b in B)+((F(0),F(0),F(1)),
       (la,F(0),F(1)),(F(0),la,F(1)))
 D=F(0);K=[F(0)]*3;supports=[]
 for f in FACETS:
  a,b,c=(Z[i] for i in f[:3]);n=cross(sub(b,a),sub(c,a));h=dot(n,a)
  assert n!=(0,0,0)
  assert all(dot(n,Z[j])==h if j in f else dot(n,Z[j])<h for j in range(10))
  supports.append((n,h))
  for k in range(1,len(f)-1):
   a,b,c=(Z[i] for i in (f[0],f[k],f[k+1]));d=dot(a,cross(b,c));D+=d
   for j in range(3):K[j]+=d*(a[j]+b[j]+c[j])/4
 g=tuple(a/D for a in K);assert D>0 and F(1,4)<g[2]<F(3,4)
 Q=tuple(tuple(a/(h-dot(n,g)) for a in n) for n,h in supports)
 assert len(Z)==10 and len(FACETS)==9 and len(EDGES)==17
 assert all(len(e)==2 for e in EF)
 return Z,g,Q,D/6

def tensors(Z,g):
 out=[]
 for i,j in ARROWS:
  a=sub(Z[i],g);b=sub(Z[j],Z[i])
  out.append(tuple(tuple((a[r]*b[s]+a[s]*b[r])/2 for s in range(3)) for r in range(3)))
 return tuple(out)

def census(Z,g,Q,M):
 assert min(minors(M))>0;N=inv(M);X=tuple(sub(z,g) for z in Z)
 P={(i,j):bil(X[i],M,sub(X[j],X[i])) for i,j in ARROWS}
 E={(i,j):bil(Q[i],N,sub(Q[j],Q[i])) for i,j in DUAL}
 U=tuple(i for i in range(10) if all(P[i,j]<0 for j in ADJ[i]))
 S=tuple(i for i in range(9) if all(E[i,j]<0 for a,j in DUAL if a==i))
 H=[];weak={}
 for (i,j),(a,b) in zip(EDGES,EF):
  vals=(P[i,j],P[j,i],E[a,b],E[b,a])
  if max(vals)<0:H.append((i,j))
  if max(vals)<=0 and 0 in vals:
   pp=next((X[k] for k,l in ((i,j),(j,i)) if P[k,l]==0),None)
   qq=next((tuple(x/bil(Q[k],N,Q[k]) for x in mv(N,Q[k]))
            for k,l in ((a,b),(b,a)) if E[k,l]==0),None)
   if pp is not None and qq is not None:assert pp==qq
   point=pp if pp is not None else qq
   kind='VF' if pp is not None and qq is not None else 'VE' if pp is not None else 'EF'
   weak.setdefault(point,{'kind':kind,'point':point,'edges':[]})['edges'].append((i,j))
   if kind=='VF':weak[point]['kind']='VF'
 assert len(S)+len(U)-len(H)==2
 return {'M':M,'N':N,'S':S,'U':U,'H':H,'counts':(len(S),len(U),len(H)),
         'weak':list(weak.values()),'zero_primitives':sum(v==0 for v in P.values())+sum(v==0 for v in E.values()),
         'primal':[(i,j,P[i,j]) for i,j in ARROWS],
         'polar':[(i,j,E[i,j]) for i,j in DUAL]}

def schur_check(Z,g,M):
 tr=M[0][0]+M[1][1];M=tuple(tuple(a/tr for a in row) for row in M)
 G=tuple(row[:2] for row in M[:2]);b=(M[0][2],M[1][2]);d=G[0][0]*G[1][1]-G[0][1]**2
 v=((G[1][1]*b[0]-G[0][1]*b[1])/d,(G[0][0]*b[1]-G[0][1]*b[0])/d)
 f=dot(b,v);eta=M[2][2]-f;assert d>0 and eta>0
 for i,j in ARROWS:
  a=sub(Z[i][:2],g[:2]);delta=sub(Z[j][:2],Z[i][:2]);k=Z[i][2]-g[2];sigma=Z[j][2]-Z[i][2]
  A=bil(a,G,delta)+dot(tuple(sigma*a[t]+k*delta[t] for t in range(2)),b)
  D=bil(sub(Z[i],g),M,sub(Z[j],Z[i]))
  if not sigma:assert D==A
  else:
   c=-k*sigma;assert c>0;L=A/c
   assert D/c==L-M[2][2]
   assert (d*L-(G[1][1]*b[0]**2-2*G[0][1]*b[0]*b[1]+G[0][0]*b[1]**2))==d*(L-f)
 return {'normalized_G':G,'b':b,'v':v,'eta':eta,'Mzz':M[2][2]}

def trees():
 ai={e:k for k,e in enumerate(ARROWS)};out=[]
 for es in combinations(EDGES,9):
  adj=[[] for _ in range(10)]
  for i,j in es:adj[i].append(j);adj[j].append(i)
  for root in range(10):
   p={root:root};queue=[root]
   for j in queue:
    for i in adj[j]:
     if i not in p:p[i]=j;queue.append(i)
   if len(p)!=10:break
   out.append((root,tuple(sorted(ai[i,p[i]] for i in range(10) if i!=root))))
 assert len(out)==48790 and len(set(out))==48790
 return out

def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [enc(v) for v in x]
 return x

def write(name,x):
 raw=(json.dumps(enc(x),sort_keys=True,indent=2)+'\n').encode();Path(name).write_bytes(raw)
 return {'file':name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}

def build():
 Z,g,Q,V=body();A=tensors(Z,g)
 C=tuple(tuple(-sum(w*A[k][i][j] for k,w in zip(PACKET,WEIGHTS)) for j in range(3)) for i in range(3))
 assert min(minors(C))>0 and C[2][2]==1
 den=lcm(*(a.denominator for row in C for a in row));CI=tuple(tuple(int(a*den) for a in row) for row in C)
 records=[]
 for omit,m in zip(PACKET,PROPER):
  M=mat(tuple(F(a,1000) for a in m));cc=census(Z,g,Q,M);P={(i,j):v for i,j,v in cc['primal']}
  assert all(P[ARROWS[k]]>0 for k in PACKET if k!=omit) and P[ARROWS[omit]]<0
  assert not cc['weak'] and cc['zero_primitives']==0 and len(cc['U'])>=2
  cc.update({'omitted_arrow':ARROWS[omit],'leading_minors':minors(M),
             'packet_values':[P[ARROWS[k]] for k in PACKET],'schur':schur_check(Z,g,M)})
  records.append(cc)
 TR=trees();assert (3,TREE) in TR and set(PACKET)<=set(TREE)
 contains=Counter(r for r,t in TR if set(PACKET)<=set(t))
 unique={k:set() for k in (2,3,4,5)}
 for r,t in TR:
  for k in unique:unique[k].update(combinations(t,k))
 out={'identity':'H5_JOINT_SCHUR_SHARP_FIVE_ARROW_V1','theta':THETA,'vertices':Z,
      'facets':FACETS,'edges':EDGES,'volume':V,'centroid':g,'poles':Q,
      'packet':[ARROWS[k] for k in PACKET],'weights':WEIGHTS,'stress':C,
      'integer_stress_scale':den,'integer_stress':CI,'stress_minors':minors(C),
      'containing_tree_root':3,'containing_tree':[ARROWS[k] for k in TREE],
      'raw_rooted_trees_containing_packet':dict(sorted(contains.items())),
      'proper_subpacket_controls':records,'rooted_trees':len(TR),
      'compatible_packet_counts':{k:len(v) for k,v in unique.items()},
      'scope':'Sharp five-arrow bound for full joint SPD cones. This actual minimal five-packet is not a complete U1 witness or a whole-body all-metric exclusion.'}
 print(json.dumps(write('h5_joint5_report.json',out),sort_keys=True))
 print('H5_JOINT_FIVE_ARROW_SHARPNESS_EXACT_PASS')
 return out
if __name__=='__main__':build()
```

### h5_joint_quartic.py

```python
"""Complete joint-G elimination to shear-plane polynomial signs.
Uses h5_joint5.py verbatim. Compiles a reduction, NOT a global CAD verdict.
All arithmetic and acceptance are exact; CPython 3.13.5 standard library.
"""
from h5_joint5 import *
from functools import reduce

# Sparse polynomials in the two shear coordinates.
def P(c=0):return {} if not c else {(0,0):F(c)}
def clean(p):return {e:c for e,c in p.items() if c}
def add(*ps):
 q={}
 for p in ps:
  for e,c in p.items():q[e]=q.get(e,F(0))+c
 return clean(q)
def scale(p,c):return clean({e:a*c for e,a in p.items()})
def mul(p,q):
 r={}
 for (i,j),a in p.items():
  for (k,l),b in q.items():r[i+k,j+l]=r.get((i+k,j+l),F(0))+a*b
 return clean(r)
def neg(p):return scale(p,-1)
def sq(p):return mul(p,p)
def deg(p):return max((sum(e) for e in p),default=-1)
def value(p,v):return sum((c*v[0]**i*v[1]**j for (i,j),c in p.items()),F(0))
def pcross(u,v):return add(mul(u[0],v[1]),neg(mul(u[1],v[0])))
def pdot(u,v):return add(mul(u[0],v[0]),mul(u[1],v[1]))

def projected_polys(theta=THETA):
 Z,g,Q,V=body(theta);vx={(1,0):F(1)};vy={(0,1):F(1)}
 uv=[];rows=[]
 for i,j in ARROWS:
  a=sub(Z[i][:2],g[:2]);d=sub(Z[j][:2],Z[i][:2]);k=Z[i][2]-g[2];sigma=Z[j][2]-Z[i][2]
  u=(add(P(a[0]),scale(vx,k)),add(P(a[1]),scale(vy,k)))
  v=(add(P(d[0]),scale(vx,sigma)),add(P(d[1]),scale(vy,sigma)))
  C=pdot(u,v);A=add(mul(u[0],v[0]),neg(mul(u[1],v[1])))
  B=add(mul(u[0],v[1]),mul(u[1],v[0]))
  uv.append((u,v));rows.append((C,A,B))
 return rows,uv

def disk(rows,strict):
 """Return rational (t,u) in t^2+u^2<1 satisfying C+A*t+B*u.
 Weak rows >=0, strict rows >0. None is an exact infeasibility verdict.
 """
 rows=[tuple(map(F,r)) for r in rows];strict=tuple(strict);assert len(rows)==len(strict)
 candidates=[(F(0),F(0))]
 for C,A,B in rows:
  N=A*A+B*B
  if N:candidates.append((-C*A/N,-C*B/N))
 for (C,A,B),(D,E,H) in combinations(rows,2):
  det=A*H-B*E
  if det:candidates.append(((B*D-C*H)/det,(C*E-A*D)/det))
 for q in candidates:
  margin=1-dot(q,q)
  if margin<=0:continue
  vals=[C+A*q[0]+B*q[1] for C,A,B in rows]
  if min(vals,default=F(0))<0:continue
  active=[i for i,x in enumerate(vals) if not x]
  need=[i for i in active if strict[i]]
  if not need:return q
  dirs=[(F(1),F(0)),(F(-1),F(0)),(F(0),F(1)),(F(0),F(-1))]
  for i in active:
   C,A,B=rows[i];dirs.extend(((-B,A),(B,-A)))
  dirs=[d for d in dirs if all(dot(rows[i][1:],d)>=0 for i in active)]
  chosen=[]
  for i in need:
   d=next((d for d in dirs if dot(rows[i][1:],d)>0),None)
   if d is None:break
   chosen.append(d)
  if len(chosen)!=len(need):continue
  d=(sum(x for x,y in chosen),sum(y for x,y in chosen))
  eps=min(F(1),margin/(4*(1+2*abs(dot(q,d))+dot(d,d))))
  for r,x in zip(rows,vals):
   der=dot(r[1:],d)
   if x>0 and der:eps=min(eps,x/(2*abs(der)))
  p=(q[0]+eps*d[0],q[1]+eps*d[1])
  assert dot(p,p)<1
  assert all(C+A*p[0]+B*p[1]>0 if s else C+A*p[0]+B*p[1]>=0
             for (C,A,B),s in zip(rows,strict))
  return p
 return None

def tests():
 cases=(
  ((),(),True),(((0,0,0),),(False,),True),(((0,0,0),),(True,),False),
  (((1,0,0),),(True,),True),(((-1,0,0),),(False,),False),
  (((-1,1,0),),(False,),False),(((F(-1,2),1,0),),(True,),True),
  (((0,1,0),(0,-1,0)),(False,False),True),
  (((0,1,0),(0,-1,0)),(True,False),False),
  (((0,1,0),(0,0,1),(0,-1,-1)),(False,False,True),False),
  (((0,1,0),(0,0,1),(0,-1,-1)),(False,False,False),True),
  (((F(-1,4),1,0),(F(1,4),-1,0),(0,0,1)),(False,False,True),True))
 for rows,strict,expected in cases:assert (disk(rows,strict) is not None)==expected
 rows,uv=projected_polys();Z,g,Q,V=body();checks=0
 for omit,m in zip(PACKET,PROPER):
  M=mat(tuple(F(a,1000) for a in m));v=schur_check(Z,g,M)['v']
  rs=[tuple(value(p,v) for p in r) for r in rows]
  assert disk([rs[k] for k in PACKET],[ARROWS[k][0]<7<=ARROWS[k][1] or ARROWS[k][1]<7<=ARROWS[k][0] for k in PACKET]) is None
  ks=[k for k in PACKET if k!=omit]
  point=disk([rs[k] for k in ks],[True]*len(ks));assert point is not None
  t,u=point;G=((F(1,2)*(1+t),u/2),(u/2,F(1,2)*(1-t)))
  for k in ks:
   i,j=ARROWS[k];Y=tuple(Z[i][h]-g[h]+(Z[i][2]-g[2])*v[h] for h in range(2))
   D=tuple(Z[j][h]-Z[i][h]+(Z[j][2]-Z[i][2])*v[h] for h in range(2))
   assert bil(Y,G,D)>0
   checks+=1
 return {'formal_mixed_disk_cases':len(cases),'independent_positive_projected_rows':checks,
         'sharp_five_packets_rejected_at_control_shears':len(PROPER)}

class Catalog:
 def __init__(self):self.polys=[()];self.ids={():0};self.tags={}
 def put(self,name,p):
  if not p:self.tags[name]=(0,1);return
  D=lcm(*(c.denominator for c in p.values()));terms=sorted((i,j,int(c*D)) for (i,j),c in p.items())
  h=reduce(gcd,(abs(c) for i,j,c in terms));sgn=1 if terms[-1][2]>0 else -1
  key=tuple((i,j,c//h*sgn) for i,j,c in terms)
  if key not in self.ids:self.ids[key]=len(self.polys);self.polys.append(key)
  self.tags[name]=(self.ids[key],sgn)

def compile_model(theta=THETA):
 rows,uv=projected_polys(theta);TR=trees();triples=sorted({t for r,ks in TR for t in combinations(ks,3)})
 pairs=sorted({p for t in triples for p in combinations(t,2)})
 assert len(triples)==4190 and len(pairs)==501
 cat=Catalog();N=[];T=[];pairdata={};identities=0
 for i,(C,A,B) in enumerate(rows):
  n=add(sq(A),sq(B));t=add(n,neg(sq(C)))
  assert t==sq(pcross(*uv[i])) and deg(t)<=2;identities+=1;N.append(n);T.append(t)
  for name,p in zip(('C','A','B','N','T'),(C,A,B,n,t)):cat.put(name+str(i),p)
 for i,j in pairs:
  C,A,B=rows[i];D,E,F1=rows[j]
  H=add(mul(A,F1),neg(mul(B,E)))
  X=add(mul(B,D),neg(mul(C,F1)));Y=add(mul(C,E),neg(mul(A,D)))
  I=add(sq(H),neg(sq(X)),neg(sq(Y)))
  ui,di=uv[i];uj,dj=uv[j]
  factors=(pcross(ui,uj),pcross(ui,dj),pcross(di,uj),pcross(di,dj))
  assert all(deg(p)<=1 for p in factors)
  product=P(-4)
  for p in factors:product=mul(product,p)
  assert I==product and deg(I)<=4 and max(map(deg,(H,X,Y)))<=3;identities+=1
  ndot=add(mul(A,E),mul(B,F1));L=add(ndot,neg(mul(C,D)))
  assert deg(L)<=2
  Fi=add(mul(N[i],D),neg(mul(C,ndot)))
  Fj=add(mul(N[j],C),neg(mul(D,ndot)))
  assert max(deg(Fi),deg(Fj))<=4
  cat.put(f'H{i},{j}',H);cat.put(f'I{i},{j}',I)
  cat.put(f'F{i},{j}',Fi);cat.put(f'F{j},{i}',Fj)
  pairdata[i,j]=(H,X,Y)
 for i,j,k in triples:
  H,X,Y=pairdata[i,j];C,A,B=rows[k]
  R=add(mul(C,H),mul(A,X),mul(B,Y));assert deg(R)<=3
  cat.put(f'R{i},{j},{k}',R)
 degree_counts=Counter(max((i+j for i,j,c in p),default=-1) for p in cat.polys)
 assert max(degree_counts)<=4
 model={'identity':'H5_COMPLETE_JOINT_U1_QUARTIC_SHEAR_REDUCTION_V1','theta':theta,
        'arrows':ARROWS,'strict_cross':[k for k,(i,j) in enumerate(ARROWS) if (i<7)!=(j<7)],
        'polynomials':cat.polys,'tags':cat.tags,'triples':triples,'rooted_trees':TR,
        'scope':'Quantifier-free sign reduction in two real shear variables, all tangential SPD metrics and weak same-layer strata. Not an executed CAD or whole-shape exclusion.'}
 raw=(json.dumps(enc(model),sort_keys=True,separators=(',',':'))+'\n').encode()
 Path('h5_joint_quartic_model.json').write_bytes(raw)
 report={'model_bytes':len(raw),'model_sha256':hashlib.sha256(raw).hexdigest(),
         'rooted_trees':len(TR),'compatible_triples':len(triples),'compatible_pairs':len(pairs),
         'tagged_polynomials':len(cat.tags),'distinct_primitive_polynomials_including_zero':len(cat.polys),
         'primitive_degree_histogram':dict(sorted(degree_counts.items())),
         'zero_polynomial_tags':sum(v[0]==0 for v in cat.tags.values()),
         'exact_square_and_four_linear_factor_identities':identities,'tests':tests(),
         'verdict':'COMPLETE_REDUCTION_COMPILED_NOT_GLOBAL_CAD_EXECUTED'}
 print(json.dumps(write('h5_joint_quartic_report.json',report),sort_keys=True))
 print(json.dumps(report,sort_keys=True));print('H5_JOINT_QUARTIC_REDUCTION_COMPILED_PASS')
 return report
if __name__=='__main__':compile_model()
```

### h5_joint_discover.py

```python
"""Optional deterministic numerical locator, not proof.
CPython 3.13.5 / NumPy 2.3.5 / SciPy 1.17.0; one BLAS thread.
The literal exact proof inputs remain in h5_joint5.py.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
from h5_joint5 import *
import numpy as np
from scipy.optimize import linprog
Z,g,Q,V=body();AT=tensors(Z,g)
AE=tuple(tuple(M[i][j] for i,j in ((0,0),(0,1),(0,2),(1,1),(1,2),(2,2))) for M in AT)
A=np.array(AE,dtype=float)*[1,2,2,1,2,1];A/=np.linalg.norm(A,axis=1)[:,None]
def full(x):return np.array(mat(x))
def vv(u):return np.array([u[0]**2,2*u[0]*u[1],2*u[0]*u[2],u[1]**2,2*u[1]*u[2],u[2]**2])
INIT=np.array([vv(v/np.linalg.norm(v)) for v in np.array(
 [(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,-1,0),(1,0,1),(1,0,-1),(0,1,1),(0,1,-1)],dtype=float)])
CACHE={}
def test(ks):
 ks=tuple(sorted(ks))
 if ks in CACHE:return CACHE[ks]
 planes=INIT.copy()
 for it in range(80):
  rows=np.r_[A[list(ks)],planes]
  res=linprog(np.r_[np.zeros(6),-1.],A_ub=np.c_[-rows,np.ones(len(rows))],
      b_ub=np.zeros(len(rows)),A_eq=[[1,0,0,1,0,1,0]],b_eq=[1],
      bounds=[(None,None)]*7,method='highs')
  if not res.success:raise RuntimeError(res.message)
  ev,U=np.linalg.eigh(full(res.x[:6]))
  if res.x[-1]<-1e-8 or ev[0]>res.x[-1]-1e-9:break
  planes=np.r_[planes,vv(U[:,0])[None,:]]
 out=(float(min(ev[0],res.x[-1])),res.x[:6].tolist());CACHE[ks]=out;return out

def main():
 TR=trees();rng=np.random.default_rng(20260926)
 for count,idx in enumerate(rng.permutation(len(TR))):
  root,original=TR[int(idx)];ks=list(original)
  if test(ks)[0]>1e-8:raise RuntimeError('full-tree numerical candidate; exact audit required')
  for k in rng.permutation(ks):
   js=[j for j in ks if j!=k]
   if test(js)[0]<-1e-8:ks=js
  if len(ks)==5 and test(ks)[0]<-1e-8 and all(test([j for j in ks if j!=k])[0]>1e-8 for k in ks):break
  if count>=1000:raise RuntimeError('no locator output; not an exclusion')
 else:raise RuntimeError('no locator output; not an exclusion')
 assert tuple(ks)==PACKET and root==3 and count==481
 rational=[]
 for omit in ks:
  m=test([j for j in ks if j!=omit])[1]
  for den in (100,1000,10000,100000,1000000):
   mm=tuple(F(round(x*den),den) for x in m);M=mat(mm)
   vals=[sum(mm[h]*AE[k][h]*(2 if h in (1,2,4) else 1) for h in range(6)) for k in ks if k!=omit]
   if min(minors(M))>0 and min(vals)>0:break
  else:raise RuntimeError('exact rationalization failed')
  rational.append(mm)
 assert rational==[tuple(F(a,1000) for a in m) for m in PROPER]
 # Locate a PD nonnegative stress; numerical output is checked exactly below.
 B=-np.array([full(list(map(float,r))) for r in AE]);planes=np.array([B[:,i,i] for i in range(3)])
 for it in range(100):
  pp=planes[:,ks]
  rr=linprog([0]*len(ks)+[-1],A_ub=np.c_[-pp,np.ones(len(pp))],b_ub=np.zeros(len(pp)),
       A_eq=[[1]*len(ks)+[0]],b_eq=[1],bounds=[(0,None)]*len(ks)+[(None,None)],method='highs')
  if not rr.success:raise RuntimeError(rr.message)
  w=rr.x[:-1];C=np.einsum('i,ijk->jk',w,B[list(ks)]);ev,U=np.linalg.eigh(C)
  if ev[0]>1e-8:
   for den in (10,20,50,100,200,500,1000,3000,10000,30000,100000):
    wi=tuple(round(x*den) for x in w)
    C=mat(tuple(-sum(wi[j]*AE[k][h] for j,k in enumerate(ks)) for h in range(6)))
    if min(wi)>0 and min(minors(C))>0:break
   else:raise RuntimeError('exact stress rounding failed')
   break
  planes=np.r_[planes,np.einsum('i,kij,j->k',U[:,0],B,U[:,0])[None,:]]
 else:raise RuntimeError('no PD proposal; not a feasibility result')
 assert wi==WEIGHTS
 out={'theta':THETA,'seed':20260926,'tree_permutation_position':count,'root':root,
      'tree':original,'packet':ks,'exact_metric_entries6':rational,'exact_weights':wi,
      'oracle_calls':len(CACHE),'status':'EXACT_CHECKED_OUTPUT_NOT_NUMERICAL_EXCLUSION'}
 print(json.dumps(write('h5_joint_discovery_report.json',out),sort_keys=True))
 print('H5_JOINT_DISCOVERY_EXACT_RATIONALIZATION_PASS')
if __name__=='__main__':main()
```

Convenience copy: [complete sources, compiled model, exact reports, and this handoff](sandbox:/mnt/data/h5_joint_capsule.zip). The inline sources above are the durable recovery capsule; this link is not a dependency.
