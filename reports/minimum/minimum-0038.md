# minimum-0038

Historical AI scientific report · saved 2026-09-10 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# C32_FOUR_TRIANGLE_FAN_PHYSICAL_BOUNDARY_V1

## Determination

**The proposed proper-subbody extension fails at four triangles, even for a single-vertex fan, even inside an actual C32 realization, and even when every proper principal minor of the selected block is positive.** I give a fixed six-vertex subhull R and a continuous family P(t), 0<t<=1/100, of actual convex polyhedra with (V,E,F)=(9,16,9). Four preserved maximal triangular facets form the induced true-edge path F0-F1-F2-F3 and share one vertex. Their common hull is always R, with Vol(R)/Vol(P(t))<1.

The selected physical block has the exact determinant

```text
D(r)=1-(789/529)r^2+(5932/12167)r^3.
```

It is positive, zero, or negative precisely as r is below, equal to, or above one isolated number r* in (0,1). The family crosses that root without any incidence or mechanical degeneracy: an exact rational interval audit certifies strict (S,U,H)=(4,4,6), with 168 tested primitive intervals separated from zero by more than 10^-6, throughout the isolating interval of the singular body. Thus **proper volume does not even guarantee nonsingularity** of a four-triangle block. At the rational control t=1/500, the determinant is strictly negative although the inherited scalar deficit inequality 400000(Vol(P)-Vol(R))^2>Vol(R)^2 also holds.

A positive extension survives for a different, precisely delimited class: **all triangular side facets of a pyramid with a planar polygonal base** have determinant (1-r)^2(1+2r), for any number of sides, when preserved inside P. The proof is below. The planarity/full-fan condition cannot be replaced by a connected open fan.

**No Gömböc incidence type, unstable-root class, stable-root class, or global complexity lower bound is newly closed.** The principal contribution is a decisive physical boundary for that proposed proof route, together with an exact spectral classification of every extension preserving the displayed subcomplex.

## 1. Authority, work performed, and scope

I read the literal parent `minimum-0035`, SHA-256 `8c1f1ed216fa9ce12e3141e4b177040958865e3dbbc42c88b8a7f4fcf68faf36`, end-to-end. Its compact version-2 envelope authenticates at 57,518 bytes by taking its title-through-EOF Markdown, adding one final LF, and serializing with `ensure_ascii=False,separators=(',',':')`. There is no conflict between its scoped three-triangle theorem and this result. The parent explicitly proves only the three-facet inequality and the associated three-row Schur reduction. :contentReference[oaicite:0]{index=0}

I reconstructed and executed its literal `chain_minor.py`: the 9,929-byte source has SHA-256 `1b3bd959fb05e9de55b084fb4551fb7317b931206576bb13c0296690d6bc8aa1`; its 3,720-byte output reproduces SHA-256 `32b3f4b4843e662f619811fc855a50f4cfe11fca809f47777d054f05cb59e906`. In particular, the parent's negative minor involving two quadrilaterals remains `-2626495209961/103553973712244`, and its three valid triangular-chain checks pass. That nontriangular warning is preserved, not contradicted. :contentReference[oaicite:1]{index=1}

I then investigated longer common-apex fans. Their rank-three area-centroid factorization reduced the proposed spectral extension to a cubic. A rational six-vertex fan supplies the first offending eigenvalue; splitting the two roof inequalities embeds it into the continuous C32 family below. The final proof and exact controls require neither a numerical locator nor any unrecovered parent data. The malformed cap9 decoder, the pending five-tree reconstruction, and free-mass matrix relaxations are not dependencies.

All conclusions concern ordinary uniform volume and actual maximal facets. They permit arbitrary affine distortion and arbitrarily ill-conditioned positive-definite physical metrics through the corresponding affine images. The reported equilibrium counts are for the displayed Euclidean controls and the certified singular interval, not for every affine image.

## 2. One actual body and one matrix

Let g be the ordinary volume centroid of P, and use centered coordinates x=p-g. For its actual facets write q_i.x<=1. Let c_i be the actual centered uniform-area centroid, a_i the outward area vector, V_P=Vol(P), and

```text
d_i = A_i h_i/V_P = 3 omega_i,
Lambda_ij = d_j(1-q_i.c_j),
B = diag(d) Lambda diag(d)^(-1).
```

Here omega_i is the actual volume fraction of the cone from g to facet i. Divergence and cone integration give

```text
sum d_i=3,   sum d_i q_i=sum d_i c_i=0,
sum d_i c_i q_i^T=I_3,
Lambda 1=3*1,   Lambda Q=-Q,
Lambda^2+Lambda=4*1*d^T.
```

For completeness, `sum a_i=0` is divergence for constant vector fields, and `sum c_i a_i^T=V_P I` is divergence for coordinate fields. Coning each facet to g gives volume A_i h_i/3 and cone centroid 3c_i/4, hence `sum d_i c_i=0`. Substitution proves the stated Lambda identities. Since Lambda has the factorization `1*d^T-Q*[d_j c_j]_j`, its rank is at most four; the independent eigenvectors 1 and the three pole-coordinate columns give rank exactly four. The matrix-square identity implies the square-free annihilating polynomial `Lambda(Lambda+I)(Lambda-3I)=0`; its 3-eigenspace is one-dimensional and trace zero makes the -1 multiplicity three. Consequently `rank(I+Lambda)=F-3`, and for nine facets its spectrum is `4,1,1,1,1,1,0,0,0`.

Direct cancellation of the support heights gives the affine-invariant entry formula

```text
B_ij = A_i dist(c_j,aff F_i)/V_P.
```

Suppose R=conv(union_{i in T} F_i) is full-dimensional. Its selected facets are genuinely preserved: R is contained in P, contains F_i, and therefore `R intersect aff(F_i)=F_i`. Their areas and area centroids are unchanged. Thus

```text
B_T(P)=r B_T(R),  r=Vol(R)/Vol(P).
```

This is a statement about the diagonally similar physical matrices, not permission to scale independently chosen Lambda rows or retain artificial cone weights.

### Common-apex reduction

Translate a common vertex o of the selected facets to the raw origin, solely for this geometric calculation. Write their raw area centroids as cbar_i. Then `a_i.cbar_i=0` and

```text
B_T(P)_ij = -a_i.cbar_j/V_P,
E = -(1/Vol(R)) sum_{i in T} cbar_i a_i^T,
det(I+B_T(P)) = det(I_3+r E).
```

The last equality follows from `det(I+UV)=det(I+VU)`. In particular `rank B_T<=3` and `tr E=0`. Expanding the three-dimensional determinant yields the exact general common-apex identity

```text
det(I+B_T(P))
 =1-(tr(E^2)/2)r^2+(tr(E^3)/3)r^3.
```

Nothing in this identity forces the cubic to stay positive on r<1. The following geometry demonstrates the failure.

## 3. The fixed triangular subcomplex and its exact spectrum

Use these six fixed vertices, retaining their permanent nine-vertex labels:

```text
p0=(0,0,0)       p1=(0,0,1)        p2=(0,1,0)
p5=(3/4,-1,3/4)  p6=(1,0,0)        p8=(3/2,-3/2,1/4).
```

Their convex hull R contains the standard tetrahedron on p0,p1,p2,p6, so is full-dimensional. Its exact volume is W=23/48. Select

```text
F0=(0,6,8), F1=(0,2,6), F2=(0,1,2), F3=(0,5,1).
```

The common edges are respectively `(0,6),(0,2),(0,1)`. Every nonconsecutive pair meets only at p0. Thus these four facets form a genuine triangular disk fan whose induced facet adjacency graph is a path, not a fictitious set of independent triangles.

Their exact raw area centroids and outward area vectors are

```text
i   cbar_i                  a_i
0   (5/6,-1/2,1/12)          (0,-1/8,-3/4)
1   (1/3,1/3,0)             (0,0,-1/2)
2   (0,1/3,1/3)             (-1/2,0,0)
3   (1/4,-1/3,7/12)         (-1/2,-3/8,0).
```

The formula in Section 2 now gives, without any mass fitting,

```text
B_T(R) = C/23,
C = [[ 0, 2,14,19],
     [ 2, 0, 8,14],
     [20, 8, 0, 6],
     [11,14, 6, 0]].
```

For example, `-a0.cbar1/W=2/23`; all other entries follow from the same table. Adjacent triangular pairs have symmetric entries, as required by their common tetrahedral volumes. Nonadjacent entries need not be symmetric.

Exact calculation gives

```text
rank C=3,
sum_{i<j} C_ij C_ji=789,
tr(C^3)=17796=3*5932,
char_C(z)=z(z^3-789z-5932).
```

Therefore every convex extension of this literal R preserving the four selected facets, not merely the family subsequently constructed, satisfies

```text
det((I+Lambda)_T)=D(r)=1-(789/529)r^2+(5932/12167)r^3.
```

This includes every invertible affine image of such an extension.

### Complete sign and spectral determination

`D(0)=1`, `D(1)=-48/12167`, and

```text
D'(r)=r[-1578/529+(17796/12167)r]<0  for 0<r<=1.
```

Hence D has exactly one zero r* in (0,1). Exact integer-grid bisection gives

```text
199480998299/200000000000 < r* < 124675623937/125000000000,
i.e. 0.997404991495 < r* < 0.997404991496.
```

The cubic `z^3-789z-5932` has a root in each of `(-24,-23),(-9,-8),(31,32)`, by its exact endpoint signs. These three disjoint intervals exhaust its roots. Consequently the four eigenvalues of the selected I+Lambda block are real: one is 1, two remain positive for 0<=r<=1, and the remaining eigenvalue crosses zero exactly at r*. Thus:

```text
0<r<r*:   four positive real eigenvalues; determinant positive;
r=r*:     rank three; determinant zero;
r*<r<=1:  exactly one negative eigenvalue; determinant negative.
```

All fourteen proper principal minors of this four-by-four block are positive throughout 0<=r<=1. The six reciprocal products in C are `4,280,209,64,196,36`, each below 529. For the four three-element subsets, their reciprocal sums are `348,409,525,296`, also below 529. Each triple determinant is `1-s r^2/529` plus its positive oriented-cycle term, hence is strictly positive. This is an order-four failure, not an inherited bad three-minor hidden inside the selected block.

The true-edge-connected triangular order boundary is therefore sharp: one row has determinant one; two edge-adjacent triangles give `1-r^2>0` for their proper tetrahedral hull; three edge-connected triangles fall under the literal parent's two-edge-chain theorem. Four suffice for failure. At C32 any true-edge-connected four-triangle union has at most six of the nine actual vertices, so the proper-subbody condition is automatic, but positivity is not.

## 4. A continuous actual C32 realization of both sides and the singular point

For `0<t<=1/100`, define P(t) by the following nine inequalities `n_i(t).p<=h_i(t)`, in permanent facet order:

```text
i   n_i(t)                         h_i(t)
0   (0,-1,-6)                      0
1   (0,0,-1)                       0
2   (-1,0,0)                       0
3   (-4,-3,0)                      0
4   (-14,-15,-6)                   0
5   (1-t,1-t,1-2t)                 1-t
6   (2-2t,1-2t,2-8t)               2-2t
7   (2-6t,1-4t,2-2t)               2-2t
8   (1-2t,1-t,1-t)                 1-t.
```

Six vertices are the fixed points in Section 3. The other three are

```text
p3=((1-t)(1+2t), -2t(1-t), (1-t)(1+2t))/(2-t-4t^2),
p4=((1-t)(3+4t), -8t(1-t), 2(1-t))/(5-11t+4t^2),
p7=(51(1-t), -54(1-t), 16(1-t))/(40-61t).
```

Every displayed denominator is positive on the entire parameter interval. The actual maximal facet cycles, including their deliberate nonsimplicial coplanarities, are exactly

```text
F0 [0,6,8]       F1 [0,2,6]       F2 [0,1,2]
F3 [0,5,1]       F4 [0,8,7,5]     F5 [2,3,4,6]
F6 [4,7,8,6]     F7 [1,5,7,4,3]   F8 [1,3,2].
```

The sixteen true edges are

```text
(0,1),(0,2),(0,5),(0,6),(0,8),(1,2),(1,3),(1,5),
(2,3),(2,6),(3,4),(4,6),(4,7),(5,7),(6,8),(7,8).
```

All nine vertices are extreme, all nine facet planes are irredundant, and every nonincidence slack is strictly positive for all 0<t<=1/100. The full source below proves this continuously: it checks every rational vertex slack and exhausts all 84 support triples by exact polynomial identities and Bernstein coefficient signs. There are 27 feasible triples, representing the nine vertices including their nonsimple incidences, and 57 infeasible triples, each with a fixed strict violating inequality throughout the interval. No triple determinant vanishes inside the interval. A recession-cone enumeration independently proves boundedness.

To explain the exact sign certificate: for a polynomial with any initial power of t factored out, the code converts its remaining ascending power coefficients a_j to Bernstein coefficients on [0,1/100] by `b_k=sum_{j<=k} a_j(1/100)^j binom(k,j)/binom(n,j)`. Strict positivity of every b_k proves the required strict sign for t>0. Thus this is a finite continuous proof, not a sampled hull assertion. The exact face lattice fixes the orientation and triangulations used for integration throughout the interval; the independently reconstructed rational endpoint hulls check them directly.

### Why R is preserved and proper

At t=0 the last four inequalities reduce to the two roof planes

```text
p_x+p_y+p_z<=1,   2p_x+p_y+2p_z<=2.
```

Together with the first five they define exactly the six-vertex R. Put alpha=t/(1-t). On the cone defined by the first five inequalities, the four new roof conditions are

```text
p_x+p_y+p_z <=1+alpha p_z,
p_x+p_y+p_z <=1+alpha p_x,
2p_x+p_y+2p_z<=2+alpha(p_y+6p_z),
2p_x+p_y+2p_z<=2+alpha(4p_x+3p_y).
```

Every added right-hand term is nonnegative on that cone. Hence R is contained in P(t). The boundary point `(1/2,0,1/2)` of R satisfies all nine inequalities strictly for t>0, proving strict volume inclusion. The four selected facet planes remain supporting and intersect P(t) in exactly the original triangles. In particular R is full-dimensional, the selected triangles are genuinely preserved, and `r<1`; none of these premises is inferred from a freely assigned scalar.

Exact integration gives

```text
V(t)=(t-1)(1128t^4-3658t^3+835t^2+2467t-1150)
     /[6(61t-40)(4t^2-11t+5)(4t^2+t-2)].
```

The same polynomial checker proves `V'(t)>0`, so r(t)=(23/48)/V(t) strictly decreases. There is exactly one t* in this interval with D(r(t*))=0:

```text
2399007863/1000000000000 < t* < 299875983/125000000000,
i.e. 0.002399007863 < t* < 0.002399007864.
```

This specifies an exact algebraic physical polytope. An explicit integer-polynomial generator for t* is obtained by writing the displayed volume as N(t)/Q(t):

```text
27648 N(t)^3 -9468 N(t)Q(t)^2 +1483 Q(t)^3=0,
```

with the isolating interval above. No expanded degree-fifteen coefficient table is needed to reconstruct it. Its denominators are positive, and the root is unique and transverse. Therefore the selected determinant is negative for `0<t<t*`, zero at t*, and positive for `t*<t<=1/100`.

The exact interval audit in the capsule also integrates this algebraic body at its own centroid and proves strict `(4,4,6)` throughout the t* isolator. Matrix singularity here is neither a flattened solid, an incidence wall, nor a mechanical equilibrium degeneracy.

## 5. One fully rational negative control, with its actual mass data

Take t=1/500. The complete coordinates are

```text
0 (0,0,0)
1 (0,0,1)
2 (0,1,0)
3 (125249/249748,-499/249748,125249/249748)
4 (93812/155563,-499/155563,62375/155563)
5 (3/4,-1,3/4)
6 (1,0,0)
7 (25449/19939,-26946/19939,7984/19939)
8 (3/2,-3/2,1/4).
```

Use exactly the nine facet cycles and sixteen edges above. Its ordinary volume is

```text
V_P=743992554601211/1549322036088872.
```

With `G=13859928571499513036851080048`, its exact ordinary centroid is

```text
g=(6748991945383365267959630389,
   -2642032621652432866983703193,
    4372576569979438119365214199)/G.
```

Here is a compact exact specification of **all nine actual facet centroids, cone weights, and the single full 9x9 Lambda**, avoiding an unreadable 81-entry fraction table. It is also implemented literally in the recovery source. For each oriented facet cycle f and its displayed outward n_i, form

```text
u_j=(p_f[j]-p_f[0]) cross (p_f[j+1]-p_f[0]),  j=1,...,len(f)-2,
w_j=n_i.u_j >0,
a_i=(1/2) sum_j u_j,
cbar_i=sum_j w_j(p_f[0]+p_f[j]+p_f[j+1])/(3 sum_j w_j),
c_i=cbar_i-g,
d_i=a_i.c_i/V_P,   omega_i=d_i/3,
q_i=n_i/(h_i-n_i.g),
Lambda_ij=d_j[1-q_i.c_j],  0<=i,j<=8.
```

All inputs to these finite rational formulas are printed above; they specify each of the 81 entries of one matrix, not independently chosen blocks. The output ledger serializes every raw and centered area centroid, every area vector, all nine cone weights, all poles, and all 81 Lambda fractions. For the selected four facets the centroids and area vectors are already the short table in Section 3, and their actual d weights are, explicitly,

```text
d0=(g_y/8+3g_z/4)/V_P,
d1=g_z/(2V_P),
d2=g_x/(2V_P),
d3=(g_x/2+3g_y/8)/V_P.
```

Independent integration with boundary apex p0 and with the mean of all vertices gives the identical V_P and g; reintegrating after translation gives centroid exactly zero. The code verifies every shared area/moment identity, all 81 matrix-square entries, `Lambda Q=-Q`, rank Lambda=4, and rank(I+Lambda)=6. The selected B block is verified against the fixed C by diagonal similarity using these same d values.

The exact ratio and negative minor are

```text
r=4454300853755507/4463955327607266 <499/500,

det((I+Lambda)_[0,1,2,3])
 =-29225402286904272323120130050768458025941435
   /44476389385373086840084719020220335744901748548
 <-1/2000.
```

Numerically the minor is about -0.0006570992540. All fourteen proper principal minors are strictly positive. In addition,

```text
400000(V_P-23/48)^2 > (23/48)^2.
```

This last check shows that the **scalar** deficit used in the earlier conditional three-row denominator bound does not repair a four-row positivity claim. It does not assert that this (4,4,6) body has the unique-U ancestor-closed escape certificate from which that scalar bound was originally derived.

The exhaustive Euclidean feature audit at g is

```text
S=[0,3,4,7],
U=[1,2,6,8],
H=[(0,5),(0,8),(1,2),(1,5),(2,6),(6,8)].
```

All 64 true-edge cone components are nonzero. The separate t=1/100 positive-determinant control has the same strict counts. The algebraic singular body likewise has these counts, with its full 168-primitive strict interval certificate. These bodies are controls of a proposed unconditional physical theorem, not homogeneous Gömböcs and not counterexamples to an additional, unproved S=1-specific assertion.

## 6. A positive whole-fan theorem, with proof and C32 consequences

**Planar-base complete-fan theorem.** Let R be a pyramid over a genuine convex planar m-gon B, m>=3, with apex o off its plane. Let T consist of all m triangular side facets. Suppose they are preserved as actual maximal facets of a full-dimensional convex P containing R. With the physical Lambda of P and r=Vol(R)/Vol(P),

```text
spec(B_T(R))={2,-1,-1,0 repeated m-3 times},
det((I+Lambda)_T)=(1+2r)(1-r)^2.
```

In particular a proper extension gives a nonsingular block with positive real eigenvalues, for any m.

**Proof.** Put o=0. Let cbar_B and a_B be the base area centroid and outward area vector. Applying divergence to the entire pyramid gives

```text
sum_side cbar_i a_i^T + cbar_B a_B^T = W I_3,
a_B.cbar_B=3W.
```

The common-apex reduction is therefore

```text
E=-I_3+cbar_B a_B^T/W.
```

The rank-one term has eigenvalue 3 on cbar_B and eigenvalue zero on the two-dimensional kernel of a_B^T. Thus E has eigenvalues 2,-1,-1. The rectangular-product identity gives the same nonzero eigenvalues for B_T(R), with m-3 additional zeros; equivalently its characteristic polynomial is `z^(m-3)(z-2)(z+1)^2`. Scaling by the actual ratio and taking the determinant proves the formula. This uses true planar pyramid geometry and all side facets; neither ingredient follows merely from an abstract fan graph.

Since the full physical I+Lambda has rank F-3, nonsingularity also forces F>=m+3. For this particular geometric class a stronger elementary count is available: **every proper extension preserving all the triangular sides has F>=2m.** Indeed any point of P outside R must lie beyond the base plane, since the side halfspaces and the base halfspace define R. That plane cannot support P. Every base edge is still a true edge of one preserved triangular facet and has an unselected incident facet. One unselected facet cannot contain two different base edges: their affine span is the base plane, which no longer supports P. Thus the m base edges require m distinct additional facets.

At C32, F=9 consequently rules out a proper planar-base complete side fan with m>=5. For m=5,6,7 the fan uses only m+1<=8 vertices, so a nine-vertex P would necessarily be proper and is geometrically impossible under these premises. An m=8 fan uses all nine vertices: its hull can equal P, r=1, and the strict bound must not be invoked. The only larger-than-parent proper planar fan remaining here is m=4, for which the formula is always positive. These are explicit geometric/sign-domain exclusions, not newly counted Gömböc catalogue/root exclusions; some may already be subsumed by existing incidence or pyramid results.

## 7. Exact remaining complement and continuation

The new positive theorem leaves nonplanar complete fans, open fans, branched triangular complexes, and complexes without a common apex outside its positive scope. The four-path example decisively prevents asserting positivity or nonsingularity for those domains from connectedness, triangularity, common apex, rank three, or a proper common hull-volume ratio alone. For the displayed fixed subcomplex and all its preserved extensions, the complete determinant/spectral classification is Section 3; there is no remaining ratio ambiguity in that class.

No entire realization space of the displayed C32 facet list is excluded as a Gömböc. Its negative-minor controls occupy a nonempty relatively open strict incidence/mechanical domain, while its singular crossing occurs inside that same mechanical class. No stable-root or unstable-root enumeration was performed. All inherited accepted C32 exclusions remain separate; neither C>=34 nor a C32 attainer is asserted.

The parent's three-row elimination remains sound. On a nonsingular four-row block the nine-facet Schur complement has rank two, but the new family supplies an actual singular four-row block, so such elimination must branch on its determinant rather than divide by a universally positive volume bound. The full physical I+Lambda still has nonnegative spectrum and rank six; the negative principal eigenvalue is possible because this physical matrix is not symmetric.

The useful continuation is therefore to keep the proved three-chain pivot, or use a genuinely planar complete-fan pivot, and impose any stronger mechanically conditioned claim on the **same** actual Lambda. The literal family here should be a regression test for every proposed four-triangle inequality or determinant denominator. Any S=1-specific repair must use a new mechanical premise that these strict (4,4,6) controls do not satisfy; ordinary mass identities, convexity, incidence, and the scalar proper-volume deficit are already all present.

## 8. Complete deterministic recovery capsule

Save the following full source as `c32_fourfan.py`, UTF-8/LF with one final LF. It uses **CPython 3.13.5, standard library only, assertions enabled**, no randomness, numerical solver, external input, or parent file. Reconstruction and verification are the same command:

```sh
python -S c32_fourfan.py > c32_fourfan.log
```

The source proves the continuous hull/volume statements by exact polynomial signs, reconstructs rational controls from both H and V, performs two actual volume integrations, checks one physical matrix throughout, isolates both roots exactly, and encloses every mechanical primitive of the algebraic singular body with rational intervals. Two fresh directories reproduced output and transcript byte-for-byte. These are clean replays of one source, not two independently authored full implementations or external peer review.

```text
c32_fourfan.py    16394 bytes  6419d9a0f237bf13dd429c5a843c07e7d177d053a154a8c32b99e71cfe3fc238
c32_fourfan.json  37861 bytes  e35023eb2e7da92dc8dd62763344a911987afada035d3712e265d68b7d701c1f
c32_fourfan.log     810 bytes  c5a2ef4867c84d7dbb0ff788060340b3645aa351691f26a6d8d17e0bb21506ce
```

The JSON is a generated full physical ledger, not an irreducible hidden input. All reconstruction-critical data are in the source below.

```python
"""C32_FOUR_TRIANGLE_FAN_PHYSICAL_BOUNDARY_V1.
CPython 3.13.5; standard library only; assertions must be enabled.
Run: python -S c32_fourfan.py > c32_fourfan.log
Analytical parent: minimum-0035,
8c1f1ed216fa9ce12e3141e4b177040958865e3dbbc42c88b8a7f4fcf68faf36.
No parent file, optimizer, random seed, or external input is required.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import hashlib,json
assert __debug__
Z=F(0);ONE=F(1);TMAX=F(1,100);TNEG=F(1,500)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),Z)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(a,s):return tuple(s*x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det3(a,b,c):return dot(a,cross(b,c))
def mm(a,b):return [[dot(r,c) for c in zip(*b)] for r in a]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def elimination(a):
 a=[list(map(F,r)) for r in a];rank=0;d=ONE
 for j in range(len(a[0])):
  k=next((k for k in range(rank,len(a)) if a[k][j]),None)
  if k is None:continue
  if k!=rank:a[k],a[rank]=a[rank],a[k];d=-d
  z=a[rank][j];d*=z;a[rank]=[v/z for v in a[rank]]
  for i in range(len(a)):
   if i!=rank:
    z=a[i][j];a[i]=[v-z*w for v,w in zip(a[i],a[rank])]
  rank+=1
  if rank==len(a):break
 return rank,d,a
def determinant(a):
 k,d,_=elimination(a);return d if k==len(a) else Z
def inverse(a):
 n=len(a);k,_,b=elimination([list(a[i])+eye(n)[i] for i in range(n)])
 assert k==n and [r[:n] for r in b]==eye(n)
 return [r[n:] for r in b]
# Exact univariate polynomials, ascending coefficients.
def poly(a):
 a=list(map(F,a))
 while a and a[-1]==0:a.pop()
 return tuple(a)
def pa(a,b):return poly([(a[i] if i<len(a) else Z)+(b[i] if i<len(b) else Z) for i in range(max(len(a),len(b)))])
def ps(a,s):return poly([s*x for x in a])
def pm(a,b):
 if not a or not b:return ()
 c=[Z]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return poly(c)
def pd(a):return poly([i*a[i] for i in range(1,len(a))])
def pe(a,t):
 z=Z
 for x in a[::-1]:z=z*t+x
 return z
def padd_all(aa):
 z=()
 for a in aa:z=pa(z,a)
 return z
def pdet(a):
 return padd_all([ps(pm(a[0][i],pa(pm(a[1][j],a[2][k]),ps(pm(a[1][k],a[2][j]),-1))),1) for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]])
def positive(a):
 # Strip t^k, then certify positivity of every Bernstein coefficient on [0,TMAX].
 a=list(a)
 while a and a[0]==0:a.pop(0)
 if not a:return False
 n=len(a)-1
 return all(sum((a[j]*TMAX**j*F(comb(k,j),comb(n,j)) for j in range(k+1)),Z)>0 for k in range(n+1))
def const(x):return poly([x])
# H rows encode n(t).x <= h(t); the first five pass through the common apex.
RAW_H=[[(0,),(-1,),(-6,),(0,)],[(0,),(0,),(-1,),(0,)],
 [(-1,),(0,),(0,),(0,)],[(-4,),(-3,),(0,),(0,)],
 [(-14,),(-15,),(-6,),(0,)],[(1,-1),(1,-1),(1,-2),(1,-1)],
 [(2,-2),(1,-2),(2,-8),(2,-2)],[(2,-6),(1,-4),(2,-2),(2,-2)],
 [(1,-2),(1,-1),(1,-1),(1,-1)]]
H=[[poly(c) for c in r] for r in RAW_H]
D=[const(1) for _ in range(9)]
N=[[const(x) for x in p] for p in [(0,0,0),(0,0,1),(0,1,0),(0,0,0),(0,0,0),
 (F(3,4),-1,F(3,4)),(1,0,0),(0,0,0),(F(3,2),-F(3,2),F(1,4))]]
D[3]=poly([2,-1,-4]);N[3]=list(map(poly,[(1,1,-2),(0,-2,2),(1,1,-2)]))
D[4]=poly([5,-11,4]);N[4]=list(map(poly,[(3,1,-4),(0,-8,8),(2,-2)]))
D[7]=poly([40,-61]);N[7]=list(map(poly,[(51,-51),(-54,54),(16,-16)]))
FAC=[[0,6,8],[0,2,6],[0,1,2],[0,5,1],[0,8,7,5],
 [2,3,4,6],[4,7,8,6],[1,5,7,4,3],[1,3,2]]
SELECTED=[0,1,2,3];RV=[0,1,2,5,6,8]
C=[[0,2,14,19],[2,0,8,14],[20,8,0,6],[11,14,6,0]]
assert all(positive(d) for d in D)
def points(t):return [tuple(pe(n,t)/pe(d,t) for n in ns) for ns,d in zip(N,D)]
def normals(t):return [tuple(pe(a,t) for a in h) for h in H]
# Prove all incidence and nonincidence inequalities on the entire interval.
for i,h in enumerate(H):
 for j in range(9):
  s=pa(pm(h[3],D[j]),ps(padd_all([pm(h[k],N[j][k]) for k in range(3)]),-1))
  assert (not s) if j in FAC[i] else positive(s)
# Boundedness: the five homogeneous inequalities have exactly these five rays.
lower=[tuple(pe(x,0) for x in h[:3]) for h in H[:5]]
def ray(v):return scale(v,1/abs(next(x for x in v if x)))
rays=set()
for a,b in combinations(lower,2):
 v=cross(a,b)
 if not any(v):continue
 for w in (v,scale(v,-1)):
  if all(dot(n,w)<=0 for n in lower):rays.add(ray(w))
assert elimination(lower)[0]==3
assert rays=={ray(points(0)[j]) for j in [1,2,5,6,8]}
for v in rays:assert positive(padd_all([ps(H[5][k],v[k]) for k in range(3)]))
# Exhaustive H-triple vertex proof over 0<t<=TMAX, not merely sampled topology.
triple_counts=[0,0,0];found=set()
for ids in combinations(range(9),3):
 a=[H[i][:3] for i in ids];hh=[H[i][3] for i in ids];d=pdet(a)
 if not d:triple_counts[0]+=1;continue
 sign=1 if pe(d,TNEG)>0 else -1
 assert positive(ps(d,sign))
 nums=[]
 for k in range(3):
  b=[list(r) for r in a]
  for i in range(3):b[i][k]=hh[i]
  nums.append(pdet(b))
 sl=[pa(pm(h[3],d),ps(padd_all([pm(h[k],nums[k]) for k in range(3)]),-1)) for h in H]
 if all(sign*pe(s,TNEG)>=0 for s in sl):
  matches=[j for j in range(9) if all(not pa(pm(nums[k],D[j]),ps(pm(N[j][k],d),-1)) for k in range(3))]
  assert len(matches)==1;found.add(matches[0]);triple_counts[1]+=1
 else:
  assert any(positive(ps(s,-sign)) for s in sl);triple_counts[2]+=1
assert found==set(range(9)) and sum(triple_counts)==84
# Symbolic signed tetrahedral integration: one common denominator suffices.
common=pm(pm(D[3],D[4]),D[7]);vn=()
for f in FAC:
 for j in range(1,len(f)-1):
  ids=[f[0],f[j],f[j+1]];z=pdet([N[i] for i in ids])
  for k in [3,4,7]:
   if k not in ids:z=pm(z,D[k])
  vn=pa(vn,z)
vd=ps(common,6)
want=pm(poly([-1,1]),poly([-1150,2467,835,-3658,1128]))
assert vn==want and positive(vn) and positive(vd)
assert positive(pa(pm(pd(vn),vd),ps(pm(vn,pd(vd)),-1)))
assert positive(pa(ps(vn,48),ps(vd,-23)))
def volume(t):return pe(vn,t)/pe(vd,t)
def ratio(t):return F(23,48)/volume(t)
def minor(r):return 1-F(789,529)*r*r+F(5932,12167)*r*r*r
assert minor(0)==1 and minor(1)==-F(48,12167)
assert -2*F(789,529)+3*F(5932,12167)<0
assert determinant(C)==0 and elimination(C)[0]==3
assert sum(C[i][j]*C[j][i] for i,j in combinations(range(4),2))==789
assert sum(mm(mm(C,C),C)[i][i] for i in range(4))==3*5932
# All proper principal minors are positive on 0<=r<=1.
for ids in combinations(range(4),3):
 s=sum(C[i][j]*C[j][i] for i,j in combinations(ids,2));assert s<529
for i,j in combinations(range(4),2):assert C[i][j]*C[j][i]<529
# Exactly isolate both the volume-ratio root and its unique physical parameter.
def grid_root(fun,lo,hi,den):
 assert fun(F(lo,den))*fun(F(hi,den))<0
 sign=1 if fun(F(lo,den))>0 else -1
 while hi-lo>1:
  m=(lo+hi)//2;v=fun(F(m,den));assert v!=0
  if sign*v>0:lo=m
  else:hi=m
 return [F(lo,den),F(hi,den)]
rbox=grid_root(minor,990000000000,1000000000000,10**12)
tbox=grid_root(lambda t:minor(ratio(t)),10**9,10**10,10**12)
assert minor(ratio(TNEG))<0<minor(ratio(TMAX))
# Independent rational V-hull rebuild for the concrete control and its subhull.
def hull(p):
 fs=set()
 for i,j,k in combinations(range(len(p)),3):
  n=cross(sub(p[j],p[i]),sub(p[k],p[i]))
  if not any(n):continue
  ss=[dot(n,sub(x,p[i])) for x in p]
  if (min(ss)<0<max(ss)) or not any(ss):continue
  fs.add(tuple(a for a,s in enumerate(ss) if s==0))
 fs=sorted(fs);edges=set()
 for a,b in combinations(fs,2):
  inter=set(a)&set(b)
  if len(inter)==2:edges.add(tuple(sorted(inter)))
  else:assert len(inter)<=1
 center=tuple(sum(x[k] for x in p)/len(p) for k in range(3))
 cycles=[]
 for f in fs:
  adj={i:sorted(j for j in f if tuple(sorted((i,j))) in edges) for i in f}
  assert all(len(v)==2 for v in adj.values());cy=[min(f),adj[min(f)][0]]
  while True:
   j=next(j for j in adj[cy[-1]] if j!=cy[-2])
   if j==cy[0]:break
   assert j not in cy;cy.append(j)
  assert set(cy)==set(f)
  if det3(sub(p[cy[1]],p[cy[0]]),sub(p[cy[2]],p[cy[0]]),sub(center,p[cy[0]]))>0:cy=[cy[0]]+cy[:0:-1]
  cycles.append(cy)
 assert len(p)-len(edges)+len(fs)==2
 return cycles,sorted(edges)
def integrate(p,faces,apex):
 v=Z;m=[Z]*3
 for f in faces:
  for j in range(1,len(f)-1):
   a,b,c=[p[k] for k in [f[0],f[j],f[j+1]]]
   w=det3(sub(a,apex),sub(b,apex),sub(c,apex))/6
   assert w>=0;v+=w
   for k in range(3):m[k]+=w*(apex[k]+a[k]+b[k]+c[k])/4
 assert v>0
 return v,tuple(x/v for x in m)
def physical(t):
 p=points(t);hf,edges=hull(p)
 assert {frozenset(f) for f in hf}=={frozenset(f) for f in FAC}
 avg=tuple(sum(x[k] for x in p)/9 for k in range(3))
 v,g=integrate(p,FAC,(Z,Z,Z));assert (v,g)==integrate(p,FAC,avg)
 assert v==volume(t)
 x=[sub(a,g) for a in p];assert integrate(x,FAC,(Z,Z,Z))==(v,(Z,Z,Z))
 q=[];d=[];cc=[];rawcc=[];av=[]
 for h,f in zip(normals(t),FAC):
  n=h[:3];height=h[3]-dot(n,g);assert height>0;q.append(scale(n,1/height))
  area=(Z,Z,Z);sumw=Z;moment=[Z]*3
  for j in range(1,len(f)-1):
   a,b,c=[p[k] for k in [f[0],f[j],f[j+1]]]
   cr=cross(sub(b,a),sub(c,a));w=dot(cr,n);assert w>0
   area=add(area,scale(cr,F(1,2)));sumw+=w
   for k in range(3):moment[k]+=w*(a[k]+b[k]+c[k])/3
  c=tuple(y/sumw for y in moment);rawcc.append(c);c=sub(c,g);cc.append(c);av.append(area);d.append(dot(area,c)/v)
 assert all(z>0 for z in d) and sum(d)==3
 assert all(sum(d[i]*q[i][k] for i in range(9))==sum(d[i]*cc[i][k] for i in range(9))==0 for k in range(3))
 assert [[sum(d[i]*cc[i][j]*q[i][k] for i in range(9)) for k in range(3)] for j in range(3)]==eye(3)
 L=[[d[j]*(1-dot(q[i],cc[j])) for j in range(9)] for i in range(9)]
 assert all(L[i][i]==0 and sum(L[i])==3 for i in range(9))
 assert all(L[i][j]>0 for i in range(9) for j in range(9) if i!=j)
 assert mm(L,q)==[list(scale(a,-1)) for a in q]
 LL=mm(L,L);assert all(LL[i][j]+L[i][j]==4*d[j] for i in range(9) for j in range(9))
 K=[[L[i][j]+F(i==j) for j in range(9)] for i in range(9)]
 assert elimination(L)[0]==4 and elimination(K)[0]==6
 rp=[p[j] for j in RV];rf,_=hull(rp);rv,_=integrate(rp,rf,(Z,Z,Z));assert rv==F(23,48)<v
 assert RV==sorted(set().union(*(set(FAC[i]) for i in SELECTED)))
 B=[[d[i]*L[i][j]/d[j] for j in SELECTED] for i in SELECTED];r=rv/v
 assert B==[[r*F(C[i][j],23) for j in range(4)] for i in range(4)]
 small=[[B[i][j]+F(i==j) for j in range(4)] for i in range(4)]
 de=determinant(small);assert de==minor(r)
 proper=[]
 for k in range(1,4):
  for ids in combinations(range(4),k):
   z=determinant([[small[i][j] for j in ids] for i in ids]);assert z>0;proper.append([ids,z])
 # Exhaustive Euclidean mechanics at this same ordinary volume centroid.
 stable=[];unstable=[];saddles=[];cones=[];zeros=0
 for i in range(9):
  vals=[dot(q[i],sub(q[i],q[j])) for j in range(9) if j!=i]
  if min(vals)>0:stable.append(i)
  else:assert min(vals)<0
 for i in range(9):
  nei=[b if a==i else a for a,b in edges if i in (a,b)]
  vals=[dot(x[i],sub(x[i],x[j])) for j in nei]
  if min(vals)>0:unstable.append(i)
  else:assert min(vals)<0
 for a,b in edges:
  e=sub(x[b],x[a]);u=-dot(x[a],e)/dot(e,e)
  i,j=[i for i,f in enumerate(FAC) if a in f and b in f]
  aa=dot(q[i],q[i]);bb=dot(q[i],q[j]);cc0=dot(q[j],q[j]);delta=aa*cc0-bb*bb;assert delta>0
  b1=(cc0-bb)/delta;b2=(aa-bb)/delta
  assert add(x[a],scale(e,u))==add(scale(q[i],b1),scale(q[j],b2))
  vals=[u,1-u,b1,b2];zeros+=sum(z==0 for z in vals)
  if min(vals)>0:saddles.append([a,b])
  else:assert min(vals)<0
  cones.append([a,b,*vals])
 assert len(stable)+len(unstable)-len(saddles)==2
 return dict(parameter=t,vertices=p,facets=FAC,edges=edges,volume=v,centroid=g,
  raw_facet_area_centroids=rawcc,centered_facet_area_centroids=cc,facet_area_vectors=av,
  cone_weights=[z/3 for z in d],d=d,poles=q,Lambda=L,selected=SELECTED,
  subhull_vertices=RV,subhull_volume=rv,ratio=r,selected_B=B,minor=de,
  proper_principal_minors=proper,mechanics=dict(S=stable,U=unstable,H=saddles),
  edge_cone_components=cones,zero_edge_components=zeros)
neg=physical(TNEG);pos=physical(TMAX)
assert neg['minor']<-F(1,2000)<0<pos['minor'] and neg['zero_edge_components']==0 and pos['zero_edge_components']==0
assert neg['ratio']<F(499,500) and 400000*(neg['volume']-neg['subhull_volume'])**2>neg['subhull_volume']**2
# Independent affine-invariant mechanism: a common-apex block has rank at most three.
assert elimination(neg['selected_B'])[0]==3
# Exact polynomial spectral brackets for C: one eigenvalue is below -23.
def cubic(z):return z**3-789*z-5932
assert cubic(-24)<0<cubic(-23) and cubic(-9)>0>cubic(-8) and cubic(31)<0<cubic(32)
# Exact rational interval audit of the algebraic singular body, without rounding.
class Interval:
 def __init__(self,a,b=None):
  if isinstance(a,Interval):self.lo,self.hi=a.lo,a.hi
  else:self.lo,self.hi=F(a),F(a if b is None else b)
  assert self.lo<=self.hi
 def __add__(self,b):
  b=Interval(b);return Interval(self.lo+b.lo,self.hi+b.hi)
 __radd__=__add__
 def __neg__(self):return Interval(-self.hi,-self.lo)
 def __sub__(self,b):return self+-Interval(b)
 def __rsub__(self,b):return Interval(b)+-self
 def __mul__(self,b):
  b=Interval(b);s=[a*c for a in [self.lo,self.hi] for c in [b.lo,b.hi]]
  return Interval(min(s),max(s))
 __rmul__=__mul__
 def __truediv__(self,b):
  b=Interval(b);assert b.lo>0 or b.hi<0
  return self*Interval(1/b.hi,1/b.lo)
 def __rtruediv__(self,b):return Interval(b)/self
it=Interval(*tbox);ip=points(it);iv=Interval(0);im=[Interval(0) for _ in range(3)]
for f in FAC:
 for j in range(1,len(f)-1):
  a,b,c=[ip[k] for k in [f[0],f[j],f[j+1]]];w=det3(a,b,c)/6
  iv+=w
  for k in range(3):im[k]+=w*(a[k]+b[k]+c[k])/4
assert iv.lo>F(23,48)
ig=tuple(z/iv for z in im);ix=[sub(a,ig) for a in ip];iq=[]
for h in normals(it):
 height=h[3]-dot(h[:3],ig);assert height.lo>0;iq.append(scale(h[:3],1/height))
sg=[];ug=[];hg=[];margins=[]
def signed(z):
 assert z.lo>0 or z.hi<0
 margins.append(z.lo if z.lo>0 else -z.hi)
 return 1 if z.lo>0 else -1
for i in range(9):
 if min(signed(dot(iq[i],sub(iq[i],iq[j]))) for j in range(9) if j!=i)>0:sg.append(i)
 nei=[b if a==i else a for a,b in neg['edges'] if i in (a,b)]
 if min(signed(dot(ix[i],sub(ix[i],ix[j]))) for j in nei)>0:ug.append(i)
for a,b in neg['edges']:
 e=sub(ix[b],ix[a]);u=-dot(ix[a],e)/dot(e,e)
 i,j=[i for i,f in enumerate(FAC) if a in f and b in f]
 aa=dot(iq[i],iq[i]);bb=dot(iq[i],iq[j]);cc0=dot(iq[j],iq[j]);delta=aa*cc0-bb*bb
 assert delta.lo>0
 if min(signed(z) for z in [u,1-u,(cc0-bb)/delta,(aa-bb)/delta])>0:hg.append([a,b])
assert dict(S=sg,U=ug,H=hg)==neg['mechanics'] and len(margins)==168
assert min(margins)>F(1,10**6)
root_audit=dict(parameter_interval=tbox,volume_interval=[iv.lo,iv.hi],
 centroid_intervals=[[z.lo,z.hi] for z in ig],mechanics=dict(S=sg,U=ug,H=hg),
 strict_primitive_count=168,certified_raw_absolute_margin=F(1,10**6))
report=dict(tag='C32_FOUR_TRIANGLE_FAN_PHYSICAL_BOUNDARY_V1',parent_assignment='minimum-0035',
 parent_sha256='8c1f1ed216fa9ce12e3141e4b177040958865e3dbbc42c88b8a7f4fcf68faf36',
 interval=[Z,TMAX],open_left=True,H_polynomials=H,vertex_numerators=N,vertex_denominators=D,
 H_triple_counts=triple_counts,volume_numerator=vn,volume_denominator=vd,
 selected_constant_matrix=C,ratio_root_bracket=rbox,physical_root_bracket=tbox,
 negative_control=neg,positive_control=pos,singular_body_interval_audit=root_audit,new_whole_C32_target_exclusions=[])
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [enc(v) for v in x]
 return x
out=(json.dumps(enc(report),sort_keys=True,separators=(',',':'))+'\n').encode()
Path('c32_fourfan.json').write_bytes(out)
print('C32_FOUR_FAN_CONTINUOUS_CONVEX_MAXIMAL_FACET_HULL_PASS',triple_counts)
print('ONE_ACTUAL_CENTROID_CONE_WEIGHT_LAMBDA_MATRIX_SQUARE_PASS')
print('NEGATIVE_MINOR',neg['minor'])
print('ALL_14_PROPER_PRINCIPAL_MINORS_POSITIVE_PASS')
print('RATIO_ROOT_BRACKET',*map(str,rbox))
print('PHYSICAL_SINGULAR_ROOT_BRACKET',*map(str,tbox))
print('NEGATIVE_CONTROL_S_U_H',*[len(neg['mechanics'][k]) for k in ['S','U','H']])
print('POSITIVE_CONTROL_S_U_H',*[len(pos['mechanics'][k]) for k in ['S','U','H']])
print('ALGEBRAIC_SINGULAR_BODY_STRICT_S_U_H_PASS',4,4,6,168,'MARGIN_GT_1E-6')
print('PROPER_VOLUME_DOES_NOT_ENSURE_FOUR_TRIANGLE_NONSINGULARITY_PASS')
print('NO_C32_GOMBOC_TYPE_OR_ROOT_EXCLUDED')
print('REPORT',len(out),hashlib.sha256(out).hexdigest())
src=Path(__file__).read_bytes();print('SOURCE',len(src),hashlib.sha256(src).hexdigest())
```

Expected complete transcript:

```text
C32_FOUR_FAN_CONTINUOUS_CONVEX_MAXIMAL_FACET_HULL_PASS [0, 27, 57]
ONE_ACTUAL_CENTROID_CONE_WEIGHT_LAMBDA_MATRIX_SQUARE_PASS
NEGATIVE_MINOR -29225402286904272323120130050768458025941435/44476389385373086840084719020220335744901748548
ALL_14_PROPER_PRINCIPAL_MINORS_POSITIVE_PASS
RATIO_ROOT_BRACKET 199480998299/200000000000 124675623937/125000000000
PHYSICAL_SINGULAR_ROOT_BRACKET 2399007863/1000000000000 299875983/125000000000
NEGATIVE_CONTROL_S_U_H 4 4 6
POSITIVE_CONTROL_S_U_H 4 4 6
ALGEBRAIC_SINGULAR_BODY_STRICT_S_U_H_PASS 4 4 6 168 MARGIN_GT_1E-6
PROPER_VOLUME_DOES_NOT_ENSURE_FOUR_TRIANGLE_NONSINGULARITY_PASS
NO_C32_GOMBOC_TYPE_OR_ROOT_EXCLUDED
REPORT 37861 e35023eb2e7da92dc8dd62763344a911987afada035d3712e265d68b7d701c1f
SOURCE 16394 6419d9a0f237bf13dd429c5a843c07e7d177d053a154a8c32b99e71cfe3fc238
```

Supplementary [source, full physical ledger, transcript, and report archive](sandbox:/mnt/data/C32_FOUR_TRIANGLE_FAN_PHYSICAL_BOUNDARY_V1.zip). The inline capsule is sufficient without this archive.
