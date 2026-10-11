# minimum-0288

Historical AI scientific report · saved 2026-09-27 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# CUT_STACK_DEEP_DEFICIT_THREE_ARROW_U2_V1

## 1. New mechanical theorem

There is a new, explicit **all-root exclusion in the deep-cut part of the six-cut complement**. It covers every positive base parameter, every stacking height, and six independently varying cuts. The proof uses only **three selected true arrows, each with coefficient 1**, rather than a larger numerical stress library.

Retain the native construction and labels from the accepted parent:

\[
\begin{aligned}
B_-&=(-1,0,0),&B_+&=(1,0,0),\\
B_0&=(0,-b,0),&B_1&=(0,1,0),&B_2&=(0,0,1),\\
L_j&=B_-+f_j(B_j-B_-),&R_j&=B_++k_j(B_j-B_+),\\
C&=(L_0+L_1+L_2)/3,&S&=tB_-+(1-t)C.
\end{aligned}
\]

The vertex order is \((B_0,B_1,B_2,L_0,L_1,L_2,R_0,R_1,R_2,S)\). All parameters retain their actual native meaning; this is not the older symmetric small-cut pyramid family.

Write

\[
\alpha_j=1-f_j,\qquad \gamma_j=1-k_j,\qquad
 d=\max_j\{\alpha_j,\gamma_j\}.
\]

### Theorem

Suppose

\[
b>0,\qquad 0<t<1,\qquad 0<f_j,k_j<1,
\]

and

\[
\boxed{
576d+128(1-t)\sum_{j=0}^2\alpha_j
       +192\sum_{j=0}^2\gamma_j\le3t.}
\tag{1}
\]

Uniformly fill the actual convex hull and subtract its own volume centroid. Then **every complete rooted true-edge weak-arrow tree is impossible for every nonzero PSD matrix**. In particular, every physical SPD metric has at least two strict unstable vertices, including when incidental physical weak equilibria occur elsewhere.

A simpler rectangular sufficient condition, with all six cuts independent, is

\[
\boxed{
1-\frac{t}{128(4-t)}\le f_j,k_j<1
\quad(j=0,1,2),\qquad b>0,\quad0<t<1.}
\tag{2}
\]

The closed lower endpoints in (1) and (2), all equal-deficit ties, and arbitrary physical conditioning are included.

There is an affine-invariant quantitative form. Let \(\Sigma_P\) be the actual uniform covariance of the body, and let

\[
A_{ij}=\operatorname{sym}\bigl((Y_i-g)(Y_j-Y_i)^T\bigr).
\]

For **every** selected rooted true-edge tree, three arrows \(i_\nu\to j_\nu\) belonging to that tree satisfy

\[
\boxed{
-\sum_{\nu=1}^3 A_{i_\nu j_\nu}
\succ \frac5{128}\Sigma_P.}
\tag{3}
\]

Consequently, for every nonzero PSD physical matrix M,

\[
\boxed{
\frac13\sum_{\nu=1}^3
(Y_{i_\nu}-g)^TM(Y_{j_\nu}-Y_{i_\nu})
< -\frac5{384}\operatorname{tr}(M\Sigma_P).}
\tag{4}
\]

These coefficients are independent dual arrow multipliers, not physical masses or centroid-balanced source loads.

This is a restricted but genuine interior-domain theorem. It is **disjoint from the previously certified six-cut box**: in (2), every cut exceeds \(383/384\), whereas the old box has \(k_0\le6/25\). The new region is a deep-cut cone, not the broad middle-cut region originally sought. In particular, this handoff does not certify the middle cube \([.45,.55]^6\), the full native family, or a new physical survivor.

## 2. Authority, retained context, and verification status

The complete new notebook and literal parent reading from the preceding interrupted attempt are retained. The current notebook is 313341 bytes, 1521 lines, SHA-256

`0f3d7bc6f429b253eeae4ea38870510d28bb0d5a7615526b608f063cb057a481`.

The immediate literal parent is

`minimum-0286`, SHA-256

`2e28f07cc57fd27c8a5e3a538577ba23b89fa14cb85f59fbe85be8967ba060d4`.

Its `CUT_STACK_MAX_DEFICIT_POLYNOMIAL_INTERIOR_ATLAS_V1` remains an analytical reduction, not an interior exclusion. The earlier mechanically accepted parent remains

`minimum-0285`, SHA-256

`383ab22af4a74c7ba8d2604d95d2f259b60928871a59f7b9d332622ab016f35f`.

Its complete native source has the retained identity

`cut_stack_allroot.py`, 27482 bytes, SHA-256

`7774c98345c9865abb4c67c01cd305c5630b06f2d353b1f72d59a3953682e174`.

No new numerical coefficient table is promoted. The central-cut search did not yield a completed acceptance record available for this handoff. No conclusion about that region follows from it.

The theorem returned here is **analytic**. Its finite certificate consists of four displayed rational matrices and a complete combinatorial rule generating 320 three-arrow supports. All estimates and the actual-volume argument are proved below. A complete standard-library auditor is included for replay, but I do not claim a newly observed successful execution or an output hash for that auditor in this continuation. The proof does not depend on such an execution.

## 3. Actual geometry and the correct normalization

The native operation is genuine on the whole domain \(b>0\), \(f_j,k_j,t\in(0,1)\). The left and right removed tetrahedra have disjoint interiors in the two halfspaces \(x<0\) and \(x>0\). The stack point is interior to the left removed tetrahedron and sees exactly the left triangular cut face. Thus the complete true maximal facet cycles remain

```
F0=(0,3,4,1,7,6)   F1=(0,2,5,3)   F2=(0,6,8,2)
F3=(1,4,5,2)       F4=(1,2,8,7)   F5=(3,9,4)
F6=(3,5,9)         F7=(4,9,5)     F8=(6,7,8).
```

The 17 true edges are

```
02,03,06,12,14,17,25,28,34,35,39,45,49,59,67,68,78.
```

No facet-integration diagonal is treated as an escape edge.

Put

\[
\beta=\frac b{1+b},\qquad
 a_j=\frac{1-f_j}{t},\qquad c_j=\frac{1-k_j}{t},
\]

\[
A=\sum_j a_j,\qquad C_1=\sum_j c_j,
\qquad m=\max_j\{a_j,c_j\},
\qquad v=\frac23(1-t)A+C_1.
\tag{5}
\]

Then (1) is precisely

\[
\boxed{6m+2v\le\frac1{32}.}
\tag{6}
\]

Apply the invertible linear map

\[
\operatorname{diag}\left(\frac1t,\frac1{1+b},1\right)
\]

to the native body. This has a constant Jacobian on that body and therefore transports uniform volume correctly. It is not a projective refill.

In the two transverse coordinates write

\[
B_0=(-\beta,0),\qquad B_1=(1-\beta,0),\qquad B_2=(0,1).
\]

The ten normalized points are

\[
\begin{aligned}
Y_j&=(0,B_j),\\
Y_{3+j}&=(-a_j,(1-ta_j)B_j),\\
Y_{6+j}&=(c_j,(1-tc_j)B_j),\\
Y_9&=\left(-L,\frac{1-t}{3}\sum_j(1-ta_j)B_j\right),
\end{aligned}
\tag{7}
\]

where

\[
L=1+\frac{1-t}{3}A\ge1.
\tag{8}
\]

The actual tetrahedron

\[
T=\operatorname{conv}(Y_0,Y_1,Y_2,Y_9)
\tag{9}
\]

is contained in the actual body. It is full-dimensional for every parameter in the theorem, including arbitrarily small positive t and every positive b.

### The uniform volume comparison is explicit

Let

\[
F=\prod_j(1-ta_j)=\prod_j f_j,
\qquad K=\prod_j(1-tc_j)=\prod_j k_j.
\]

The actual six-volume after the displayed normalization is

\[
D=\frac{2-(1-t)F-K}{t}
 =1+(1-t)\frac{1-F}{t}+\frac{1-K}{t}.
\tag{10}
\]

This is the same five-piece volume identity as in the parent: two original tetrahedra, minus the two disjoint cut tetrahedra, plus the actual stacked tetrahedron. The transverse base triangle in (9) has area 1/2, so the six-volume of T is L.

The elementary product bounds

\[
1-F\le tA,\qquad1-K\le tC_1
\]

give

\[
D\ge1,
\qquad 0\le D-L\le\frac23(1-t)A+C_1=v.
\tag{11}
\]

The nonnegativity uses the genuine inclusion \(T\subset P\). In particular, the actual fraction q of the body's volume lying outside T satisfies

\[
\boxed{q=\frac{D-L}{D}\le v.}
\tag{12}
\]

No mass in (10)–(12) is adjustable independently of the vertices.

## 4. Regular tetrahedral coordinates and the actual centroid estimate

Let an affine map send the four vertices of T to

\[
p_0=(1,1,1),\quad p_1=(1,-1,-1),\quad
p_2=(-1,1,-1),\quad p_3=(-1,-1,1),
\tag{13}
\]

in the order \(Y_0,Y_1,Y_2,Y_9\). Denote the image body by K. The regular tetrahedron has centroid 0, circumradius \(\sqrt3\), pairwise vertex distance \(\sqrt8\), and uniform covariance \(I/5\). These follow directly from

\[
\sum_i p_i=0,\qquad \sum_i p_ip_i^T=4I
\]

and the uniform tetrahedral second-moment formula.

We do **not** assume K has centroid 0. Its actual centroid will be bounded and then subtracted.

### Each of the nine nonstack labels is close to its prescribed corner

The transverse origin is in the triangle \(\operatorname{conv}(B_0,B_1,B_2)\):

\[
0=(1-\beta)B_0+\beta B_1.
\]

The transverse projection of \(Y_9\) is also in that triangle. Let d be any barycentric representation of that projection in the triangle, with nonnegative coefficients summing to 1. Let o be the displayed barycentric representation of the origin.

The affine image of \(Y_{3+j}\), minus \(p_j\), equals

\[
ta_j\left(\sum_i o_i p_i-p_j\right)
+\frac{a_j}{L}\left(p_3-\sum_i d_i p_i\right).
\tag{14}
\]

For \(Y_{6+j}\), the analogous expression has the second term with coefficient \(-c_j/L\), and the first term with \(tc_j\). Since both barycentric points are in the regular base triangle,

\[
\|Y_{3+j}^{\rm reg}-p_j\|,
\ \|Y_{6+j}^{\rm reg}-p_j\|
\le\sqrt8\,m\left(t+\frac1L\right)
<6m.
\tag{15}
\]

The other four vertices map exactly to their regular corners.

Partition the ten labels into the four fixed groups

\[
G_0=\{0,3,6\},\quad G_1=\{1,4,7\},\quad
G_2=\{2,5,8\},\quad G_3=\{9\}.
\tag{16}
\]

Every uncentered vertex of K in group i is within \(e<6m\) of \(p_i\).

### Subtracting the true centroid

Condition (6) implies \(6m\le1/32\). Hence every point of K has norm less than

\[
\sqrt3+1/32<2.
\]

The regular tetrahedron inside K has centroid 0. Splitting the **actual uniform integral** into that tetrahedron and its genuine complement gives

\[
\|g_K\|
=\left\|\frac1{\operatorname{Vol}K}\int_{K\setminus T_{
m reg}}x\,dx\right\|
<2q\le2v.
\tag{17}
\]

Thus after subtracting the actual centroid, every group-i vertex satisfies

\[
\boxed{\|X-p_i\|<6m+2v\le1/32.}
\tag{18}
\]

This is the central actual-volume step. Subtracting the tetrahedron's centroid instead of the body's actual centroid would not prove (18).

### A useful actual covariance bound

Since \(A,C_1\le3m\), one has \(v\le5m\). Combining this with (6) gives

\[
v\le5/512,
\qquad q\le5/512.
\]

The actual uncentered second moment of K obeys

\[
\mathbb E_Kxx^T
\preceq\left[\frac{1-q}{5}+4q\right]I
\preceq\left(\frac15+\frac{19}{512}\right)I
=\frac{607}{2560}I\prec\frac14I.
\]

Subtracting \(g_Kg_K^T\) only decreases this matrix. Consequently

\[
\boxed{\Sigma_K\prec I/4.}
\tag{19}
\]

Again this is the covariance of the actual uniformly filled image, not a chosen reference covariance.

## 5. The three-arrow tetrahedral lemma

Consider any rooted tree on the four regular corners in (13). For its three arrows put

\[
Q_0=\sum_{i\to j}\operatorname{sym}\bigl(p_i(p_i-p_j)^T\bigr).
\]

Up to a permutation of the four corners, there are four rooted-tree forms. Every corner permutation is induced by an orthogonal map. Representatives and their matrices are:

```
rooted star, root at centre:
  0->3, 1->3, 2->3
  Q0 = [[4,0,0],[0,4,0],[0,0,4]]

rooted star, root at a leaf:
  1->0, 2->0, 0->3
  Q0 = [[4,0,2],[0,4,2],[2,2,4]]

path, root at an endpoint:
  0->1, 1->2, 2->3
  Q0 = [[2,-2,1],[-2,6,1],[1,1,4]]

path, root at an internal vertex:
  0->1, 2->1, 3->2
  Q0 = [[2,0,1],[0,6,-1],[1,-1,4]].
```

The leading principal minors of \(Q_0-(5/8)I\) are, respectively,

\[
\begin{array}{c|ccc}
&1\text{st}&2\text{nd}&3\text{rd}\\\hline
\text{star/centre}&27/8&729/64&19683/512\\
\text{star/leaf}&27/8&729/64&5859/512\\
\text{path/endpoint}&11/8&217/64&355/512\\
\text{path/internal}&11/8&473/64&9315/512.
\end{array}
\]

They are all positive. Therefore

\[
\boxed{Q_0\succ(5/8)I}
\tag{20}
\]

for every rooted regular-tetrahedron tree.

Now replace the source and target of each of its three arrows by arbitrary centered points from the corresponding groups, each satisfying (18). The source and target selected from one group need not be the same actual vertex. This freedom is important for the quotient-tree application.

If source \(X=p_i+u\), target \(Y=p_j+w\), and \(\|u\|,\|w\|\le r\), then

\[
\begin{aligned}
&\left\|\operatorname{sym}\bigl(X(X-Y)^T-p_i(p_i-p_j)^T\bigr)\right\|_{\rm op}\\
&\hspace{25pt}\le(2\sqrt3+\sqrt8)r+2r^2
<\frac{13}{2}r+2r^2.
\end{aligned}
\]

Summing three arrows, using \(r\le1/32\), gives an operator error less than

\[
\frac{39}{64}+\frac6{1024}=\frac{630}{1024}.
\]

Since \(5/8=640/1024\), every such three-arrow matrix satisfies

\[
\boxed{Q\succ\frac5{512}I.}
\tag{21}
\]

Together with (19), this gives

\[
Q\succ\frac5{128}\Sigma_K.
\tag{22}
\]

Under the inverse affine congruence this becomes precisely (3) in the native physical coordinates. If \(\Sigma_T\) is the actual covariance of the contained tetrahedron before regularization, (21) also gives the independent intrinsic bound

\[
Q\succ\frac{25}{512}\Sigma_T.
\]

Neither covariance is independently assigned or used to reset the physical metric.

## 6. Why this covers every complete true rooted tree

Take any of the actual ten-label rooted true-edge trees. Contract the four groups (16), discarding arrows that stay within a group. The resulting directed multigraph has a directed walk from each group to the root group: map any original vertex-to-root path into the quotient.

Every finite directed graph in which all nodes can reach a root contains an in-arborescence to that root. For example, choose at each nonroot group an outgoing edge that decreases its shortest directed distance to the root. Thus three of the original selected **true** arrows induce a rooted tree on the four groups.

Those three arrows have the matrix lower bound (21), regardless of which allowed actual endpoints they use. Therefore they cannot all be weakly nonnegative under any nonzero PSD physical matrix. This contradicts the complete selected packet.

The argument is purely combinatorial after the matrix bound. It does not presume that each group induces a connected subtree, choose a highest-norm vertex as an unproved shortcut, or require positive rather than weak arrows.

### Complete finite support rule

The cross-group true edges are

```
G0--G1: 34,67
G0--G2: 02,35,68
G0--G3: 39
G1--G2: 12,45,78
G1--G3: 49
G2--G3: 59.
```

Choose any three of these edges whose group pairs form a spanning tree on four groups, and orient them toward any chosen root group. Give all three arrows weight 1. This is the entire certificate list; there are no unlisted real coefficients or selected-cell parameters.

The multiplicity-weighted group Laplacian has cofactor

\[
\begin{pmatrix}6&-2&-3\\-2&6&-3\\-3&-3&7\end{pmatrix},
\qquad\det=80.
\]

There are therefore 80 unrooted three-edge choices and **320 distinct rooted supports**. Every one of these supports is positive throughout (1), and every rooted true-edge tree contains one of them. The previous graph's count of 4641 unrooted and 46410 rooted trees is unchanged; the quotient argument covers them without requiring a newly optimized stress for each tree.

For SPD M, unique strict U would supply a selected weak tree because every nonroot vertex has an incident weak escape, and each such arrow strictly increases the quadratic norm. Thus the complete packet exclusion implies U≥2. Singular matrices are included in the certificate pairing, but no ordinary physical equilibrium interpretation is imposed on them.

## 7. The explicit domain, ties, and limitations

For the sufficient box (2), set

\[
r_t=\frac1{128(4-t)}.
\]

Then \(a_j,c_j\le r_t\), so

\[
6m+2v
\le[6+4(1-t)+6]r_t
=4(4-t)r_t=1/32.
\]

This proves (2), including all six independent endpoints. The maximum normalized deficit may be attained by any number of cuts; no tie face is removed. The actual native parameters remain strict where feature fidelity requires it: t is in (0,1), b>0, and the cuts are less than 1. Parameter values with a cut exactly 1 can be interpreted as lower-vertex limits, but are not called E17 bodies here.

As a simple literal native point in the new region, take

\[
b=1,\qquad t=1/2,\qquad f_j=k_j=895/896.
\]

It lies on the allowed six-cut lower boundary of (2), has the genuine stated maximal cycles, and is far outside the old certified box. This point is only an instantiation of the new exclusion theorem; no unexecuted exact census or survivor claim is attached to it.

The theorem also holds on the larger asymmetric deficit-budget region (1), not just the sufficient box. The asymmetry between the left and right cut budgets comes from the actual stack: the left volume excess carries the factor \(1-t\). Replacing those coefficients by independently chosen volume weights would invalidate the proof.

This is an effective deep-cut result, not a full solution of the middle-cut interior. It does not decide whether the original native family has a U1 metric elsewhere. It does not prove S≥2 on the new region, identify an additional incidence class, or show that the native eight parameters exhaust the broader eleven-parameter realization chart.

## 8. Same-inverse and minimum consequences

There is no spectral cutoff in this theorem. The positive matrix pairing excludes the complete primal weak packet even for a singular nonzero PSD M. Hence no actual joint S1/U1 metric exists in (1), whatever the same-origin inverse does on the dual side.

This is a complete primal exclusion, not a relaxation in which primal and polar matrices have been chosen independently. Under either affine normalization used in the proof, centered vectors transform linearly, the physical matrix transforms by inverse congruence, and the polar uses exactly its inverse.

The new covariance margin (4) is **local to this actual shape domain**. It does not improve the universal orthogonal factor \(41/5\) or the universal E17 condition bound below 40. The canonical C622 attaining construction, the accepted genuine lower counterfamilies, and \(34\le C_{\min}\le622\) remain unchanged.

No canonical registry subtraction is made. The new domain is disjoint from the prior six-cut box, but it has not been compared against every historically closed corner-collapse sector. Its contribution is the explicit whole-domain inequality, its unrestricted conditioning, and the complete three-unit-arrow certificate.

## 9. Complete deterministic recovery capsule

The exact certificate is already specified by (13), the four matrices in Section 5, the 17 true edges, the group map, and the spanning-tree rule in Section 6. Those data reconstruct every one of the 320 supports. The proof of their whole-domain positivity is the actual-volume estimate (10)–(19), not a sampled numerical test.

The following complete auditor uses only the Python standard library and exact integers/Fractions. It is written for Python 3.9 or later. It requires no native-parent source, old row table, external file or random seed. It checks all generated three-arrow matrices, independently enumerates the full true rooted-tree set, verifies support containment for every tree, and checks the rational constants.

Save it as `cut_stack_deep_deficit.py` and run:

```
python -B -S cut_stack_deep_deficit.py
```

Its expected terminal marker is

```
CUT_STACK_DEEP_DEFICIT_THREE_ARROW_U2_V1 PASS
```

Verification status is deliberately separated: the analytic proof above is complete, while **no new completed author execution, source byte-count pin or output SHA-256 is claimed for this auditor**. The central-cut numerical work is not being laundered into this certificate. All continuation-critical data are literal below, so replay does not depend on a missing artifact or hash-only object.

```python
#!/usr/bin/env python3
'''Exact finite auditor for CUT_STACK_DEEP_DEFICIT_THREE_ARROW_U2_V1.
Python >=3.9, standard library only. Assertions must remain enabled.
The accompanying proof establishes the actual-volume domain inequality.
This program audits its finite matrix and complete-tree certificate.
'''
from fractions import Fraction as F
from itertools import combinations
import json

OBJECT = 'CUT_STACK_DEEP_DEFICIT_THREE_ARROW_U2_V1'
PARENT = 'minimum-0286'
PARENT_SHA256 = '2e28f07cc57fd27c8a5e3a538577ba23b89fa14cb85f59fbe85be8967ba060d4'
FACES = ((0,3,4,1,7,6),(0,2,5,3),(0,6,8,2),
         (1,4,5,2),(1,2,8,7),(3,9,4),(3,5,9),(4,9,5),(6,7,8))
EDGES = tuple(sorted({tuple(sorted((a,b))) for cy in FACES
                      for a,b in zip(cy,cy[1:]+cy[:1])}))
ARROWS = tuple(e for a,b in EDGES for e in ((a,b),(b,a)))
GROUP = (0,1,2,0,1,2,0,1,2,3)
P = ((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))


def det3(A):
    a,b,c = A
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))


def leading(A):
    return (A[0][0], A[0][0]*A[1][1]-A[0][1]*A[1][0], det3(A))


def is_tree(n, edges):
    parent = list(range(n))
    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for a,b in edges:
        u,v = find(a),find(b)
        if u == v:
            return False
        parent[u] = v
    return len(edges) == n-1 and len({find(i) for i in range(n)}) == 1


def orient(n, edges, root):
    nbr = [[] for _ in range(n)]
    for a,b in edges:
        nbr[a].append(b)
        nbr[b].append(a)
    par = [-1]*n
    par[root] = root
    queue = [root]
    for i in queue:
        for j in nbr[i]:
            if par[j] < 0:
                par[j] = i
                queue.append(j)
    assert len(queue) == n
    return tuple(par)


def regular_stress(arrows):
    Q = [[F(0) for _ in range(3)] for _ in range(3)]
    for a,b in arrows:
        x,y = P[GROUP[a]],P[GROUP[b]]
        e = tuple(x[i]-y[i] for i in range(3))
        for i in range(3):
            for j in range(3):
                Q[i][j] += F(x[i]*e[j]+e[i]*x[j],2)
    return Q


def main():
    if not __debug__:
        raise RuntimeError('Run with assertions enabled, not with -O')
    assert len(EDGES) == 17 and len(ARROWS) == 34
    expected_edges = ((0,2),(0,3),(0,6),(1,2),(1,4),(1,7),(2,5),
                      (2,8),(3,4),(3,5),(3,9),(4,5),(4,9),(5,9),
                      (6,7),(6,8),(7,8))
    assert EDGES == expected_edges
    cross = tuple(e for e in EDGES if GROUP[e[0]] != GROUP[e[1]])
    assert len(cross) == 11
    lap = [[0]*4 for _ in range(4)]
    for a,b in cross:
        i,j = GROUP[a],GROUP[b]
        lap[i][i] += 1
        lap[j][j] += 1
        lap[i][j] -= 1
        lap[j][i] -= 1
    assert [row[:3] for row in lap[:3]] == [[6,-2,-3],[-2,6,-3],[-3,-3,7]]
    assert det3([row[:3] for row in lap[:3]]) == 80

    supports = []
    group_tree_count = 0
    matrix_records = []
    for chosen in combinations(cross,3):
        ge = tuple((GROUP[a],GROUP[b]) for a,b in chosen)
        if not is_tree(4,ge):
            continue
        group_tree_count += 1
        for root in range(4):
            par = orient(4,ge,root)
            arrows = []
            for i in range(4):
                if i == root:
                    continue
                j = par[i]
                a,b = next(e for e in chosen if {GROUP[e[0]],GROUP[e[1]]} == {i,j})
                arrows.append((a,b) if GROUP[a] == i else (b,a))
            arrows = tuple(sorted(arrows))
            Q = regular_stress(arrows)
            shifted = [[Q[i][j]-(F(5,8) if i == j else 0)
                        for j in range(3)] for i in range(3)]
            pivots = leading(shifted)
            assert min(pivots) > 0
            supports.append(arrows)
            matrix_records.append(pivots)
    assert group_tree_count == 80
    supports = tuple(sorted(set(supports)))
    assert len(supports) == 320
    masks = tuple(sum(1 << ARROWS.index(e) for e in row) for row in supports)

    tree_count = 0
    rooted_count = 0
    for chosen in combinations(EDGES,9):
        if not is_tree(10,chosen):
            continue
        tree_count += 1
        for root in range(10):
            par = orient(10,chosen,root)
            mask = sum(1 << ARROWS.index((i,par[i]))
                       for i in range(10) if i != root)
            assert any((mask & submask) == submask for submask in masks)
            rooted_count += 1
    assert tree_count == 4641 and rooted_count == 46410

    r = F(1,32)
    error = 3*(F(13,2)*r+2*r*r)
    assert error == F(630,1024)
    assert F(5,8)-error == F(5,512)
    assert F(7,4)**2 > 3 and 3**2 > 8
    assert F(7,4)+r < 2
    assert F(5,16)*r == F(5,512)
    covariance_upper = F(1,5)+F(19,512)
    assert covariance_upper == F(607,2560) < F(1,4)
    assert 4*F(5,512) == F(5,128)
    assert F(5,128)/3 == F(5,384) > F(1,80)
    # Uniform independent-cut corollary:
    # [6+4(1-t)+6]/[128(4-t)] is identically 1/32.
    assert 32*16 == 128*4 and 32*(-4) == -128
    # Literal native boundary point b=1,t=1/2,f=k=895/896.
    t = F(1,2)
    deficit = F(1,896)
    assert deficit == t/(128*(4-t))
    budget = 576*deficit+128*(1-t)*3*deficit+192*3*deficit
    assert budget == 3*t

    report = {
        'object': OBJECT,
        'parent': PARENT,
        'parent_sha256': PARENT_SHA256,
        'true_facets': FACES,
        'true_edges': EDGES,
        'group_map': GROUP,
        'regular_corners': P,
        'stress_supports_all_weights_one': supports,
        'regular_shift': '5/8',
        'positive_regular_minor_checks': 3*len(matrix_records),
        'unrooted_group_choices': group_tree_count,
        'unrooted_true_trees': tree_count,
        'covered_rooted_true_trees': rooted_count,
        'centered_cluster_radius_upper': '1/32',
        'regular_frame_stress_lower': '5/512',
        'actual_covariance_stress_lower': '5/128',
        'negative_mean_arrow_covariance_margin': '5/384',
        'native_condition': '576*d+128*(1-t)*sum(alpha)+192*sum(gamma)<=3*t',
        'independent_cut_condition': '1-t/(128*(4-t))<=f_j,k_j<1',
        'scope': 'All b>0 and 0<t<1 in the stated actual native domain; no metric cutoff; no whole-native or global E17 conclusion'
    }
    print(json.dumps(report,sort_keys=True,indent=2))
    print(OBJECT+' PASS')


if __name__ == '__main__':
    main()
```

## 10. What changed and the remaining frontier

The accepted largest-deficit atlas was not an interior mechanical theorem. This continuation adds one: the actual deep-cut budget (1) has no complete weak rooted tree under any nonzero PSD metric. Its certificate has only three unit-weight arrows, and its shape-independent support rule covers every rooted alternative. The actual volume excess outside a contained tetrahedron controls the COM error; no moment over-cover is substituted for the real body.

The useful mechanism is therefore a **volume-aware tetrahedral grouping theorem**, not another increase in polynomial degree or a failed stress-library scan. It supplies an explicit covariance-normalized negative-work margin and includes all relative rates as t tends to zero within the displayed domain.

The result is narrower than the broad middle-cut coverage originally sought. No accepted conclusion is returned for that middle region, for the full six-cut complement, or for the coordinator's broader realization chart. A generic wall compactness theorem alone still does not decide those interiors.

The next useful enlargement is to retain the same independent-arrow quotient mechanism while treating non-tetrahedral normalized cores, or to complete an exact middle-cut stress cover. Neither a failed finite row list nor a singular formal packet should be called a physical survivor. The global minimum bracket and the canonical attaining construction are unchanged.
