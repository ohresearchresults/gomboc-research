# figure-0543

AI research report · 2026-09-25 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Fixed-normal support branch: an exact all-root obstruction

## Outcome

**The literal ROBUST_G3 fixed-normal family cannot contain the requested body. In fact, every uniformly filled member of this family has at least two strict stable facets at its own volume centroid.** This exclusion covers every support vector, every rooted polar-chord tree, all root choices, changes of incidence, and deletion or inactivity of any of the original inequalities. No restriction on the number of primal unstable vertices is needed.

Here is the stronger certified statement. Let \(n_0,\ldots,n_{57}\) be the primitive outward normals reconstructed from the 32 literal ROBUST_G3 rows in the recovery code below. For any positive supports \(h\), put
\[
K(h)=\{x:n_i\cdot x\le h_i\text{ for all }i\}.
\]
If
\[
-\frac{2}{7}K(h)\subseteq K(h),
\]
then \(K(h)\) has at least two **strict** stable facets relative to the origin. The statement permits additional weak equilibria; it does not assume them away.

Every three-dimensional convex body centered at its uniform volume centroid satisfies \(-K/3\subseteq K\), hence satisfies the displayed weaker \(7/2\)-asymmetry condition. Consequently **the own-COM-zero support fiber is disjoint even from the union of all closed, nonnegative polar-chord tree cones**, not merely from one selected positive tree cone.

There is also a quantitative consequence directly relevant to support optimization. If a member has only one strict stable facet relative to the chosen origin, and
\[
r_0=\min_i\frac{h_i}{\|n_i\|},
\]
then its actual uniform volume centroid obeys
\[
\boxed{\|c(h)\|>r_0/8.}
\]
Thus the obstruction is not an arbitrarily small residual that a better centroid solver, tree exchange, or weak-equilibrium tolerance could remove.

**No new own110 body is claimed.** The substantive result is a global exclusion of this explicitly specified normal family, together with a reusable all-tree/centroid enclosure method. Changing the normal set is necessary for a constructive continuation from this architecture.

## Source authority and reading receipt

I read the entire supplied 327143-byte journal through EOF, including its embedded W51 parent, and decoded and read all 82 files in its self-contained recovery capsule. The delivered pack has SHA-256 `a45d48a37be34d648ae8134a090d3f56ddb9c120cbfd47c3b6ef4f28ed03113d`. No additional library or unsupplied parent was used.

The controlling source is the delivered payload labeled `figure-0537`, declaring SHA-256 `05577e4a0b36b334bf63e1fd41ffdbb8b9c663892f7da776c851bf47acf7af21`. There is one outer-serialization limitation: extracting its rendered text from the W51 heading through the supplied EOF gives 81780 UTF-8 bytes and SHA-256 `6b7c2e66c5ed54021aa9e6532f222f57b843c4b6ea6255c18f489500899abea1`, rather than that declared immutable hash. I cannot reconcile those outer representations from this pack. The embedded executable decoder, however, is exactly 61061 bytes with the advertised SHA-256 `9cad65f5688d803d536d995be50f2ae475c7d53d5791f960a72b027f9dbfb577`; its decoded 171845-byte dictionary matches `ce7c3f1ad9ce6d5696792ac9fd6ad791c37c39dbb5442783e9413477c1eea559`. The literal baseline input and its replayed audit also match their advertised byte hashes. The new theorem depends on those explicitly reproduced rows, not on an unresolved outer wrapper.

The baseline is exactly V31/E87/F58, C174, own211, additional weak000. Input row **3** is interior; row **4** is retained and extreme. Its volume and centroid are
\[
V=\frac{10865185711}{1500000000},\qquad
c=\left(
-\frac{386613615871}{10865185711000},
-\frac{3857015486057}{21730371422000},
\frac{57133873364297}{173842971376000}
\right).
\]
The parent gives canonical stable facets 11 and 14, unstable vertex 1, and saddle edge 2–7. These are not original material-row labels. The contradictory row-4/volume-7.590617 claims elsewhere in the notebook were not used.

The 565-byte baseline input hash is `0fa93190d2a33864b219b2b73b6a433236f1e1338dea7ec49075c3ca2ac033fc`. I reran the parent's complete exact baseline audit; its 2839-byte output matched `5a77084f44934652c84a5af6345729acfc72e8ea493a2198fca46baf163f80a7`. The new standalone checker independently reconstructs the normals, verifies row retention, V/E/F, volume, and centroid. It does not claim to be a second complete equilibrium auditor.

## 1. Why all roots and weak boundaries are covered

Use primitive rational normals rather than unit normals; this merely rescales the support coordinates. Their positive rays are distinct. For each supplied inequality define its plane foot and polar material point by
\[
f_i=\frac{h_i n_i}{\|n_i\|^2},\qquad q_i=\frac{n_i}{h_i}.
\]
These polar points only encode the same physical body's foot tests; their own filled centroid is never used.

If every other inequality is strict at \(f_i\), then inequality \(i\) carries an actual maximal facet and \(f_i\) lies in its relative interior: it is a strict stable facet. This observation also handles redundant inequalities; a redundant row cannot pass that strict test.

Suppose there were exactly one strict stable facet, with index \(r\). For every \(i\ne r\), some \(j\ne i\) must therefore satisfy
\[
n_j\cdot f_i\ge h_j,
\quad\text{equivalently}\quad
h_j\le a_{ij}h_i,
\qquad a_{ij}=\frac{n_i\cdot n_j}{\|n_i\|^2}>0.
\tag{1}
\]
The corresponding chord has \(q_i\cdot(q_j-q_i)\ge0\). Even at equality,
\[
\|q_j\|^2-\|q_i\|^2
=2q_i\cdot(q_j-q_i)+\|q_j-q_i\|^2>0,
\]
because distinct normal rays give distinct polar points. Thus selected arrows cannot cycle. Every path ends at \(r\), giving a rooted tree with at most 57 edges along a path.

**Equality arrows are deliberately allowed.** A boundary foot is not silently treated as absent, and no positive barcode is rounded to zero. The certificate excludes this larger nonnegative-arrow relaxation, which is necessary even for a body with one strict S and additional weak configurations.

There is always at least one strict stable facet: choose the smallest normalized support \(h_i/\|n_i\|\). Its foot satisfies every other inequality strictly, since distinct unit normals have scalar product strictly below one. Excluding the possibility of exactly one therefore proves **S≥2**, not merely “S≠1.”

## 2. The actual-volume-centroid ingredient

The needed centroid inequality has an elementary uniform-volume proof; no external centroid theorem is assumed.

Fix any \(p\in K\). Cone a triangulation of the boundary to \(p\), omitting zero-volume tetrahedra. In every resulting tetrahedron its uniform centroid is
\[
\frac{p+a+b+d}{4}.
\]
Averaging with the positive tetrahedral volumes gives
\[
c(K)=\frac14p+\frac34y\qquad\text{for some }y\in K.
\]
Consequently \(c(K)=0\) implies \(-p/3\in K\). This holds for every \(p\in K\), so
\[
-K/3\subseteq K.
\tag{2}
\]
This argument uses the filled body's volume weights, not vertex masses, a surface centroid, or an adjustable reference point.

For the stronger certificate I assume only
\[
-K/\beta\subseteq K,\qquad \beta=7/2.
\tag{3}
\]
Condition (2) implies (3). The additional slack in \(\beta\) produces the quantitative centroid separation stated above.

## 3. All-tree lower bounds, followed by centroid enclosure

Fix a root \(r\). A positive homothety normalizes its support to
\[
h_r=H_r:=\max_k |n_{r,k}|.
\]
This is only a scale choice. Suppose a vector \(\ell\) is already known to satisfy \(h_i\ge\ell_i\) for every putative solution with this root.

### A checked Bellman bound

Construct \(u\) with \(u_r=H_r\), \(u_i\ge\ell_i\), and
\[
u_i\le\max\!\left(\ell_i,\frac{u_j}{a_{ij}}\right)
\quad\text{for every }i\ne r\text{ and every }a_{ij}>0.
\tag{4}
\]
Then every support vector satisfying (1) along any tree rooted at \(r\) must satisfy \(h_i\ge u_i\). Indeed, start at the root and induct backwards along its actual tree paths. Both entries of the maximum in (4) are bounded above by \(h_i\).

The implementation computes useful labels by an exact minimax-path algorithm, but **independently checks every inequality (4)**. The exclusion does not depend on trusting an optimizer or assuming its selected tree is the only possible one.

Starting with \(\ell_r=H_r\), \(\ell_i=0\) otherwise, this recovers the usual all-path lower envelope. Equivalently, if \(B_{ir}\) is the maximum product of the \(a\)'s along paths to \(r\), then initially \(u_i=H_r/B_{ir}\). All paths, rather than one nominated spanning tree, are bounded.

### The step that closes the remaining roots

Because \(h\ge u\),
\[
L(u):=\{x:Nx\le u\}\subseteq K(h).
\]
Choose any finite collection of **exactly feasible** points \(x\in L(u)\). By (3), each \(-x/\beta\) belongs to the putative \(K(h)\). Therefore improve the lower supports to
\[
\ell'_i=\max\left(u_i,\max_x\frac{-n_i\cdot x}{\beta}\right).
\tag{5}
\]
Apply (4) again, then repeat.

This is the consequential use of the fixed normal set: lower bounds on all its supports imply containment of an entire new H-body, not just containment of the selected reflected points. Repeating that containment amplifies the necessary centroid constraint.

The certificate stops when it obtains an exactly feasible \(x\in L(u)\) with
\[
-n_r\cdot x>\beta H_r.
\tag{6}
\]
The putative body's inclusion (3) would instead require \(-n_r\cdot x\le\beta h_r=\beta H_r\), an immediate contradiction.

Only rational plane intersections, all-row containment tests, and inequalities (4)–(6) enter the final verification. Complete enumeration of the auxiliary H-body's vertices is unnecessary: any certified feasible witnesses suffice.

## 4. Executed exact certificate

For \(\beta=7/2\), every one of the 58 roots is excluded. The numbers of roots requiring respectively zero, one, two, three, four, or five enclosure updates are
\[
(34,1,2,12,8,1).
\]
The two stable-normal choices in the actual baseline are both covered: root 11 takes three updates, and root 14 takes four.

The replay checked **136 all-tree label systems, 265279 Bellman inequalities, 531 feasible point witnesses, and 30798 exact halfspace inequalities**. The smallest terminal factor \(-n_r\cdot x/H_r\) occurs at root 16 and satisfies
\[
\frac{3512958835751}{10^{12}}
\le \min_r\frac{-n_r\cdot x_r}{H_r}
<\frac{3512958835752}{10^{12}}.
\]
In particular every terminal factor exceeds \(7/2+1/100\). These brackets are obtained by integer division of exact fractions, not by rounding a floating margin.

Default replay uses only the Python standard library. A separate fresh `--discover` run regenerated the same witness plan and the same 1684-byte receipt byte-for-byte. Discovery uses a floating hull solely to propose triples; every retained intersection is reconstructed rationally and checked against every inequality. The actual exclusion is the subsequent exact replay. This is one displayed proof implementation with checked certificates, not a claim of independent formal verification in a proof assistant.

## 5. Quantitative separation from actual COM

Let \(K\) contain the reference origin, let \(c\) be its actual volume centroid, and let \(r_0\) be its reference-centered inradius. Write \(s_K\) for its support function on unit directions. Apply (2) to \(K-c\):
\[
s_K(-v)+v\cdot c\le3\bigl(s_K(v)-v\cdot c\bigr).
\]
Hence
\[
s_K(-v)\le3s_K(v)+4\|c\|.
\]
If \(\|c\|\le r_0/8\), then \(s_K(v)\ge r_0\) implies
\[
s_K(-v)\le\frac72s_K(v)
\]
for every direction. This is exactly (3), so the certified theorem forces S≥2. Thus every reference-S1 support vector in this normal family has **\(\|c\|>r_0/8\)**.

An equivalent useful own-centered statement is: for any member with actual centroid \(g\) and own-centered inradius \(r\), **every reference point in the closed ball \(\|z-g\|\le r/9\) has at least two strict stable facets**. Indeed,
\[
\frac{s_{K-z}(-v)}{s_{K-z}(v)}
\le\frac{3r+\|z-g\|}{r-\|z-g\|}\le\frac72.
\]
The bounds are uniform over all support vectors of this family, not just a neighborhood of ROBUST_G3.

## 6. Tree changes and exact centering: reusable geometry and its limit here

I also analyzed whether tree changes themselves create a connectivity obstruction. They do not, when the root is fixed and mass is ignored.

An acute rooted tree alone is always linearly realizable: set \(h_r=1\) and recursively \(h_i=(h_{\mathrm{parent}(i)}+\varepsilon)/a_{i,\mathrm{parent}(i)}\), with rational \(\varepsilon>0\). This gives reference S1, not own S1. The obstruction is the actual mass placement, not infeasibility of the linear tree inequalities.

Let \(C_r\) be the union of the **positive** rooted chord cones, with \(h_r=1\). If \(a,b\in C_r\), then \(\min(a,b)\), taken coordinatewise, belongs to \(C_r\): at each source use the outgoing witness of whichever support vector attains that minimum. Its target support can only decrease. Positive radial ascent prevents cycles.

There is consequently an explicit piecewise-linear route from \(a\) to \(b\) through tree overlaps. First use
\[
\min(a,\lambda b),\qquad
\lambda:\max(1,\max_i a_i/b_i)\downarrow1,
\]
then use
\[
\min(\lambda a,b),\qquad
\lambda:1\uparrow\max(1,\max_i b_i/a_i).
\]
At a switch, both inherited outgoing witnesses remain strictly valid. This is a finite, constructive parent-exchange mechanism, not a claim that one local gate cancellation eliminates a basin. It does **not** preserve the volume centroid.

The centroid constraint itself has the exact global retraction
\[
R(h)=h-Nc(h),\qquad K(R(h))=K(h)-c(h).
\]
It satisfies \(R^2=R\), \(R(h+Nt)=R(h)\), and produces positive supports. Where the support differential is taken,
\[
DR=I-NJ,\qquad JN=I,
\]
so centering is not obstructed by a missing three-dimensional differential rank. With rational normals and rational supports, the retraction is rational because the filled centroid is rational.

**For these particular normals, however, retraction necessarily leaves every reference-S1 cone.** The global exclusion above explains why connecting cones or improving a local moment correction cannot produce the desired intersection.

Changing the unique stable root while keeping S=1 throughout a continuous fixed-normal path is also impossible: the unique stable root is the unique smallest unit-normal support. A root change passes through a tie for that minimum, and both distinct minimum-support facets are then strictly stable. This is a genuine S≥2 region, not a tolerance-erased weak event.

## 7. Scope and constructive continuation

The theorem includes arbitrary positive heights, all original-normal subsets that define bounded full-dimensional bodies, facet inactivity or reactivation, nonsimple incidences, and all polar tree/root choices. It already excludes S1; primal-U1 guards and edge budgets cannot rescue this fixed-normal family.

It does **not** exclude changed normal directions, additional genuinely new directions, arbitrary nonsingular affine metrics, projective transformations that change the normal set, or other supplied S1 architectures. It is not a global nonexistence result for own110 polyhedra.

The useful next construction must therefore **replace/rotate at least one normal or introduce a new supporting direction**, then rebuild the all-root enclosure test before investing in support continuation. Pure deletions of the original 58 directions remain within the exclusion. Adding at most 27 new directions retains the sufficient bound F≤85, hence E≤249 and C≤498 even if every row becomes active. One replacement retains the stronger F≤58 budget. Neither one replacement nor one addition has been proved sufficient for an own110 construction. Certificate failure for a modified normal set would only reopen the question; it would not prove feasible own mass or U1.

The finite witness lists below are useful design data: a changed architecture must invalidate at least one enclosure implication in each would-be surviving root's proof. They are not themselves proposed physical cut locations at the old centroid.

## 8. Self-contained recovery capsule

Save the following complete source as `W51_FIXED_NORMAL_NO_S1.py`, with LF endings. It includes every literal input row, all witness banks, and all 58 root plans; it needs no parent decoder for the main theorem.

Source: **12144 bytes**, SHA-256 `e3d223d95537420aaa7d3553c9bd6c1a18f3c9670c0ed24d190761d754ba1362`.

Run without Python's `-O` option, because assertions are the certificate checks:

```sh
python -B -S W51_FIXED_NORMAL_NO_S1.py
```

Observed output:

```text
W51_LITERAL_NORMALS_MASS_PASS 31 87 58
W51_FIXED_NORMAL_ALL_ROOTS_NO_S1_EXACT_PASS 7/2 58
CHECKS 136 265279 531 30798
MIN_FACTOR_BRACKET 3512958835751 3512958835752 1000000000000 ROOT 16
RECEIPT 1684 c1718527c3b13f61a7ce25ad1500c0d377e52375652fde323b8b90f4bbde9f84
```

The output is `W51_NO_S1_RECEIPT.json`. Its normal-stream hash is `567b4cbc444c08db088e5855d2db13363a709c06eaeef2c27abe2fa4b442d7c3`; its complete bank/plan-stream hash is `55b9b4baf529b3174d5fd6392d4c69c3deaa25e95f2581f7c25a53d79dd17aa0`.

Exact replay was observed with CPython 3.13.5. Optional rediscovery was observed with NumPy 2.3.5 and SciPy 1.17.0, using no randomness and these non-default settings:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B W51_FIXED_NORMAL_NO_S1.py --discover --beta 7/2 --out REDISCOVERED.json
```

It produced the identical receipt. The fixed eight-round discovery limit and every other parameter are in the source. The embedded exact replay does not import NumPy or SciPy.

```python
"""W51 fixed-normal all-root no-S1 certificate.
Default replay is exact and uses only Python's standard library.
--discover uses NumPy/SciPy only to propose rationally checked witnesses.
"""
from fractions import Fraction as F
from itertools import combinations
from math import gcd
from pathlib import Path
import argparse, hashlib, json, sys
sys.set_int_max_str_digits(0)
BETA = F(7, 2)
PARENT_ID = 'figure-0537'
INPUT_SHA256 = '0fa93190d2a33864b219b2b73b6a433236f1e1338dea7ec49075c3ca2ac033fc'
P = [[-2678, -1136, 975], [-2745, -769, 406], [-2212, -627, 45], [96, -637, -245], [465, 1184, -402], [80, 119, -1160], [294, 781, -935], [157, 537, -1075], [311, 1098, -580], [681, 814, -815], [565, -379, -1032], [883, 11, -962], [947, 461, -856], [1007, 793, -634], [840, 1037, -473], [1206, 848, -369], [1174, 1065, 103], [1389, 818, -95], [1535, 736, 189], [1603, 668, 465], [1571, 172, -108], [1639, 563, 721], [1644, 425, 972], [1609, 244, 1244], [1506, 4, 1547], [1301, -295, 1859], [970, -604, 2131], [548, -896, 2304], [78, -1126, 2365], [-418, -1288, 2323], [-968, -1386, 2170], [-1604, -1391, 1853]]
BANKS = [
    [[0, 1, 2], [0, 1, 7], [0, 7, 8], [8, 11, 12], [12, 13, 14], [14, 15, 30]],
    [[0, 1, 5], [0, 1, 7], [0, 7, 8], [8, 11, 12], [12, 13, 14], [14, 15, 30], [18, 43, 51]],
    [[0, 1, 5], [0, 1, 8], [1, 7, 8], [8, 11, 12], [12, 13, 14], [14, 15, 30], [18, 41, 43], [41, 43, 51]],
    [[0, 1, 5], [0, 1, 8], [1, 7, 8], [8, 11, 12], [12, 13, 14], [14, 15, 30], [18, 41, 43], [41, 43, 45]],
    [[0, 1, 5], [0, 1, 8], [1, 7, 8], [8, 11, 12], [12, 13, 14], [14, 15, 30]],
    [[0, 1, 8], [1, 7, 8], [8, 11, 12], [12, 13, 14], [18, 43, 51]],
    [[0, 7, 8], [8, 11, 12], [12, 13, 14], [18, 41, 43]],
    [[0, 1, 5], [0, 1, 8], [1, 7, 8], [8, 11, 12], [12, 13, 14], [14, 15, 30], [18, 43, 51]],
    [[0, 7, 8], [8, 11, 12], [12, 13, 14], [18, 43, 51]],
    [[0, 1, 5], [0, 1, 8], [1, 7, 8], [8, 11, 12], [12, 13, 14], [14, 15, 30], [41, 43, 51]],
    [[0, 1, 5], [0, 1, 8], [1, 7, 8], [5, 28, 49], [8, 11, 12], [12, 13, 14], [14, 15, 30], [41, 43, 45]],
    [[0, 7, 8], [6, 10, 31], [6, 18, 31], [8, 11, 12], [12, 13, 14], [18, 41, 43]],
]
PLAN = [
    ([0, 1, 2, 3], [5, 48, 49]),  # root 0
    ([4, 5, 6], [6, 18, 31]),  # root 1
    ([], [18, 43, 51]),  # root 2
    ([], [18, 43, 51]),  # root 3
    ([], [18, 43, 51]),  # root 4
    ([7, 8], [18, 41, 43]),  # root 5
    ([0, 1, 2, 3], [5, 48, 49]),  # root 6
    ([4, 5, 6], [6, 10, 31]),  # root 7
    ([4, 9, 2, 3], [5, 28, 49]),  # root 8
    ([], [18, 43, 51]),  # root 9
    ([], [41, 43, 51]),  # root 10
    ([4, 5, 6], [6, 10, 31]),  # root 11
    ([4, 9, 2, 3], [5, 28, 49]),  # root 12
    ([4, 5, 6], [6, 10, 31]),  # root 13
    ([4, 9, 2, 3], [5, 28, 49]),  # root 14
    ([4, 5, 6], [6, 10, 31]),  # root 15
    ([4, 9, 2, 3], [5, 28, 49]),  # root 16
    ([4, 5, 6], [6, 10, 31]),  # root 17
    ([4, 4, 3, 3, 10], [5, 48, 49]),  # root 18
    ([4, 5, 6], [6, 10, 31]),  # root 19
    ([], [12, 13, 14]),  # root 20
    ([], [14, 15, 30]),  # root 21
    ([], [12, 13, 14]),  # root 22
    ([], [12, 13, 14]),  # root 23
    ([], [12, 13, 14]),  # root 24
    ([], [12, 13, 14]),  # root 25
    ([], [12, 13, 14]),  # root 26
    ([], [12, 13, 14]),  # root 27
    ([], [8, 11, 12]),  # root 28
    ([4, 4, 3, 3], [0, 1, 5]),  # root 29
    ([4, 5, 6], [6, 10, 31]),  # root 30
    ([], [0, 1, 8]),  # root 31
    ([4, 4, 3], [0, 1, 5]),  # root 32
    ([], [8, 11, 12]),  # root 33
    ([], [8, 11, 12]),  # root 34
    ([], [8, 11, 12]),  # root 35
    ([], [1, 7, 8]),  # root 36
    ([], [0, 1, 8]),  # root 37
    ([], [1, 7, 8]),  # root 38
    ([], [0, 1, 8]),  # root 39
    ([4, 5, 6], [6, 10, 31]),  # root 40
    ([4, 4], [0, 1, 5]),  # root 41
    ([], [0, 1, 8]),  # root 42
    ([4, 5, 6], [6, 10, 31]),  # root 43
    ([], [0, 1, 8]),  # root 44
    ([4, 5, 6], [6, 10, 31]),  # root 45
    ([], [0, 1, 8]),  # root 46
    ([], [0, 1, 8]),  # root 47
    ([4, 5, 6, 11], [6, 10, 31]),  # root 48
    ([4], [0, 1, 8]),  # root 49
    ([], [0, 1, 8]),  # root 50
    ([], [0, 1, 5]),  # root 51
    ([], [0, 1, 8]),  # root 52
    ([], [0, 1, 5]),  # root 53
    ([], [0, 1, 8]),  # root 54
    ([], [0, 1, 8]),  # root 55
    ([], [0, 1, 5]),  # root 56
    ([], [0, 1, 5]),  # root 57
]

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def encoded(z): return (json.dumps(z,sort_keys=True,separators=(',',':'))+'\n').encode()

def normals():
    raw=(json.dumps(dict(name='W51_ROBUST_G3',denominator=1000,points=P),separators=(',',':'))+'\n').encode()
    assert len(raw)==565 and hashlib.sha256(raw).hexdigest()==INPUT_SHA256
    pts=sorted(map(tuple,P)); faces=[]; W=0; M=[0,0,0]; closure=[0,0,0]
    for f in combinations(range(len(pts)),3):
        a,b,c=[pts[i] for i in f]; n=cross(sub(b,a),sub(c,a))
        if not any(n): continue
        h=dot(n,a); signs=[dot(n,x)-h for x in pts]
        if min(signs)<0<max(signs): continue
        if max(signs)>0:
            n=tuple(-v for v in n); b,c=c,b
        assert sum(v==0 for v in signs)==3
        g=gcd(*n); faces.append((f,tuple(v//g for v in n)))
        for j in range(3): closure[j]+=n[j]
        d=dot(a,cross(b,c)); W+=d
        for j in range(3): M[j]+=d*(a[j]+b[j]+c[j])
    vertices=sorted({i for f,n in faces for i in f}); ix={v:i for i,v in enumerate(vertices)}
    faces.sort(key=lambda z:tuple(ix[i] for i in z[0]))
    edge={tuple(sorted(e)) for f,n in faces for e in combinations(f,2)}
    assert (len(vertices),len(edge),len(faces))==(31,87,58)
    assert tuple(P[3]) not in [pts[i] for i in vertices]
    assert all(tuple(P[i]) in [pts[j] for j in vertices] for i in range(32) if i!=3)
    assert closure==[0,0,0] and W>0
    assert F(W,6*1000**3)==F(10865185711,1500000000)
    c=[F(v,4*W*1000) for v in M]
    assert c==[F(-386613615871,10865185711000),F(-3857015486057,21730371422000),F(57133873364297,173842971376000)]
    N=[n for f,n in faces]
    assert all(any(cross(n,k)) or dot(n,k)<0 for n,k in combinations(N,2))
    assert any(dot(a,cross(b,c)) for a,b,c in combinations(N,3))
    return N, [tuple(ix[i] for i in f) for f,n in faces]

class Proof:
    def __init__(self,N,beta):
        self.N=N; self.m=len(N); self.beta=beta
        self.nn=[dot(n,n) for n in N]
        self.A=[[F(max(0,dot(n,k)),self.nn[i]) if i!=j else F(0)
                 for j,k in enumerate(N)] for i,n in enumerate(N)]
        self.reaches=0; self.bellman=0; self.points=0; self.halfspaces=0

    def reach(self,l,r,H):
        # Minimax path labels; ordering is exact in normalized squared height.
        d=[None]*self.m; d[r]=H; seen=set()
        for unused in range(self.m):
            options=[i for i in range(self.m) if i not in seen and d[i] is not None]
            assert options, 'Acute graph does not connect to the nominated root'
            j=min(options,key=lambda i:(d[i]*d[i]/self.nn[i],i)); seen.add(j)
            for i in range(self.m):
                if i in seen or not self.A[i][j]: continue
                t=max(l[i],d[j]/self.A[i][j])
                if d[i] is None or t<d[i]: d[i]=t
        assert d[r]==H and all(d[i]>=l[i] for i in range(self.m))
        # These checked inequalities, NOT trust in Dijkstra, prove the bounds:
        # use them backwards along any nonnegative escape path to the root.
        for i in range(self.m):
            if i==r: continue
            for j in range(self.m):
                if self.A[i][j]:
                    assert d[i]<=max(l[i],d[j]/self.A[i][j])
                    self.bellman+=1
        self.reaches+=1
        return d

    def point(self,l,f,check=True):
        a,b,c=[self.N[i] for i in f]; det=dot(a,cross(b,c)); assert det
        cof=[cross(b,c),cross(c,a),cross(a,b)]
        x=tuple(sum(l[f[i]]*cof[i][j] for i in range(3))/det for j in range(3))
        if check:
            assert all(dot(n,x)<=h for n,h in zip(self.N,l)), ('infeasible witness',f)
            self.points+=1; self.halfspaces+=self.m
        return x

    def update(self,l,bank,r,H):
        floor=l[:]
        for f in bank:
            x=self.point(l,f)
            for i,n in enumerate(self.N): floor[i]=max(floor[i],-dot(n,x)/self.beta)
        assert floor[r]<=H
        return self.reach(floor,r,H)

    def replay(self,banks,plan):
        assert len(plan)==self.m
        rows=[]; factors=[]; hist={}
        for r,(steps,terminal) in enumerate(plan):
            H=F(max(map(abs,self.N[r]))); l=[F(0)]*self.m; l[r]=H
            l=self.reach(l,r,H)
            for k in steps: l=self.update(l,banks[k],r,H)
            x=self.point(l,terminal); factor=-dot(self.N[r],x)/H
            assert factor>self.beta, ('root not excluded',r)
            factors.append(factor); hist[len(steps)]=hist.get(len(steps),0)+1
            floor=factor.numerator*10**12//factor.denominator
            rows.append([r,len(steps),floor])
        return dict(beta=str(self.beta),roots=self.m,round_histogram=hist,
                    minimum_factor_root=min(range(self.m),key=lambda i:factors[i]),
                    minimum_factor_bracket=[min(x[2] for x in rows),min(x[2] for x in rows)+1,10**12],
                    strict_margin_gt_001=all(x>self.beta+F(1,100) for x in factors),
                    reaches=self.reaches,bellman_checks=self.bellman,
                    feasible_witnesses=self.points,halfspace_checks=self.halfspaces,
                    root_brackets=rows)

    def discover(self):
        import numpy as np
        from scipy.spatial import ConvexHull
        banks=[]; plan=[]
        for r in range(self.m):
            H=F(max(map(abs,self.N[r]))); l=[F(0)]*self.m; l[r]=H
            l=self.reach(l,r,H); steps=[]
            for iteration in range(8):
                q=np.array([[float(F(t)/l[i]) for t in self.N[i]] for i in range(self.m)])
                proposed=sorted({tuple(sorted(map(int,f))) for f in ConvexHull(q).simplices})
                vv=[]
                for f in proposed:
                    a,b,c=[self.N[i] for i in f]
                    if not dot(a,cross(b,c)): continue
                    x=self.point(l,f,False)
                    if all(dot(n,x)<=h for n,h in zip(self.N,l)): vv.append((f,x))
                assert vv
                terminal=max(vv,key=lambda z:-dot(self.N[r],z[1]))
                if -dot(self.N[r],terminal[1])>self.beta*H:
                    plan.append((steps,list(terminal[0]))); break
                winners=[]
                for i,n in enumerate(self.N):
                    f,x=max(vv,key=lambda z:-dot(n,z[1]))
                    if -dot(n,x)/self.beta>l[i]: winners.append(f)
                bank=[list(f) for f in sorted(set(winners))]
                if bank not in banks: banks.append(bank)
                steps.append(banks.index(bank)); l=self.update(l,bank,r,H)
            else: raise AssertionError(('No exclusion in eight rounds',r))
        return banks,plan

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--discover',action='store_true')
    parser.add_argument('--beta',default='7/2')
    parser.add_argument('--out',default='W51_NO_S1_RECEIPT.json')
    args=parser.parse_args(); beta=F(args.beta); N,faces=normals()
    banks,plan=BANKS,PLAN
    if args.discover: banks,plan=Proof(N,beta).discover()
    else: assert beta==BETA
    report=Proof(N,beta).replay(banks,plan)
    report['normal_sha256']=hashlib.sha256(encoded(N)).hexdigest()
    report['plan_sha256']=hashlib.sha256(encoded([banks,plan])).hexdigest()
    data=encoded(report); Path(args.out).write_bytes(data)
    print('W51_LITERAL_NORMALS_MASS_PASS',31,87,58)
    print('W51_FIXED_NORMAL_ALL_ROOTS_NO_S1_EXACT_PASS',beta,report['roots'])
    print('CHECKS',report['reaches'],report['bellman_checks'],report['feasible_witnesses'],report['halfspace_checks'])
    print('MIN_FACTOR_BRACKET',*report['minimum_factor_bracket'],'ROOT',report['minimum_factor_root'])
    print('RECEIPT',len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__': main()
```

## 9. Optional positive-control replay

As a compatibility check, I also freshly audited the supplied **H24** body with its own, different normal set: V44/E66/F24, strict own121, additional weak000. Eight rounds of the same enclosure procedure at its unique stable input normal, row 15, kept every inferred lower support below that body's actual centered support. Thus the algorithm does not automatically reject a known own-S1 family.

This check is not needed for the standalone theorem above. The following complete patch requires `exact_h.py`, `exact_poly.py`, and `fast_h51.py` from the supplied W51 decoder. Their SHA-256 values are respectively `6ad529254c433a8078eabbfca5058f10a6612f4cec107606198af5039852d25b`, `898f77989193886996d6f2dc121ccdfdf611b8a9ac52fd3207557eac6a69c0c4`, and `0de27af824919fb82fd0bc90bd307ecfccbe46a2d2c8832ea391d733b78bcbce`. The full literal H24 input is included in the patch.

Save as `H24_COMPATIBILITY.py`: **2234 bytes**, SHA-256 `55151a74ea40e237eab0e49c99d7e3fe8034c629e83f6b981346491f4721c5b1`.

```sh
python -B -S RECOVER_W51.py W51_SOURCE
PYTHONPATH=W51_SOURCE OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B H24_COMPATIBILITY.py
```

Observed marker:

```text
H24_KNOWN_OWN_S1_CLOSURE_COMPATIBILITY_PASS 15 8 295 1b6271079551a5313414e12a966f238eb617a18f324ffb617863831ac78d65fb
```

The 295-byte file is `H24_COMPATIBILITY_RECEIPT.json`. This is a control on an unchanged supplied body, not a new geometric successor.

```python
"""Positive S1 control for the closure method.
Requires exact_h.py, exact_poly.py and fast_h51.py from literal W51.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
import numpy as np
from scipy.spatial import ConvexHull
from fast_h51 import audit
from W51_FIXED_NORMAL_NO_S1 import Proof,dot,encoded
H24=[[-754,596,-826,1000],[-853,1454,-237,1000],[-624,235,-911,1000],[-843,1043,-595,1000],[-729,1915,472,1000],[-612,2025,98,1000],[-221,-694,-1011,1000],[-260,921,-1181,1000],[101,-548,-937,1000],[-211,1301,-1116,1000],[-552,2046,997,1000],[-384,2123,-267,1000],[-265,1914,-694,1000],[249,-1378,-625,1000],[92,-867,-1106,1000],[794,-2056,714,1000],[-268,2239,-150,1000],[-392,2067,1304,1000],[-299,2014,1499,1000],[167,1596,2401,1000],[517,822,2784,1000],[757,-11,2758,1000],[888,-775,2419,1000],[915,-1438,1812,1000]]
z=audit(dict(name='H24_COMPATIBILITY',halfspaces=H24))
assert z['strict']==[1,2,1] and z['additional_weak']==[0,0,0]
N=[tuple(a[:3])for a in H24];c=list(map(F,z['centroid']))
h=[F(a[3])-dot(a[:3],c)for a in H24]
r=min(range(24),key=lambda i:h[i]**2/dot(N[i],N[i]));assert r==15
H=F(max(map(abs,N[r])));scale=H/h[r];h=[v*scale for v in h]
p=Proof(N,F(7,2));l=[F(0)]*24;l[r]=H;l=p.reach(l,r,H);trace=[]
for k in range(8):
    assert all(x<=y for x,y in zip(l,h))
    q=np.array([[float(F(v)/l[i])for v in N[i]]for i in range(24)]);vv=[]
    for ff in ConvexHull(q).simplices:
        f=tuple(sorted(map(int,ff)))
        try:x=p.point(l,f)
        except AssertionError:continue
        vv.append((f,x))
    assert vv
    factor=max(-dot(N[r],x)/H for f,x in vv)
    assert factor<F(7,2)
    trace.append(factor.numerator*10**12//factor.denominator)
    bank=sorted({max(vv,key=lambda v:-dot(n,v[1]))[0]for n in N})
    l=p.update(l,bank,r,H)
assert all(x<=y for x,y in zip(l,h))
out=dict(root_input=r,iterations=8,own=z['strict'],additional_weak=z['additional_weak'],
         vertex_edge_face=[z[k]for k in ['V','E','F']],root_factor_floors_1e12=trace,
         all_lower_bounds_below_known_actual_supports=True)
b=encoded(out);Path('H24_COMPATIBILITY_RECEIPT.json').write_bytes(b)
print('H24_KNOWN_OWN_S1_CLOSURE_COMPATIBILITY_PASS',r,8,len(b),hashlib.sha256(b).hexdigest())
```

Convenience copies supplement the full recovery source above: standalone exact verifier (`W51_FIXED_NORMAL_NO_S1.py`), exact receipt (`W51_NO_S1_RECEIPT.json`), and positive-control patch (`H24_COMPATIBILITY.py`).
