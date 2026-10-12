# minimum-0160

AI research report · 2026-09-21 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# PROPER33_TWO_QUADRILATERAL_OBSTRUCTION_V1

## 1. Proved reduction and its boundary

**The entire proper33 sector with at most two unprotected polygonal facets, all of them quadrilaterals, contains no all-positive-endpoint full-class local maximum.** This excludes that genuine polygonal class in the negative-anchor complement. In fact the proof does not need the assumption `G(C)<=0 or G(D)<=0`.

Precisely, let

```
A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
T0=conv(A,B,C,D) subset P subset {x>=0,y>=0,ell>=0},
ell=a+(d-a)x+(c-a)y-(a-b)z,
a>b>0, c>0, d>0.
```

Assume P is a bounded full-dimensional polytope, its root `F=P intersect {ell=0}` has positive area, and its **actual maximal coordinate facets are exactly ABC and ABD**. Suppose every unprotected maximal facet is a triangle or a quadrilateral, and there are at most two quadrilaterals among these unprotected facets. Then P is not a Hausdorff local maximum of the original uniformly filled trace, even with ell held fixed, when competitors range over the full marked supporting-patch class. Consequently it is not a full marked-body/support-function joint maximum.

Only `x=0`, `y=0`, and `ell=0` are protected. The root may initially be an arbitrary polygon; it is not counted among the two quadrilaterals. The hypotheses do not initially bound the number of vertices, auxiliary positive-ell vertices, triangular facets, or root vertices.

Two reusable structural conclusions are proved en route:

1. When all four canonical marks are true vertices, every auxiliary vertex outside the protected facets lies on a genuine nonsimplicial unprotected facet. In particular, at a proper33 maximum every positive-ell auxiliary vertex lies on such a polygon.
2. At a proper33 all-positive maximum the root has at least two edges adjacent to genuine nonsimplicial unprotected facets. If there are exactly two such facets and both are quadrilaterals, all auxiliary vertices are on the root, and the root has three or four vertices. The entire remaining annular fan is then excluded by actual triangle reactions and a new whole-quadrilateral reaction obstruction.

Thus a surviving proper33 negative-anchor joint maximum must have at least two root-adjacent unprotected polygons, and either at least three unprotected nonsimplicial facets or an unprotected facet with at least five true vertices.

**The proper33 hypothesis is additional in the negative-anchor sector.** It has not been proved automatic there. Enlarged coordinate patches, redundant C/D marks, three or more free quadrilaterals, and free pentagons or larger facets are not eliminated by the main theorem. No universal `T<51/25`, no numerical bound on the supremum of arbitrary bodies in this nonclosed sector, and no finite termination of improving variations is asserted. The mechanical interval remains `34<=C_min<=622`.

## 2. Input closure and evidence

The complete new journal was read through line 1745/EOF, including the full literal parent payload and its source code. Its whole-file identity is 289,523 UTF-8 bytes, SHA-256 `a546e2111e8362d830c95c35dd7128761c8fff12ed5c2faab3564ee31dfb62d9`. The new cap-erasure proof was read through EOF: 10,958 bytes, SHA-256 `c23e9d7f45f6fa3436daac568156befa6dd5bd7d7c8d43205a47d23601a50337`.

The unchanged three analytic sources and earlier journal had already been read fully in this chat. The parent is the runtime-identified `minimum-0156`, declared SHA-256 `7432ccd712e9d766758a21f7ee4a1bfe2992a54e3e0cbc25154611566f8ac5aa`. Its simplicial-unprotected exclusion is inherited, not re-proved as a new result. No mathematical conflict between that literal payload and the new journal's description was found. The attached previous audit source/output also retain their stated 7,004/5,208-byte identities.

The new proof below is independent of a reconstruction of the historical <=16-vertex localization or the old covariance-control executables. Those missing historical executable sources are not dependencies of this result. The finite audit and actual-body control below have no external data-file dependency.

Evidence level: an analytic geometric reduction, a completely generated and exactly checked finite necessary fan cover, and an exactly integrated rational actual body with an exactly improving whole-quadrilateral plane motion. The two source-only executions described below agree byte for byte. This is not a proof-assistant formalization or a claim of external publication/priority.

## 3. Actual first variations and canonical reactions

Use the same uniformly filled body for every quantity:

```
s=a+b, alpha=a-b>0,
n=(s+c)x+(s+d)y,
V=int_P 1, E=int_P ell, N=int_P n,
g=(int_P (x,y,z))/V,
r=N/V, q=N/E, T=N/(6VE),
G=n-r-q ell.
```

In particular,

```
G(g)=-r,
G(A)=-r-qa < G(B)=-r-qb < 0,
partial_z G=q alpha>0.
```

The fixed-ell comparison is exact:

```
T(P')>T(P)
iff Delta int G > N Delta V Delta E/(VE).
```

At a full-class fixed-ell local maximum, every auxiliary true vertex has strictly positive G, and every genuine unprotected facet H satisfies

```
max_H G + 3 mean_H G <= 0.                         (3.1)
```

These are the supplied cap/thin-edge-cap and outward-pyramid variation results, not fixed-lattice stationarity. They imply that every unprotected facet contains a canonical mark. The supplied one-canonical rigidity theorem makes a one-mark facet a triangle `[X,u,v]`, with `G(u)=G(v)=-G(X)/3>0`.

For a true triangular facet and an auxiliary vertex z, the entire-plane displacement given by its barycentric coordinate lambda_z fixes every canonical mark in that triangle. Both signs are admissible, so

```
int_H G lambda_z = Area(H)[sum_(v in H) G(v)+G(z)]/12 = 0.  (3.2)
```

For `[X,Y,u]` this gives `G(u)=-(G(X)+G(Y))/2`.

For a genuine two-mark polygon H with marks X,Y, keep the **whole reaction**, rather than giving its integration triangles independent motions. The linear functional on affine normal displacements satisfies

```
int_H G h = -gamma_X h(X)-gamma_Y h(Y),
gamma_X,gamma_Y >= 0.                              (3.3)
```

Indeed, it vanishes on the kernel `h(X)=h(Y)=0`, because those whole-plane motions are two-sided. The two remaining evaluation coefficients are nonpositive, because the outward halfspace variations with nonnegative values at the marks are feasible. A positive common normalization of normal displacement is absorbed in gamma. The new quadrilateral argument uses (3.3) only for an affine h vanishing at both marks, together with the independent whole-facet condition (3.1).

A facet containing three canonical marks is not treated as ordinary. Its three reactions remain; the plane is not freely rotatable through three fixed noncollinear marks. The finite audit explicitly omits any triangle equations on ACD or BCD.

All these motions are available inside the full joint problem. We only need its fixed-ell subfamily; neither independent root moments nor projective covariance completions are substituted. The genuine positive-endpoint root-plane identities remain valid under the supplied hypotheses, but are not needed for the contradiction. In particular, none is imposed on the nonstationary control below or extended to a zero-endpoint boundary.

## 4. New auxiliary-vertex localization

### Lemma

Assume the preceding full-class local-maximum conditions, and assume all four canonical marks are true vertices. Let v be an auxiliary vertex on none of the protected facets. Then at least one incident maximal facet is nonsimplicial.

### Proof

Suppose all incident facets are triangles, and set `L=G(v)>0`. In the cyclic vertex link, consecutive neighbours cannot both be auxiliary: their triangle with v would have no canonical mark.

If an auxiliary neighbour u occurs, its adjacent triangles are ordinary. Therefore `G(u)=L` and the two adjacent canonical neighbours have value `-3L`. Along any consecutive block of canonical neighbours, equation (3.2) gives `G(X)+G(Y)=-2L`. Thus their values alternate between `-3L` and `+L`. Every neighbour consequently has G-value at most L.

If there are at least two auxiliary neighbours, there are at least two distinct true edge directions at level L. If there is exactly one auxiliary neighbour, the canonical block begins and ends at `-3L`; its pair-triangle relations require at least three canonical neighbours and an intervening `+L` neighbour. This again gives two distinct edge directions at level L. Distinct true edges from an extreme vertex cannot be collinear.

Since the tangent cone is generated by true incident edges, v is a global maximum of the affine G. The two independent level edges produce a two-dimensional exposed face of constant positive G. This is an unprotected facet, because v belongs to no protected facet. It violates (3.1).

It remains that every neighbour of v is canonical. There are three or four neighbours. No link edge can join A and B: AB already belongs to both coordinate facets, and a third facet cannot contain that true edge.

With four neighbours, A and B are opposite in the link, so comparing the pair equations across AC and CB gives `G(A)=G(B)`, impossible.

With three neighbours, they are A,C,D or B,C,D. The three pair equations make all three canonical values equal to `-L`.

For A,C,D, the true facet ACv has plane `z=eta x`. Containment of B fixes its inward side to `z>=eta x`; D is strictly off that facet, so `eta<0`. As `x(v)>0`, `z(v)<0`. But G equals `-L` on z=0 and has positive z derivative, contradicting `G(v)=L>0`.

For B,C,D, equality of the three canonical values gives

```
c=d=k,   q(k-b)=s+k>0,   hence k>b.
```

Write `h=x+y+z-1`. G is `-L+q alpha h`, so `h(v)>0`. The vertex is simple with neighbours B,C,D. Every other point of P lies in its simplicial tangent cone; write its displacement as a nonnegative combination of `B-v,C-v,D-v`. Every other true vertex except B,C,D has coefficient sum greater than one: otherwise it would lie in the tetrahedron `conv(v,B,C,D)` and fail to be extreme. Hence all other true vertices have `h<=0`.

On that entire collection of vertices,

```
ell=b+(k-b)(x+y)-alpha h >= b>0.
```

At most v could be a zero of ell among the vertices. This cannot support a positive-area root facet. The contradiction proves the lemma.

In proper33 there are no auxiliary vertices on either coordinate facet. The lemma therefore places every positive-ell auxiliary vertex on a genuine free polygon. This is stronger than merely placing it on a special facet, which could have been a two-mark triangle.

## 5. Two quadrilaterals force a small actual root-only body

The root is disjoint from the coordinate triangles because all their endpoint values are positive. Every root edge whose other facet is triangular is therefore an ordinary one-mark triangle. Its two endpoints have equal G by (3.2).

G is nonconstant on the root plane: there it is `n-r`; a nonzero horizontal gradient of n cannot be proportional to the gradient of ell, whose z component is nonzero. A nonconstant affine function on a polygon cannot change along only one edge of the cycle. Thus at least two root edges have nonsimplicial other facets. One free facet meets the root in at most one edge.

Under the main theorem's hypothesis, there are consequently exactly two free quadrilaterals, both root-adjacent. Each consists of two root vertices and exactly two canonical vertices. The canonical pair is its opposite true edge. A third canonical mark or a positive-ell auxiliary vertex would require a fifth true vertex in that facet.

The localization lemma now leaves **all** auxiliary vertices on the root. Two consecutive ordinary root edges would put three true root vertices on a single affine G-level line, which is impossible. With only two exceptional root edges, the root has `k=3` or `k=4` vertices. Hence

```
P=conv(A,B,C,D,F),
(V_true,E_true,F_true)=(7,13,8) or (8,15,9).
```

These are consequences at the proposed maximum, not restrictions imposed on the original class.

## 6. A whole-quadrilateral positive-edge obstruction

### Lemma

Let H be a true unprotected quadrilateral with cyclic vertices `X,Y,R,U`, where X,Y are its two canonical marks and R,U are auxiliary. If

```
G(Y)=G(R)=L>0,
```

then H cannot occur at a full-class fixed-ell local maximum.

### Proof with its exact area identity

If `G(X)>=0`, all four vertex values are nonnegative and some are positive, immediately contradicting (3.1). Thus set `G(X)=-gamma<0`.

The true edge YR is a level line of G. Convexity and the negative value at X imply `0<G(U)<L`. Use affine coordinates on the actual facet plane:

```
X=(0,0), Y=(1,0), R=(1,h), U=(t,ht+e),
h>0, e>0, 0<t<1,
G=-gamma+(gamma+L)xi.
```

Here `eta=0` is the true canonical edge XY. The whole-plane tilt with affine displacement eta is admissible in both directions and fixes both marks. Consequently

```
int_H G eta=0,
kappa:=gamma/(gamma+L)=(int_H xi eta)/(int_H eta).
```

Put `mu=(int_H xi)/Area(H)`. The whole-facet spike condition requires

```
4 kappa-3 mu-1 >= 0.
```

But direct uniform area integration over H gives

```
4 (int_H xi eta)/(int_H eta) - 3 (int_H xi)/Area(H) - 1
 = e(e+2h)(e+ht)(t-1)
   /[(e+h)(e^2+eht+eh+h^2)] < 0.                    (6.1)
```

For completeness, the four integrals used are

```
Area=(e+h)/2,
int xi=(et+e+2h)/6,
int eta=(e^2+eht+eh+h^2)/6,
int xi eta=(2e^2t+e^2+2eht^2+2eht+2eh+3h^2)/24.
```

A constant Jacobian from the affine plane chart cancels from the ratios. The two triangles XYR and XRU are used **only to integrate the actual quadrilateral**; neither triangle is moved independently.

This also gives an improving-variation alternative. If `int_H G eta` is nonzero, choose the improving sign of the actual plane tilt. If it vanishes, the spike residual is the explicit positive quantity

```
max_H G+3 mean_H G
=(gamma+L)e(e+2h)(e+ht)(1-t)
 /[(e+h)(e^2+eht+eh+h^2)] > 0.
```

A sufficiently small actual outward pyramid at a relative-interior point near the maximizing edge then strictly raises T by the exact comparison. There is no uniform gap as the quadrilateral degenerates, and none is claimed.

## 7. Complete finite ordinary-level fan cover

### Why the list is exhaustive for actual bodies

Remove the root disk and the fixed canonical disk from the polyhedral sphere. The latter is initially `ABC union ABD`. At most one additional three-canonical facet can occur: ACD and BCD cannot both occur, because their halfspaces together with x,y>=0 would give `P=T0`, contradicting the root.

If such a facet occurs, include it in the canonical disk. The canonical boundary cycle is then one of

```
no three-mark facet: A,C,B,D;
ACD present:         B,C,D;
BCD present:         A,C,D.
```

There is no omitted internal CD edge in the first case. Indeed, write f3 for the number of free triangular facets. Euler's formula and edge counting, with k root vertices and exactly two free quadrilaterals, give `f3=k`. Exactly `k-2` of these triangles have two root vertices. Therefore there are two two-canonical triangles when no three-mark facet occurs, or one when such a facet occurs. The four canonical boundary edges already consume all four free canonical-edge incidences in the no-base case; any additional CD edge would consume two more. In the base case those two incidences are exactly the true CD edge shared with the base triangle.

Every remaining annular face has exactly two canonical-to-root edges. The annular face-adjacency graph across these edges is connected and has degree two, hence is a single cycle. Traversing it gives a word in three symbols:

```
Q: quadrilateral (c_i,c_(i+1),r_(j+1),r_j); advance i,j.
P: triangle      (c_i,c_(i+1),r_j);         advance i.
R: triangle      (c_i,r_(j+1),r_j);         advance j.
```

If m is the canonical cycle length, the word contains exactly two Q's, `m-2` P's and `k-2` R's. Choose the first canonical vertex of the displayed cycle and label the root endpoint of a starting cross edge as r0. Thus enumeration of every multiset permutation covers every actual annulus, without assuming a special metric realization or a particular ordering of G-levels.

The source removes duplicate labelled face sets and rejects only necessary incidence failures: wrong edge multiplicities/Euler characteristic, improper intersections of maximal faces, and failure of three-connectivity. Retaining other unrealizable configurations is harmless. The result is a finite **overcover**, not 175 realized bodies or 175 combinatorial isomorphism classes.

### What is checked in each case

Let the vector of vertex G-values be gval. Build an integer matrix E whose rows are exactly (3.2), one for each auxiliary vertex of each genuine free triangle. Neither the root nor coordinate or three-canonical facets receive a fictitious equation. Compute the complete rational nullspace N of E.

Every retained case has one of two exact contradictions:

- A quadrilateral has an adjacent canonical vertex X and root vertex R for which `N[X,:]=N[R,:]`. Thus the actual triangle equations force `G(X)=G(R)>0` and the whole-quadrilateral lemma applies. If X is A or B the sign contradiction is already immediate.
- The equations contradict just `G(A)<G(B)<0` and positivity at every root vertex. Homogeneously rescale these finitely many strict gaps to write `I gval<=-1`. The source constructs nonnegative rational lambda with sum one and `lambda^T I N=0`. Since `E gval=0`, this gives `0=lambda^T I gval<=-1`.

**No sign constraint on G(C) or G(D) is used.** The exact cover is:

|Root size|Three-mark facet|Forced positive edge|Strict-sign contradiction|Total|
|---:|---|---:|---:|---:|
|3|none|15|10|25|
|3|ACD|8|0|8|
|3|BCD|8|0|8|
|4|none|54|30|84|
|4|ACD|25|0|25|
|4|BCD|25|0|25|
|**Total**||**135**|**40**|**175**|

The source records every complete face list, every integer triangle equation, and the selected exact certificate. It independently checks the relevant row-span identity by rank as well as by nullspace multiplication. A failed search is not used as a certificate; all 175 cases return a verified contradiction.

As a representative geometric mechanism, take root PQR, free quadrilaterals BCPR and BDQR, free triangles CPQ and CDQ, and base ACD. The triangle equations give `G(P)=G(Q)=-G(C)/3` and `G(Q)=-(G(C)+G(D))/2`, hence `G(D)=G(Q)>0`. The genuine quadrilateral BDQR has the forbidden positive edge DQ. Its whole reaction, not an integration-diagonal motion, is essential to the final contradiction.

This completes the main theorem. At every excluded actual body, failure of one of the necessary stationarity steps gives a cap, a genuine plane variation, or a whole-facet outward-pyramid improvement. It is not necessary, and is not asserted, that the improvement stays in the two-quadrilateral class.

## 8. New exact actual-body control and whole-polygon improvement

The excluded geometric class is nonempty, including bodies with a genuinely negative canonical G and **strictly positive G at every auxiliary vertex**. The following rational control is distinct from the parent's nine-vertex control.

Use endpoints

```
(a,b,c,d)=(1,1/10,1/100,1/5),
ell=1-(4/5)x-(99/100)y-(9/10)z,
n=(111/100)x+(13/10)y.
```

Besides A,B,C,D, take

```
P=(313703/2505450,151046703/167030000,13703/2700000),
Q=(2968477/2417820,5386297/402970000,13703/2700000),
R=(2/3,1/100,13703/27000).
```

All three are root vertices. In the input order A,B,C,D,P,Q,R, the maximal facet cycles are

```
ABC, ABD, ACD, CDQ, CPQ, BCPR, BDQR, PQR.
```

Its true f-vector is `(7,13,8)`, the coordinate facets are exactly ABC and ABD, and the two unprotected quadrilaterals are exactly BCPR and BDQR. Actual uniform integration gives

```
V=238757899714842373/1090390881420000000,
E=25318800491841114373/436156352568000000000,
N=10955460639579898617855248173397/73392115696536080322000000000000,
T=11831897490746290507283668027268760000/
  6045063628731102534617451664359727129
 =1.95728253951065216... .
```

Here `G(D)=-0.0860121054027...<0<G(C)=0.592565899897...`; every auxiliary G is positive. These signs are checked as rational inequalities, not accepted from the decimals. It already lies in `0<=ell<=1`, so this control is not a high-level overshoot example. No local optimality is asserted: the ordinary triangle reactions also need not hold.

Move the **entire actual plane** of BCPR. In normalized form its slack is `H=1-y-z+kx`, where `k=-13027/18000`. Replace k by `k-1/10000`, leaving every other actual facet inequality fixed. Equivalently replace only

```
18000-13027x-18000y-18000z >= 0
```

by

```
11250-8143x-11250y-11250z >= 0.
```

The exact whole-quadrilateral first variation is negative with respect to increasing k:

```
int_BCPR G x dA/|grad H|
=-538971807107659008043645929484304067537877549127522469527/
  611652934231050156133601778392035790987483649495753000000000 <0.
```

The specified negative step gives an actual uniformly filled convex competitor. Its true f-vector remains `(7,13,8)`, it retains proper33 and the positive-area root, and still has `G(D)<0<G(C)` with all auxiliary G positive. Its trace is

```
T_child=3239491567985779279136842679501028384800/
        1655095577334922382192822759299082819849
       =1.95728368340038236... .
```

The exact gain is strictly positive, approximately `1.14388973020221386e-6`. This is a genuine polygon-plane improvement, not an independent modification of tetrahedron masses or of integration triangles.

The audit reconstructs all supporting planes from triples, removes nonvertices, integrates using two distinct interior-apex fans, and independently reconstructs the changed halfspace intersection. Its reconstructed hull has exactly the changed halfspaces, verifying the claimed bounded intersection. The control is below `51/25`; no mechanical S/U/H census or monostatic construction is claimed.

## 9. Complete self-contained recovery capsule

Save the following complete source as `two_quad_obstruction_audit.py`, UTF-8/LF with its final newline. It contains the entire fan generator/verifier, the symbolic whole-quadrilateral identity, the exact actual-body generator, the supporting-triple/true-facet reconstruction, both uniform moment integrations, and the whole-plane child construction. No parent coordinate file, coefficient table, floating solver, random seed, or external input is required.

Runtime actually used: **CPython 3.13.5, SymPy 1.14.0**, assertions enabled; remaining dependencies are Python standard-library modules. The exact non-default geometric parameters are embedded, including `rx=2/3`, `ry=t=1/100`, and plane step magnitude `1/10000`.

```
python two_quad_obstruction_audit.py > two_quad_obstruction_audit.out
sha256sum two_quad_obstruction_audit.py two_quad_obstruction_audit.out
```

Expected source: **14,264 bytes**, SHA-256 `af56220f3a1438f1e7ac065b371a98d24e9fa60bf91c702c58e7dffd28f587c4`.

Expected complete stdout: **60,732 bytes**, SHA-256 `5542ed5a04ed2c6724a9cc195a95d01a95642642d8162825759f358fcdfc4ace`.

The first stdout line is the complete exact JSON report, including all 175 cases and every new actual coordinate/plane/moment. The terminal markers are


[Encoded source block omitted; the code in this passage is incomplete.]


A normal execution and a second execution in a fresh directory containing only the source both completed; their full outputs are byte-identical. Symbolic checks and rational finite certificates do not by themselves formalize the geometric exhaustiveness/admissibility arguments; those are supplied in Sections 3–7.

```python
"""PROPER33_TWO_QUADRILATERAL_OBSTRUCTION_V1: exact finite audit.
CPython 3.13.5, SymPy 1.14.0, assertions enabled. No external inputs or RNG.
python two_quad_obstruction_audit.py > two_quad_obstruction_audit.out
"""
from collections import Counter
from itertools import combinations, permutations
from math import gcd, lcm
import json
import sympy as S

Q = S.Rational

def cycle(f):
    f = tuple(f)
    r = f[::-1]
    return min([f[i:]+f[:i] for i in range(len(f))]
               + [r[i:]+r[:i] for i in range(len(f))])

def edges(f):
    return {tuple(sorted((f[i], f[(i+1) % len(f)])))
            for i in range(len(f))}

def valid(fs, n):
    if len(set(fs)) != len(fs):
        return False
    ee = [edges(f) for f in fs]
    count = Counter(e for es in ee for e in es)
    if any(v != 2 for v in count.values()):
        return False
    if n-len(count)+len(fs) != 2:
        return False
    for i, j in combinations(range(len(fs)), 2):
        common = set(fs[i]) & set(fs[j])
        if len(common) > 2:
            return False
        if len(common) == 2:
            e = tuple(sorted(common))
            if e not in ee[i] or e not in ee[j]:
                return False
    # Necessary three-connectivity, not a claim of metric realizability.
    removals = [()] + list(combinations(range(n), 1))
    removals += list(combinations(range(n), 2))
    for removed in removals:
        left = set(range(n))-set(removed)
        reached = {min(left)}
        while True:
            new = reached | {b for a,b in count if a in reached and b in left}
            new |= {a for a,b in count if b in reached and a in left}
            if new == reached:
                break
            reached = new
        if reached != left:
            return False
    return True

def fan_inputs():
    seen = set()
    for k in (3, 4):
        for base, cc in [('none',(0,2,1,3)), ('ACD',(1,2,3)),
                         ('BCD',(0,2,3))]:
            m = len(cc)
            words = sorted(set(permutations('QQ'+'P'*(m-2)+'R'*(k-2))))
            for word in words:
                fixed = [cycle((0,1,2)), cycle((0,1,3)),
                         cycle(tuple(range(4,4+k)))]
                if base != 'none':
                    fixed += [cycle((0,2,3) if base == 'ACD' else (1,2,3))]
                fs = fixed[:]
                i = j = 0
                for letter in word:
                    x,y = cc[i % m],cc[(i+1) % m]
                    u,v = 4+j % k,4+(j+1) % k
                    if letter == 'Q':
                        f = (x,y,v,u)
                        i += 1
                        j += 1
                    elif letter == 'P':
                        f = (x,y,u)
                        i += 1
                    else:
                        f = (x,v,u)
                        j += 1
                    fs.append(cycle(f))
                assert i == m and j == k
                fs = tuple(sorted(fs))
                key = (k,fs)
                if key in seen or not valid(fs,4+k):
                    continue
                seen.add(key)
                rows = []
                for f in fs:
                    if len(f) != 3 or f in fixed:
                        continue
                    for z in f:
                        if z < 4:
                            continue
                        row = [0]*(4+k)
                        for w in f:
                            row[w] += 1
                        row[z] += 1
                        rows.append(row)
                yield k,base,''.join(word),fs,S.Matrix(rows)

def inequalities(n):
    rows = []
    row = [0]*n
    row[0],row[1] = 1,-1
    rows.append(row)  # GA-GB <= -1 after positive homogeneous rescaling.
    row = [0]*n
    row[1] = 1
    rows.append(row)  # GB <= -1.
    for i in range(4,n):
        row = [0]*n
        row[i] = -1
        rows.append(row)  # Every root value >= 1.
    return S.Matrix(rows)

def sign_certificate(H):
    for size in range(1,min(H.rows,H.cols+1)+1):
        for ids in combinations(range(H.rows),size):
            null = H[list(ids),:].T.nullspace()
            if len(null) != 1:
                continue
            v = null[0]
            if all(x <= 0 for x in v):
                v = -v
            if all(x >= 0 for x in v) and sum(v) > 0:
                v = v/sum(v)
                assert v.T*H[list(ids),:] == S.zeros(1,H.cols)
                return ids,v
    raise AssertionError('UNCOVERED_SIGN_CASE')

def finite_audit():
    records = []
    stats = Counter()
    for k,base,word,fs,E in fan_inputs():
        basis = E.nullspace()
        N = S.Matrix.hstack(*basis) if basis else S.zeros(E.cols,0)
        assert E*N == S.zeros(E.rows,N.cols)
        assert E.rank()+N.cols == E.cols and N.rank() == N.cols
        hits = []
        for f in fs:
            if len(f) != 4 or len(set(f) & set(range(4))) != 2:
                continue
            for x,y in sorted(edges(f)):
                if x < 4 <= y and N[x,:] == N[y,:]:
                    hits.append((f,x,y))
        cert = {}
        if hits:
            status = 'positive_edge_hinge'
            f,x,y = hits[0]
            equality = S.zeros(1,E.cols)
            equality[0,x],equality[0,y] = 1,-1
            assert equality*N == S.zeros(1,N.cols)
            assert E.col_join(equality).rank() == E.rank()
            cert = dict(facet=f,canonical=x,root=y)
        else:
            status = 'strict_sign_contradiction'
            I = inequalities(E.cols)
            ids,v = sign_certificate(I*N)
            row = v.T*I[list(ids),:]
            assert row*N == S.zeros(1,N.cols)
            assert E.col_join(row).rank() == E.rank()
            assert all(x >= 0 for x in v) and sum(v) == 1
            # Thus 0 = row*g <= -1, using only the displayed strict signs.
            cert = dict(inequality_indices=ids,weights=[str(x) for x in v])
        stats[(k,base,status)] += 1
        records.append(dict(k=k,base=base,word=word,faces=fs,
                            equations=[[int(x) for x in row] for row in E.tolist()],status=status,certificate=cert))
    expected = {(3,'none','positive_edge_hinge'):15,
                (3,'none','strict_sign_contradiction'):10,
                (3,'ACD','positive_edge_hinge'):8,
                (3,'BCD','positive_edge_hinge'):8,
                (4,'none','positive_edge_hinge'):54,
                (4,'none','strict_sign_contradiction'):30,
                (4,'ACD','positive_edge_hinge'):25,
                (4,'BCD','positive_edge_hinge'):25}
    assert dict(stats) == expected and len(records) == 175
    return dict(count=175,hinges=135,sign_contradictions=40,
                counts=[[k,b,s,v] for (k,b,s),v in sorted(stats.items())],
                records=records)

def quadrilateral_identity():
    h,e,t = S.symbols('h e t', positive=True)
    pts = [S.Matrix(p) for p in ((0,0),(1,0),(1,h),(t,h*t+e))]
    area = ix = iy = ixy = S.S(0)
    for ids in ((0,1,2),(0,2,3)):
        p = [pts[i] for i in ids]
        ar = S.det(S.Matrix.hstack(p[1]-p[0],p[2]-p[0]))/2
        x,y = [z[0] for z in p],[z[1] for z in p]
        area += ar
        ix += ar*sum(x)/3
        iy += ar*sum(y)/3
        ixy += ar*(sum(x)*sum(y)+sum(u*v for u,v in zip(x,y)))/12
    denominator = (e+h)*(e**2+e*h*t+e*h+h**2)
    rhs = e*(e+2*h)*(e+h*t)*(t-1)/denominator
    assert S.factor(4*ixy/iy-3*ix/area-1-rhs) == 0
    # Rational planar integration check; explicitly not a body.
    sub = {h:1,e:1,t:Q(3,4)}
    kappa = (ixy/iy).subs(sub)
    mean = (ix/area).subs(sub)-kappa
    assert kappa == Q(27,40) and mean == -Q(1,20)
    assert 1-kappa+3*mean == Q(7,40)
    return dict(area=str(S.factor(area)),Ix=str(S.factor(ix)),
                Iy=str(S.factor(iy)),Ixy=str(S.factor(ixy)),
                signed_gap=str(S.factor(rhs)),
                planar_check='NOT_A_THREE_DIMENSIONAL_BODY')

# Independent exact supporting-triple reconstruction for one actual control.
MARKS = [S.Matrix(p) for p in ((0,0,0),(0,0,1),(0,1,0),(1,0,0))]
a,b,c,d = S.S(1),Q(1,10),Q(1,100),Q(1,5)
alpha = S.Matrix((d-a,c-a,b-a))

def ell(p):
    return a+alpha.dot(p)

def nfun(p):
    return (a+b+c)*p[0]+(a+b+d)*p[1]

def primitive(h):
    hh = list(map(S.Rational,h))
    den = lcm(*(int(x.q) for x in hh))
    nums = [int(x*den) for x in hh]
    g = gcd(*nums)
    assert g > 0
    return tuple(x//g for x in nums)

def slack(h,p):
    return S.Matrix(h[:3]).dot(p)+h[3]

def hull(points):
    planes = set()
    for i,j,k in combinations(range(len(points)),3):
        p,u,v = points[i],points[j],points[k]
        normal = (u-p).cross(v-p)
        if normal == S.zeros(3,1):
            continue
        h = list(normal)+[-normal.dot(p)]
        vals = [slack(h,x) for x in points]
        if min(vals) >= 0:
            pass
        elif max(vals) <= 0:
            h = [-x for x in h]
        else:
            continue
        planes.add(primitive(h))
    planes = sorted(planes)
    keep = []
    for p in points:
        active = [h[:3] for h in planes if slack(h,p) == 0]
        if len(active) >= 3 and S.Matrix(active).rank() == 3:
            keep.append(tuple(p))
    pts = [S.Matrix(p) for p in sorted(set(keep))]
    fs = [tuple(i for i,p in enumerate(pts) if slack(h,p) == 0) for h in planes]
    assert all(len(f) >= 3 for f in fs)
    return pts,planes,fs

def face_edges(f,fs):
    ee = sorted({tuple(sorted(set(f)&set(g))) for g in fs
                 if g != f and len(set(f)&set(g)) == 2})
    assert len(ee) == len(f)
    assert all(sum(i in e for e in ee) == 2 for i in f)
    return ee

def moments(pts,fs,o):
    V = S.S(0)
    J = S.zeros(3,1)
    for f in fs:
        center = sum((pts[i] for i in f),S.zeros(3,1))/len(f)
        for i,j in face_edges(f,fs):
            p,q = pts[i],pts[j]
            w = abs(S.det(S.Matrix.hstack(center-o,p-o,q-o)))/6
            assert w > 0
            V += w
            J += w*(o+center+p+q)/4
    return V,J

def body_audit(points):
    pts,hs,fs = hull(points)
    assert all(all(slack(h,p) >= 0 for h in hs) for p in MARKS)
    assert all(p[0] >= 0 and p[1] >= 0 and ell(p) >= 0 for p in pts)
    V,J = moments(pts,fs,sum(MARKS,S.zeros(3,1))/4)
    assert (V,J) == moments(pts,fs,S.Matrix([Q(1,5)]*3))
    E = a*V+alpha.dot(J)
    N = (a+b+c)*J[0]+(a+b+d)*J[1]
    assert min(V,E,N) > 0
    G = lambda p: nfun(p)-N/V-(N/E)*ell(p)
    assert G(J/V) == -N/V
    roots = tuple(i for i,p in enumerate(pts) if ell(p) == 0)
    assert len(roots) >= 3 and roots in fs
    for coord,ids in ((0,(0,1,2)),(1,(0,1,3))):
        face = {tuple(p) for p in pts if p[coord] == 0}
        assert face == {tuple(MARKS[i]) for i in ids}
    es = set(e for f in fs for e in face_edges(f,fs))
    assert len(pts)-len(es)+len(fs) == 2
    report = dict(vertices=[[str(x) for x in p] for p in pts],
                  planes=hs,faces=fs,f_vector=[len(pts),len(es),len(fs)],
                  V=str(V),J=[str(x) for x in J],E=str(E),N=str(N),
                  T=str(N/(6*V*E)),G_marks=[str(G(p)) for p in MARKS],
                  G_aux=[str(G(p)) for p in pts if p not in MARKS])
    return pts,hs,fs,V,E,N,G,report

def intersection(hs):
    vv = set()
    for ids in combinations(range(len(hs)),3):
        H = S.Matrix([hs[i][:3] for i in ids])
        if H.det() == 0:
            continue
        p = H.inv()*S.Matrix([-hs[i][3] for i in ids])
        if all(slack(h,p) >= 0 for h in hs):
            vv.add(tuple(p))
    return [S.Matrix(v) for v in sorted(vv)]

def actual_control():
    rx,ry,t = Q(2,3),Q(1,100),Q(1,100)
    R = S.Matrix((rx,ry,(a+(d-a)*rx+(c-a)*ry)/(a-b)))
    k = (R[2]-1+ry)/rx
    h = (R[2]-1+rx)/ry
    ux = c/((1-d)+(1-c)*k)
    vy = d/((1-c)+(1-d)*h)
    U,V0 = S.Matrix((ux,1+k*ux,0)),S.Matrix((1+h*vy,vy,0))
    P,Q0 = (1-t)*U+t*R,(1-t)*V0+t*R
    data = body_audit(MARKS+[P,Q0,R])
    pts,hs,fs,V,E,N,G,parent = data
    assert parent['f_vector'] == [7,13,8]
    assert G(MARKS[3]) < 0 < G(MARKS[2])
    assert all(G(p) > 0 and ell(p) == 0 for p in (P,Q0,R))
    assert all(p[0] > 0 and p[1] > 0 for p in (P,Q0,R))
    quads = [f for f in fs if len(f) == 4]
    assert len(quads) == 2
    old = primitive((k,-1,-1,1))
    assert old in hs
    f = fs[hs.index(old)]
    assert len(f) == 4
    # Projection to (x,y) gives dA/|grad H|=dxdy for H=kx-y-z+1.
    # Compute the actual whole-quadrilateral reaction int G*x dxdy.
    center = sum((pts[i] for i in f),S.zeros(3,1))/len(f)
    reaction = S.S(0)
    for i,j in face_edges(f,fs):
        pp = [center,pts[i],pts[j]]
        ar = abs(S.det(S.Matrix.hstack((pp[1]-pp[0])[:2,0],
                                      (pp[2]-pp[0])[:2,0])))/2
        gg,xx = [G(p) for p in pp],[p[0] for p in pp]
        reaction += ar*(sum(gg)*sum(xx)+sum(g*x for g,x in zip(gg,xx)))/12
    assert reaction != 0
    step = S.sign(reaction)*Q(1,10000)
    new = primitive((k+step,-1,-1,1))
    hh = list(hs)
    hh[hs.index(old)] = new
    child_data = body_audit(intersection(hh))
    cp,ch,cf,cV,cE,cN,cG,child = child_data
    assert set(ch) == set(hh)  # These same halfspaces bound this actual hull.
    assert cG(MARKS[3]) < 0 < cG(MARKS[2])
    assert all(cG(p) > 0 and ell(p) == 0 for p in cp if p not in MARKS)
    gain = cN/(6*cV*cE)-N/(6*V*E)
    assert gain > 0
    return dict(status='ACTUAL_UNIFORM_PROPER33_NOT_A_LOCAL_MAXIMUM',
                input=dict(endpoints=list(map(str,(a,b,c,d))),
                           rx=str(rx),ry=str(ry),t=str(t)),
                parent=parent,child=child,
                tilt=dict(old_plane=old,new_plane=new,step=str(step),
                          whole_quad_reaction=str(reaction),
                          derivative=str(reaction/(6*V*E)),gain=str(gain)))

if __name__ == '__main__':
    report = dict(quadrilateral=quadrilateral_identity(),
                  finite=finite_audit(),actual_control=actual_control())
    print(json.dumps(report,sort_keys=True,separators=(',',':')))
    print('WHOLE_QUADRILATERAL_PASSIVE_POSITIVE_EDGE_IDENTITY_PASS')
    print('ALL_175_ANNULAR_FAN_OVERCOVERS_135_HINGE_40_SIGN_PASS')
    print('ACTUAL_PROPER33_NEGATIVE_ANCHOR_TWO_QUAD_CONTROL_PASS')
    print('ACTUAL_WHOLE_QUADRILATERAL_PLANE_TILT_STRICT_GAIN_PASS')
    print('PROPER33_TWO_QUADRILATERAL_OBSTRUCTION_EXACT_AUDIT_PASS')
```

Convenience copies, not recovery dependencies: complete source (`two_quad_obstruction_audit.py`) and complete exact output (`two_quad_obstruction_audit.out`).

## 10. Most useful continuation and unresolved alternatives

The negative-anchor maximum has not been reduced to proper33. Resolving enlarged coordinate patches or a redundant opposite canonical mark remains a distinct task; the auxiliary-vertex lemma above deliberately requires true canonical vertices and does not silently settle those cases.

Inside proper33, the next smallest surviving structures are three genuine free quadrilaterals, or two root-adjacent polygons with at least one pentagon. The new localization lemma forces every positive-ell auxiliary vertex onto those actual polygons, and the whole-quadrilateral identity gives a concrete test whenever a triangular part of the fan forces equality between a positive canonical value and its adjacent root value. A three-mark pentagon remains a genuine reaction exception; no fictitious affine tilt through three noncollinear fixed marks is available. The finite annulus method applies directly only after the actual root-only reduction has been justified.

For any surviving full joint maximum with `T>=tau`, the supplied new cap theorem adds the genuine common-body restriction

```
0<=ell<=H_tau,
H_tau=max(a,b,c,d,(a+c+d)/tau).
```

This remains available in the negative-anchor branch. Its stronger `ell<=a` conclusion requires `G(C),G(D)>=0` and has not been imported here. Clipping preserves the root and proper33 when initially present, but need not preserve a prescribed G-sign sector.

The most direct next calculation is the full coupled area-reaction system of a three-quadrilateral proper33 fan, allowing an off-root auxiliary vertex only where the new localization permits it. The alternative that a remaining polygonal class supports `T>=51/25` is unresolved. No abstract moment completion, separately optimized root polygon, or auxiliary annular fan has been identified with a realized stationary uniform body.
