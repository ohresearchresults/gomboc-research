# minimum-0077

AI research report · 2026-09-16 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# MIRROR_BELT_ALL_AFFINE_METRICS_U_GE2_V1

## Determination

**The entire affine-metric orbit of the supplied algebraic mirror-belt family is excluded from homogeneous joint110. Every member has at least two strict unstable vertices for every SPD metric, including metrics on unused-shadow zero walls.** This is not just preservation of the previously displayed 222 chamber.

More strongly, the exclusion holds for every genuine centred polyhedron with the same literal true-edge graph in a specified closed thirty-coordinate vertex box of radius **1/512**. No reflection symmetry or moment-rank assumption is required inside that box. All invertible affine images are covered. Thus the theorem includes nonsymmetric realizations satisfying the stated geometric bounds, not merely the isolated algebraic root or its one-parameter continuation.

The proof consists of **131 literal nonnegative integer separators**, their independently checked reflected versions, **262 positive-definite 3×3 matrices**, and **786 strictly positive interval-enclosed leading minors**. They exclude **all 60,000 rooted weak-escape spanning trees**, namely all ten rootings of all 6,000 true-edge spanning trees. The metric is completely unrestricted. The certificates also give a uniform negative-arrow bound in the fixed coordinate chart.

**The global assertion that every bare-rank-deficient E17 shape is incompatible with110 remains unresolved.** No classification of all nonsymmetric rank-deficient strata is asserted. The accepted global bounds and canonical register remain `V≥10,F≥9,C≥34` and `632/52585`; no complete global type or registered root orbit is removed. The supplied parent distinguishes that register from mass-rank controls.

## 1. Authority and the interval repair

The immutable authority is **minimum-0075**, exactly **33797 bytes / SHA-256 17b392631f5a612ddcf377f1d2c5f478d5abcdf45652178d512fdf449e09de43**. Its full payload and complete source were read. The compact UTF-8 JSON envelope authenticates with that SHA; the payload's terminal newline is not added during this authentication. No mathematical, incidence, or object-identity conflict was found.

Current journal input: `research-journal(20260916-174724).md`, **4970774 bytes / 83514c81c0783bed0ca853aacf52c3a5d5d4b887d36c774b186084ed90b4659e**. The current synthesis and relevant correction were read before using the old proposal.

The completed object remains literally **E17_SECOND_MOMENT_KERNEL_ALGEBRAIC_CANDIDATE_V1**, notwithstanding the word CANDIDATE in its immutable name. I recovered and executed the canonical wrapper. It reproduced the corrected source, report and transcript pins:

| Inherited item | Bytes | SHA-256 |
|---|---:|---|
|recover_second_flux.py|8275|196b043688488f2887f3451d74e1444f0ff86bbd65455eb08b4689637ebb0ecb|
|failed direct-interval source|12269|f1ceeba379143b62cc8318924f3da9a6254cce4f319c87095fe23c883e880735|
|second_flux_verified.py|12560|fa1609e1456b10b406660567fdd6d7b01e4c67c9ce31c46280116b87187a1191|
|second_flux_candidate.json|89160|3f737edbca23e4c645fe60879b1c22ff48cfa94229f2361a29c6c70d38390881|
|repaired_replay.log|464|87395e798900390ac8b7a8beda1bb7e2e8e042acad156e84fdde57dcb89f0a34|

The exact repair is retained: for the full b interval the residual is enclosed using `A F(CENTER,b0)+A ∂_bF(CENTER,B)(b−b0)`, rather than repeated natural-interval substitution into `F(CENTER,b)`. The equations, root box, parameter interval and rounded preconditioner are unchanged. The old natural-interval failure is not reused as nonexistence evidence. The journal supplies the completed algebraic-kernel proof beyond interval zero containment.

The new main proof is mechanical, not another audit of mass rigidity. It uses actual centred vertices and genuine edges. The inherited rank-eight fact identifies the exceptional stratum to which the new exclusion applies.

## 2. Complete continuous geometric domain

Let P be a genuine full-dimensional convex polyhedron with its own uniform-volume centroid at0. Label its ten actual vertices x0,…,x9. Its seventeen true edges are exactly

~~~text
E=[[0,2],[0,4],[0,7],[1,3],[1,4],[1,7],[2,3],[2,5],[2,8],
   [3,6],[3,9],[4,5],[4,6],[5,6],[7,8],[7,9],[8,9]].
~~~

For the parent and its realization cell, the full maximal-facet cycles and vertex incidences are

~~~text
F=[[4,5,2,0],[4,1,3,6],[4,6,5],[5,6,3,2],
   [7,0,2,8],[7,9,3,1],[7,8,9],[8,2,3,9],[0,7,1,4]];
I=[[0,4,8],[1,5,8],[0,3,4,7],[1,3,5,7],[0,1,2,8],
   [0,2,3],[1,2,3],[4,5,6,8],[4,6,7],[5,6,7]].
~~~

No polygon diagonals are inserted as true edges. These local labels are not canonical C34 IDs and are not TREE ordinals.

Define the following integer table C:

~~~text
C=[
[ 653290,-1206585,       0],
[ 653290,  366279,       0],
[-395286,-1206585,       0],
[-852265, 1657820,       0],
[ 653290, -158009, 1048576],
[-320944, -268251,  938333],
[-700769, 1322602,  410514],
[ 653290, -158009,-1048576],
[-320944, -268251, -938333],
[-700769, 1322602, -410514]].
~~~

The closed coordinate hypothesis is

`|x_i,k−C_i,k/1048576|≤1/512`, for all ten vertices and all three coordinates.       (B)

**C is the centre of a box, not a proposed rational polyhedron.** It is not used in place of true coplanarity, true volume centring, or genuine vertices. Every realization covered by the theorem must actually have the stated true-edge graph and actual centre. The separator proof is valid for all coordinates in (B), so every genuine realization in that box is covered even when it has no symmetry.

### Theorem

For every P satisfying these premises and every symmetric positive-definite M,

`U(P,M)≥2`.

Consequently no such P, and no invertible affine image of such P with uniform density, has joint110 under its physically reciprocal pair `M,N=M⁻¹`. No upper bound on the condition number is imposed.

## 3. Complete proof, including mechanical zero walls

For a directed true edge i→j set

`D_ij=x_iᵀM(x_j−x_i)`,
`B_ij=x_i(x_i−x_j)ᵀ+(x_i−x_j)x_iᵀ`.

Then `tr(M B_ij)=−2D_ij`. For each listed certificate the nonnegative integer weights w produce

`B=Σ_(i→j) w_ij B_ij`.

The complete source below proves, on the entire closed box (B),

`B11>2/3`, `det B[{1,2},{1,2}]>7/5`, `det B>1`, `tr B<64`,
`Σw_ij≤17`.                                                               (C)

Indices in these minor inequalities are ordinary 1-based matrix indices. Sylvester's criterion gives B positive definite. Thus the arrows in that certificate cannot all satisfy D_ij≥0 for any nonzero PSD M, in particular for any physical SPD M. These B matrices are separator matrices built from actual vertex expressions, not purported physical facet moments.

All coefficients are literal: the 131 rows in DATA contain 451 positive integer entries, none greater than9. Arc2j is the forward direction of E[j] as printed, and arc2j+1 its reverse. For example, the first certificate uses `4→0`, `0→7`, `5→4` with respective weights1,1,2.

The permutation `R=(0,1,2,3,7,8,9,4,5,6)` preserves E. Each certificate and its R-image is checked **independently on the full nonsymmetric box**, giving262 matrices. The proof does not assume that an unknown realization is fixed by this permutation.

For completeness, the verifier enumerates every nine-edge subset of the seventeen-edge graph. A connected subset on ten vertices is a spanning tree. Exactly6,000 such subsets occur. Each is oriented towards each of the ten literal roots. The resulting60,000 directed masks are distinct; every one contains the full arrow support of at least one verified certificate. All roots0,…,9 are covered, with6,000 trees per root. No subtree classifier, optional-shadow graph, mechanical sampling or canonical-catalogue alias is involved.

Now orient every true edge i→j for which D_ij≥0. A weak arrow still has **strict norm growth**:

`x_jᵀMx_j−x_iᵀMx_i=2D_ij+(x_j−x_i)ᵀM(x_j−x_i)>0`.

Therefore this directed graph is acyclic, even when D_ij=0. Its sinks are exactly the vertices with every incident D_ij<0. Because the true edge rays generate the tangent cone, these are strict unstable vertices of the genuine polyhedron.

If there were only one sink, select an outgoing arrow at every other vertex. Acyclicity forces every selected path to terminate at that sink, so the nine selected arrows form a rooted spanning tree. The complete certificate cover excludes it. Hence there are at least two strict unstable vertices.

This proof directly includes every unused-shadow equality stratum. It does not require perturbation to a generic metric, a lower eigenvalue cutoff, or a boundary count inferred from an interior chamber.

### Quantitative form

Let λ1≤λ2≤λ3 be the eigenvalues of a certificate matrix B. From (C),

`λ1=det B/(λ2λ3)>4/(tr B)²>1/1024`.

Therefore `Σw_ij D_ij<−tr(M)/2048`. Since the sum of the weights is at most17, **every one of the60,000 rooted spanning trees contains an arrow with**

`D_ij<−tr(M)/34816`.                                                       (Q)

This is a uniform strict tree-obstruction bound in the specified coordinate chart. It is not asserted to be an affine-invariant numerical margin or a uniform margin for every individual unstable vertex. No optimality of the box radius or certificate count is claimed.

## 4. Application to the unchanged algebraic mirror-belt family

For a fully explicit reconstruction, let `p=(a,c,m,d,e)` lie in the coordinatewise radius `2^-30` box about

`(1.715701158033858,−0.1467378366871057,0.2967491976190772,−4.188209982907966,−0.6681749617245179)`.

Every displayed decimal is the same exact rational input as in the parent. Let `b∈1/2+[-2^-42,2^-42]`, and put H=−d−e. The upper normals and supports are

`n0=(0,−1,1), n1=(a,1/b,1), n2=(c,m,1), n3=(d,e,1)`,
`h0=h1=h2=1, h3=H`.

The lower four planes are their z reflections with the same supports; facet8 is x≤0. In the literal vertex labels,

`v0=(0,−1,0), v1=(0,b,0), v2=(−1,−1,0), v4=(0,0,1), v7=(0,0,−1)`;

v3 is the z=0 intersection of planes1 and3; v5 is the intersection of upper planes0,2,3; v6 is the intersection of upper planes1,2,3; v8 and v9 are the z reflections of v5 and v6. These are precisely the parent constructions, with the complete F/E/I lists of Section2.

For each upper facet let g_i and R_i be its actual raw first and second uniform-area moments. Write κ for the four signed3×3 cofactors of the matrix with rows1,g_x,g_y. With actual volume centroid o=(o_x,o_y,0), define hhat_i=h_i−n_i·o. The exact family is the unique p in the specified box solving

~~~text
Σκ_i n_ix g_iz=0;
Σκ_i n_iy g_iz=0;
Σκ_i h_i g_iz=0;
Σκ_i hhat_i (R_i)_xz=0;
Σκ_i hhat_i (R_i)_yz=0.
~~~

The actual centred poles, centres and moments are `q_i=n_i/hhat_i`, `c_i=g_i−o`, `T_i=R_i−g_ioᵀ−og_iᵀ+ooᵀ`. The complete kernel is the unchanged

`ν=(hhat0κ0,hhat1κ1,hhat2κ2,hhat3κ3,−hhat0κ0,−hhat1κ1,−hhat2κ2,−hhat3κ3,0)`.

The inherited repaired contraction proof establishes existence and uniqueness for every b in the entire closed interval. Reflection and the five exact equations prove the null identity; the nonzero8×8 minor proves `rank[Φ;c;T]=8`. This is not a near-zero-residual inference.

The new verifier independently integrates **all nine actual polygonal facets throughout the full six-parameter box**, including points not satisfying the rank equations. Each polygon is triangulated only for integration. For a triangle with vertices u,v,w and s=u+v+w, its actual mean is s/3 and its second moment is `(ssᵀ+uuᵀ+vvᵀ+wwᵀ)/12`. Its area-to-normal factor is obtained from the oriented cross product divided by `2||n_i||²`. Summing these factors a_i gives

`Vol(P)=Σa_i h_i/3`, `o=Σa_i h_i g_i/(4 Vol(P))`.

The source checks all strict nonincidences and convex turns. The exact incidences follow identically from the plane solves, reflection, and the stated constants; interval containment of zero is only a sanity check. The listed supporting facets form a closed connected polyhedral sphere, so they are the complete hull boundary. Thus the moment integrals are of the actual body, not an assumed mesh with hidden additional facets.

The resulting centred-vertex enclosure obeys the stronger bound

`max_i,k |(v_i−o)_k−C_i,k/1048576|<2^-20`,

well inside the mechanical radius2^-9. This covers the **whole original geometric parameter box**, hence the whole isolated rank-eight curve, with its endpoints. No equation, root interval or parent moment has been replaced.

Finally, every invertible linear map L sends actual centroid, centres and moments to `Lo,Lc_i,LT_iLᵀ`, while poles transform by `L^-T`. Consequently the bare moment rank is unchanged. Euclidean mechanics on `L(P−o)` is mechanics on `P−o` with `M=LᵀL`, `N=L^-1L^-T`. The theorem above therefore excludes110 throughout the entire affine orbit, not merely among reflection-preserving or bounded-condition metrics.

### Sharpness of U≥2 on this family

The inherited exact map and reciprocal pair are preserved:

~~~text
L0=[[10,3,2],[0,1,3],[0,0,1/10]], det L0=1;
M0=[[100,30,20],[30,10,9],[20,9,1301/100]];
N0=[[491/10,-2103/10,70],[-2103/10,901,-300],[70,-300,100]].
~~~

The completed, corrected journal capsule establishes class222 on the entire parameter enclosure: stable facets0,5; unstable vertices2,4; saddle edges(4,6),(7,8), with all162 unequal shadows strict. Its recovery was reproduced in this run. Thus U=2 is attained, and the new all-metric lower bound cannot be improved to U≥3 on this family. These are not newly invented metric objects or new110 witnesses.

## 5. What was tried, what changed, and what remains

I attacked the full six-entry metric problem rather than restricting to metrics commuting with the reflection. Floating-point linear programming was used only to propose small nonnegative combinations of true-edge shadow forms. The final131 coefficient rows were frozen as small integers; all positivity and coverage claims were then reconstructed using exact rational interval arithmetic, with no optimizer in the proof.

The successful route is stronger than an exclusion derived from the bare-rank equations: it works throughout a larger actual-coordinate box, including potentially full-rank and nonsymmetric realizations. Therefore it provides a geometric reason why the known rank-deficient control has extra unstable equilibria. It does **not** establish that rank deficiency itself is that reason for every shape.

All ten local unstable-root alternatives, with every possible stable-facet choice and every unused-shadow sign pattern, are excluded on the stated continuous domain. There is no canonical ID assignment and no subtraction from the632-type or52585-root register: other realizations of the same combinatorial type outside the certified affine-geometric neighbourhood have not been covered.

The exact residual global question is whether a rank-deficient genuine E17 body outside this excluded affine-geometric class can have U=1 and S=1 under one reciprocal SPD pair. Neither a global classification of its moment-null strata nor a counterexample to the rank-conditioned110 prohibition was obtained. The supplied algebraic family no longer offers an untested fixed-geometry metric route: leaving this excluded class requires a substantive shape change, not another affine-metric search.

## 6. Complete recovery capsule

Save the complete source below as `mirror_metric_exclusion.py`, UTF-8/LF with one final LF. **CPython3.13.5, standard library only, assertions enabled.** No journal file, parent report, coefficient download, optimizer, random seed or external geometry is an input. The source contains all131 certificates, the exact graph, the entire coordinate box, and the independent full-parent-box inclusion calculation.

~~~sh
python -S mirror_metric_exclusion.py > mirror_metric_exclusion.log
~~~

A separate cold run with `PYTHONHASHSEED=9173` reproduced the same JSON and log byte for byte. The source was then extracted from the complete prepared result_markdown and executed in another directory, again reproducing the same output bytes. It constructs every directed tree rather than requiring a hidden catalogue. Its JSON records every certificate's exact interval minors, all coverage counts and the complete parameter-box inclusion. The decimal integer stream of sorted rooted masks, one per LF-terminated line, has **647680 bytes / 87dde0001610087b1d10a0ad4604edfbfdc48a7888930d47d35ee8c6af67c15f**; this is a supplemental pin, not a substitute for its in-source enumeration.

| New artifact | Bytes | SHA-256 |
|---|---:|---|
|mirror_metric_exclusion.py|11663|8fa232cde279335aaebffc732db080f6c7becf89cede4acf7531e8b351f49019|
|mirror_metric_exclusion.json|145415|e884bd684fea824c9bc6ad35b4ef6d5f4417c4a44f9f55a93e7f83e2255ae785|
|mirror_metric_exclusion.log|480|daf7387e0f06c6d8c88d39a577f3e8cf80ccf8a967fc1a7ccd7b7263796b632d|

Observed full terminal transcript:

~~~text

[Encoded source block omitted; the code in this passage is incomplete.]

SOURCE 11663 8fa232cde279335aaebffc732db080f6c7becf89cede4acf7531e8b351f49019
~~~

Supplementary copies: complete source (`mirror_metric_exclusion.py`), exact report (`mirror_metric_exclusion.json`), observed log (`mirror_metric_exclusion.log`). The following literal source, rather than these files or their hashes alone, is the durable certificate.

```python
"""MIRROR_BELT_ALL_AFFINE_METRICS_U_GE2_V1.
CPython 3.13.5, standard library; run python -S mirror_metric_exclusion.py.
All coefficients, geometry and graph inputs are literal. No optimizer or seed.
Parent minimum-0075:
17b392631f5a612ddcf377f1d2c5f478d5abcdf45652178d512fdf449e09de43.
Parent repaired source: 12560 bytes,
fa1609e1456b10b406660567fdd6d7b01e4c67c9ce31c46280116b87187a1191.
The parent's root equations and boxes are not changed. The new theorem uses
only genuine edges and centred vertices and hence applies beyond that curve.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib,json
assert __debug__
CNUM=[[653290, -1206585, 0], [653290, 366279, 0], [-395286, -1206585, 0], [-852265, 1657820, 0], [653290, -158009, 1048576], [-320944, -268251, 938333], [-700769, 1322602, 410514], [653290, -158009, -1048576], [-320944, -268251, -938333], [-700769, 1322602, -410514]]
CDEN=1048576
RADIUS=F(1,512)
E=[[0, 2], [0, 4], [0, 7], [1, 3], [1, 4], [1, 7], [2, 3], [2, 5], [2, 8], [3, 6], [3, 9], [4, 5], [4, 6], [5, 6], [7, 8], [7, 9], [8, 9]]
REF=[0,1,2,3,7,8,9,4,5,6]
DATA="""3:1 4:1 23:2
3:1 25:2 26:1
15:1 16:1 22:1
9:1 23:1 27:2
1:2 15:1 27:1
0:2 12:1 17:1
0:1 3:1 16:2
9:2 16:1 25:1
1:2 15:1 25:1
9:1 12:1 25:2
2:2 22:1 26:1
6:1 13:2 17:1
0:1 14:1 26:1
5:1 7:1 10:2
1:1 2:1 9:1
3:1 23:1 27:2
8:2 13:1 24:1
7:1 12:1 17:1
14:1 25:1 26:2
9:1 14:1 23:1 25:1
0:1 12:1 26:1
6:1 11:1 27:2
2:1 5:1 22:2
6:1 13:1 26:2
18:5 22:2 30:1
2:1 5:1 24:1
11:1 18:2 22:1
18:2 23:1 32:1
12:1 17:2 31:2
11:1 13:2 22:1
7:1 8:3 11:1 22:3
13:2 23:3 24:3
15:1 16:1 27:1 29:1
14:1 18:2 30:1
0:4 5:4 10:7 13:1
20:2 22:1 26:1
7:2 14:1 26:1
7:1 10:1 24:1 28:1
1:2 13:1 26:1
11:2 12:1 24:2
24:1 27:2 30:1
15:1 17:1 22:3 27:1 28:3
16:1 18:2 29:2 30:2
1:2 7:1 15:1
1:1 18:2 30:1
5:1 10:2 25:1
7:1 14:1 23:1 24:1
8:1 11:1 24:1 27:1
9:1 13:1 16:2
13:1 24:1 28:1
1:2 9:1 25:1
6:3 9:2 27:3
12:1 17:1 25:1
0:1 5:1 12:1 29:1
7:1 12:1 26:2
3:1 16:1 25:1
12:1 17:1 24:1 28:1
1:2 13:1 15:1
11:1 18:1 23:1 29:1
15:1 22:3 25:1 28:3
11:2 12:1 22:2
6:1 11:1 14:1 26:1
12:1 18:3 29:2 30:3
0:2 5:3 10:3 27:1
15:1 24:1 27:2 28:1
7:1 9:2 14:2 23:3
6:1 9:2 14:2 23:3
13:1 16:1 22:1 26:1
9:2 10:7 25:1 28:6
7:1 8:1 11:2 14:1
7:1 22:1 26:1
5:1 22:2 25:1
5:2 22:1 27:1
7:6 10:3 16:3 24:4
20:2 24:1 26:1
11:2 13:1 23:2 29:3
12:2 17:3 18:6 23:4 27:2
12:1 17:1 22:1 28:1
1:1 7:1 24:1
11:1 14:1 23:2 24:1
5:1 24:1 27:1
9:1 10:1 27:1 28:1
14:1 23:1 24:1 30:1
12:1 24:1 30:1
6:2 9:1 12:1
1:3 2:1 17:3 25:1
1:1 2:1 24:1 28:1
3:1 26:1 31:2
0:1 3:1 8:1 27:1
9:1 14:1 26:1 30:1
11:2 14:1 25:1
1:2 2:1 24:1 30:1
5:1 13:1 14:2
7:2 9:1 12:1
1:2 7:1 9:1
5:1 13:2 22:1
1:2 2:1 11:1 24:1
8:4 11:1 14:2 24:2
1:1 17:1 27:1
3:3 18:3 30:2
13:3 22:1 26:3 28:1
7:2 12:1 24:1
3:5 6:1 11:2 18:9
13:1 16:2 24:1
9:1 14:1 20:4 26:2 31:1
3:2 5:1 25:1
14:1 17:1 23:1 27:1
11:1 22:2 26:1
11:1 16:1 25:1 29:1
5:1 7:1 22:2
14:1 24:1 28:1
11:1 16:1 24:1 29:1
3:1 7:1 16:1
2:1 5:1 6:1 9:1 14:1
3:3 8:3 25:2
3:1 5:1 6:1 27:2
1:1 11:1 25:1
14:1 22:1 26:1 30:1
14:1 24:1 26:1 30:1
9:1 27:2 30:1
7:1 22:3 28:3
13:1 15:1 17:1 22:1 28:1
1:1 3:1 7:1 26:1
12:1 22:3 26:2 30:2
3:1 13:2 23:1
9:1 13:1 14:1 23:1
5:1 14:1 17:1 25:1
3:1 25:1 28:2
3:1 27:1 28:2
11:1 12:1 25:1 29:1
9:2 12:1 26:1 31:4"""
class I:
 def __init__(self,x=0,y=None):
  if isinstance(x,I):self.l,self.u=x.l,x.u
  else:self.l,self.u=F(x),F(x if y is None else y)
  assert self.l<=self.u
 def __add__(self,y):
  y=I(y);return I(self.l+y.l,self.u+y.u)
 __radd__=__add__
 def __neg__(self):return I(-self.u,-self.l)
 def __sub__(self,y):return self+-I(y)
 def __rsub__(self,y):return I(y)+-self
 def __mul__(self,y):
  y=I(y);v=[a*b for a in(self.l,self.u)for b in(y.l,y.u)]
  return I(min(v),max(v))
 __rmul__=__mul__
 def inv(self):
  assert self.l>0 or self.u<0
  return I(1/self.u,1/self.l)
 def __truediv__(self,y):return self*I(y).inv()
 def __rtruediv__(self,y):return I(y)*self.inv()
 def mag(self):return max(abs(self.l),abs(self.u))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return [x-y for x,y in zip(a,b)]
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def determinant3(a):return dot(a[0],cross(a[1],a[2]))
def solve3(a,b):
 d=determinant3(a)
 return [determinant3([[b[i]if j==k else a[i][j]for j in range(3)]for i in range(3)])/d for k in range(3)]
def solve2(a,b):
 d=a[0][0]*a[1][1]-a[0][1]*a[1][0]
 return [(b[0]*a[1][1]-a[0][1]*b[1])/d,(a[0][0]*b[1]-b[0]*a[1][0])/d]
def enc(x):
 if isinstance(x,I):return [str(x.l),str(x.u)]
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {k:enc(v)for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [enc(v)for v in x]
 return x
def serial(x):return(json.dumps(enc(x),sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
ARCS=[tuple(a)for e in E for a in(e,e[::-1])]
INDEX={a:i for i,a in enumerate(ARCS)}
CERT=[[(int(a),int(b))for a,b in (t.split(':')for t in line.split())]for line in DATA.splitlines()]
assert len(CERT)==131 and sum(map(len,CERT))==451
assert max(w for c in CERT for i,w in c)==9
assert all(len(set(i for i,w in c))==len(c)and all(0<=i<34 and w>0 for i,w in c)for c in CERT)
assert sorted(tuple(sorted((REF[a],REF[b])))for a,b in E)==list(map(tuple,E))
X=[[I(F(c,CDEN)-RADIUS,F(c,CDEN)+RADIUS)for c in row]for row in CNUM]
expanded=[];records=[]
for number,c in enumerate(CERT):
 for reflect,permutation in enumerate((list(range(10)),REF)):
  literal=[(INDEX[(permutation[ARCS[i][0]],permutation[ARCS[i][1]])],w)for i,w in c]
  B=[[I(0)for _ in range(3)]for _ in range(3)]
  for i,w in literal:
   a,b=ARCS[i];u=X[a];d=sub(X[a],X[b])
   for j in range(3):
    for k in range(3):B[j][k]+=w*(u[j]*d[k]+d[j]*u[k])
  minors=[B[0][0],B[0][0]*B[1][1]-B[0][1]*B[1][0],determinant3(B)]
  assert minors[0].l>F(2,3)and minors[1].l>F(7,5)and minors[2].l>1
  trace=sum(B[j][j]for j in range(3));assert trace.u<64
  assert sum(w for i,w in literal)<=17
  expanded.append(sum(1<<i for i,w in literal))
  records.append(dict(certificate=number,reflection=reflect,leading_minors=minors,trace=trace))
assert len(records)==262
print('ALL_262_INTERVAL_PD3_CERTIFICATES_786_PRINCIPAL_MINORS_PASS')
# All graph spanning trees; orient every one at each of the ten literal roots.
allmasks=set();rootcounts=[0]*10;uses=[0]*len(expanded);spanning=0
for edges in combinations(E,9):
 adj=[[]for _ in range(10)]
 for a,b in edges:adj[a].append(b);adj[b].append(a)
 seen={0};queue=[0]
 for a in queue:
  for b in adj[a]:
   if b not in seen:seen.add(b);queue.append(b)
 if len(seen)!=10:continue
 spanning+=1
 for root in range(10):
  p=[-1]*10;p[root]=root;queue=[root]
  for a in queue:
   for b in adj[a]:
    if p[b]<0:p[b]=a;queue.append(b)
  assert len(queue)==10
  mask=sum(1<<INDEX[(a,p[a])]for a in range(10)if a!=root)
  assert mask not in allmasks;allmasks.add(mask);rootcounts[root]+=1
  witness=next((i for i,m in enumerate(expanded)if mask&m==m),None)
  assert witness is not None,(root,p)
  uses[witness]+=1
assert spanning==6000 and len(allmasks)==60000 and rootcounts==[6000]*10
mask_bytes=(''.join(str(m)+'\n'for m in sorted(allmasks))).encode('ascii')
print('ALL_6000_TRUE_SPANNING_TREES_ALL_60000_ROOTED_WEAK_ESCAPES_EXCLUDED')
print('UNRESTRICTED_RECIPROCAL_SPD_METRIC_U_GE2_WEAK_WALLS_INCLUDED_PASS')
# Independent interval containment of the entire parent's geometric parameter
# box, not just sampled roots or the midpoint of an algebraic enclosure.
PC=list(map(F,['1.715701158033858','-0.1467378366871057','0.2967491976190772','-4.188209982907966','-0.6681749617245179']))
PR=F(1,2**30);BR=F(1,2**42)
a,c,m,d,e=[I(v-PR,v+PR)for v in PC];b=I(F(1,2)-BR,F(1,2)+BR)
h=-d-e
n=[[I(0),I(-1),I(1)],[a,1/b,I(1)],[c,m,I(1)],[d,e,I(1)]]
hs=[I(1),I(1),I(1),h]
r=solve2([n[1][:2],n[3][:2]],[I(1),h])+[I(0)]
p=solve3([n[i]for i in(0,2,3)],[I(1),I(1),h])
q=solve3([n[i]for i in(1,2,3)],[I(1),I(1),h])
V=[[I(0),I(-1),I(0)],[I(0),b,I(0)],[I(-1),I(-1),I(0)],r,[I(0),I(0),I(1)],p,q,[I(0),I(0),I(-1)],[p[0],p[1],-p[2]],[q[0],q[1],-q[2]]]
FC=[[4,5,2,0],[4,1,3,6],[4,6,5],[5,6,3,2],[7,0,2,8],[7,9,3,1],[7,8,9],[8,2,3,9],[0,7,1,4]]
INC=[[0,4,8],[1,5,8],[0,3,4,7],[1,3,5,7],[0,1,2,8],[0,2,3],[1,2,3],[4,5,6,8],[4,6,7],[5,6,7]]
norm=n+[[v[0],v[1],-v[2]]for v in n]+[[I(1),I(0),I(0)]]
rhs=hs+hs+[I(0)];inc_edges={};facarea=[];means=[];second=[]
for i,(face,ni,hi)in enumerate(zip(FC,norm,rhs)):
 for j,v in enumerate(V):
  slack=hi-dot(ni,v)
  if i in INC[j]:assert slack.l<=0<=slack.u
  else:assert slack.l>0
 for j in range(len(face)):
  u,v,w=[V[face[(j+k)%len(face)]]for k in range(3)]
  assert dot(ni,cross(sub(v,u),sub(w,v))).l>0
 for u,v in zip(face,face[1:]+face[:1]):inc_edges.setdefault(tuple(sorted((u,v))),[]).append(i)
 ar=I(0);fm=[I(0)]*3;sm=[[I(0)for _ in range(3)]for _ in range(3)]
 for j in range(1,len(face)-1):
  tri=[V[k]for k in(face[0],face[j],face[j+1])]
  w=dot(ni,cross(sub(tri[1],tri[0]),sub(tri[2],tri[0])))/(2*dot(ni,ni))
  assert w.l>0;ar+=w;sums=[sum(v[k]for v in tri)for k in range(3)]
  for k in range(3):
   fm[k]+=w*sums[k]/3
   for l in range(3):sm[k][l]+=w*(sums[k]*sums[l]+sum(v[k]*v[l]for v in tri))/12
 facarea.append(ar);means.append([v/ar for v in fm]);second.append([[v/ar for v in row]for row in sm])
assert sorted(inc_edges)==list(map(tuple,E))and all(len(v)==2 for v in inc_edges.values())
# All intended zero slacks follow identically from the displayed plane solves,
# reflection and constants. Containing zero numerically is only a sanity check.
volume=sum(ar*hi for ar,hi in zip(facarea,rhs))/3;assert volume.l>0
com=[sum(ar*hi*gi[k]for ar,hi,gi in zip(facarea,rhs,means))/(4*volume)for k in range(3)]
# Reflection gives the third component exactly; keep it exact in the enclosure.
assert com[2].l<=0<=com[2].u;com[2]=I(0)
maxerror=F(0)
for i,v in enumerate(V):
 for k in range(3):
  centered=v[k]-com[k];assert X[i][k].l<centered.l and centered.u<X[i][k].u
  maxerror=max(maxerror,(centered-F(CNUM[i][k],CDEN)).mag())
assert maxerror<F(1,2**20)
print('FULL_PARENT_PARAMETER_BOX_OWN_VOLUME_CENTROID_IN_NONSYMMETRIC_VERTEX_BOX_PASS')
report=dict(identity='MIRROR_BELT_ALL_AFFINE_METRICS_U_GE2_V1',
parent=['minimum-0075','17b392631f5a612ddcf377f1d2c5f478d5abcdf45652178d512fdf449e09de43'],
parent_verified_source=[12560,'fa1609e1456b10b406660567fdd6d7b01e4c67c9ce31c46280116b87187a1191'],
center_numerators=CNUM,center_denominator=CDEN,closed_vertex_box_radius=RADIUS,
true_edges=E,reference_facets=FC,reference_incidence=INC,reflection=REF,
base_certificates=CERT,expanded_certificate_count=262,leading_minor_count=786,
principal_minor_lower_bounds=['2/3','7/5','1'],trace_upper_bound=64,maximum_weight_sum=17,
forced_negative_arrow_bound='-trace(M)/34816',spanning_tree_count=spanning,
rooted_tree_counts=rootcounts,rooted_mask_stream_pin=pin(mask_bytes),
first_certificate_uses=uses,all_interval_certificate_checks=records,
parent_parameter_center=PC,parent_parameter_radius=PR,parent_b_center='1/2',parent_b_radius=BR,
parent_box_volume=volume,parent_box_centroid=com,parent_centered_vertex_maximum_error=maxerror,
scope='All genuine centred V10 polytopes with the literal true-edge graph and vertices in the displayed closed box; every SPD M and its actual inverse. Includes the complete parent algebraic curve and all affine images, not all E17 rank-deficient bodies.',
new_global_type_exclusions=0,new_global_root_exclusions=0)
blob=serial(report);Path('mirror_metric_exclusion.json').write_bytes(blob)
print('MIRROR_BELT_ENTIRE_AFFINE_METRIC_ORBIT_NO_110_PASS')
print('REPORT',*pin(blob));print('SOURCE',*pin(Path(__file__).read_bytes()))
```
