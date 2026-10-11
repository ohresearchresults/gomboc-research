# minimum-0285

Historical AI scientific report · saved 2026-09-27 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# CUT_STACK_E17_ALLROOT_FULL_B_T_V1

## 1. Main theorem and scientific change

The former single-packet countercontrol is now inside an **all-root, all-SPD exclusion on an eight-parameter continuum**. The base-shape parameter and stacking parameter are covered over their entire admissible ranges, not merely near the parent's point. Six cut fractions vary independently over closed intervals.

Use the parent's native construction:

```
B- = (-1,0,0),  B+ = (1,0,0),
B0 = (0,-b,0),  B1 = (0,1,0),  B2 = (0,0,1),
Lj = B- + fj(Bj-B-),
Rj = B+ + kj(Bj-B+),
C  = (L0+L1+L2)/3,
Y9 = C+t(B--C).
```

The vertex order is `(B0,B1,B2,L0,L1,L2,R0,R1,R2,Y9)`.

**Theorem 1.** Uniformly fill its convex hull and subtract its own volume centroid. For every

```
b > 0,                     0 < t < 1,
f0 in [37/50,39/50],        f1 in [7/20,39/100],
f2 in [13/20,69/100],       k0 in [1/5,6/25],
k1 in [11/25,12/25],        k2 in [21/50,23/50],
```

and every physical SPD metric, there are at least **two strict unstable vertices**. Incidental physical weak equilibria are allowed. More strongly, every one of the **46,410 labeled rooted true-edge trees** is incompatible with its nine weak-arrow inequalities under every nonzero PSD matrix.

The result includes all affine images. It also includes the reflected cut box obtained by simultaneously swapping `f0,f1` and `k0,k1`, still for every positive b and every t in (0,1).

There is a uniform certificate margin in the compact coordinates defined below: for every selected rooted tree, some nonnegative integer edge weights, supported on that tree, satisfy

```
  sum wij Dij(H) / sum wij < -tr(H)/10000
```

for every nonzero PSD H. The weights are independent dual certificate coefficients, not volume masses or centroid-balanced source loads.

A second consequence is an actual-shape collar: every uniformly filled convex polytope with the same literal maximal facet cycles and matched compact-coordinate vertices within Euclidean distance `2^-25` of this family is also U>=2 for every SPD. Its own centroid is recomputed. The corresponding normalized stress margin is greater than `1/20000`.

A new exact control in the covered region has **own222, weak000** on an entire metric ray with condition number tending to infinity. Thus the conclusion U>=2 is attained in this region and is not an artifact of imposing a spectral cutoff.

This is not a theorem about all six cut fractions in (0,1), all realizations of the incidence, or all E17 bodies. It does not prove S>=2 throughout the region. It excludes every joint S1/U1 metric there because it already excludes U1, without needing to discard or separately relax any inverse-metric obligation. The global bracket remains **34<=C_min<=622**, and no new 110 attainer or registry subtraction is claimed. The supplied memory retains these distinctions. fileciteturn66file0L67-L79

## 2. Input authority and what was done

The complete new journal was read consecutively through EOF: **1835 lines, 327832 bytes**, SHA-256

`befd664e58542c32de749c8d04b87b3522a0d18f3cc6b3371e26a12d980c951d`.

The literal parent is **minimum-0279**, SHA-256

`d29ef38046c1ca99c02309710e454af21163746b81c7c780054e30b1f102b55a`.

Its compact version-2 JSON envelope, with the literal Markdown's final LF, reconstructs to 43922 bytes with that digest. Its complete 16335-byte `centroid_flow_blind.py` was recovered unchanged at SHA `faf84e0d905d13efd1a1cf0cfc0f047915e25659a1edbeaf1a7d89e96de5d384`. No unavailable source or saved parent output is needed by the new program.

The inherited geometry, TREE410 labeling, four-arrow stress and the fact that its complementary dual detects the metric cube are unchanged. fileciteturn66file0L95-L105 This continuation did not escalate polynomial degree in the proved-blind balanced-flow cone. It first derived the true realization domain and moving moments, then covered all rooted packets using unrestricted nonnegative edge multipliers.

Numerical LP and eigenvalue calculations were used only to locate integer weights and choose a cover. The observed discovery stack was NumPy 2.3.5 and SciPy 1.17.0. **All promoted statements below were accepted by exact integer/Fraction arithmetic**, including the entire eight-dimensional parameter domain, all rooted trees, the actual control hulls and the unbounded metric ray. The standalone recovery contains every accepted weight and does not require numerical rediscovery.

## 3. Faithful native realization domain

### Exact domain for the stated cut-and-stack operations

The native operation is valid on

```
b>0,  0<fj<1,  0<kj<1 for j=0,1,2,  0<t<1.
```

There is **no additional coupling inequality between the two triples of cut fractions** in this native class. This conclusion is derived, not presumed. It describes the genuine cuts on the specified original edges and the stack between the cut-face centroid and the removed vertex; it is not a classification of arbitrary real parameter continuations beyond those operations.

Let P0 be the original quadrilateral pyramid. At B- use the independent tangent vectors `ej=Bj-B-`. In these coordinates the plane through L0,L1,L2 is

```
  a0/f0+a1/f1+a2/f2 = 1.
```

The retained halfspace has left side at least 1. Each Bj has value `1/fj>1`. Since

```
B+-B- = [2/(1+b)]e0 + [2b/(1+b)]e1,
```

B+ has value greater than 2. Every Rj, being a strict convex combination of B+ and Bj, has value greater than 1. Thus the left cut does not affect any right cut vertex. The same argument with the signs exchanged handles the right cut. Equivalently, the removed left and right tetrahedra have interiors respectively in x<0 and x>0, so they are disjoint.

Both cuts therefore leave the three Bj and the six Lj,Rj as true vertices. They replace the two opposite simple corners by genuine triangular facets and preserve the five old supporting planes.

The stack point has barycentric coefficients `t,(1-t)/3,(1-t)/3,(1-t)/3` in the left removed tetrahedron. For 0<t<1 it is an interior point of that tetrahedron and hence lies strictly inside every original supporting halfspace. It also lies strictly inside the retained right-cut halfspace, while its left-cut value is `1-t<1`. Exactly the left triangular cut facet is visible. Taking its convex hull with the cut body replaces that one triangle by three genuine triangles; the other facets remain unchanged.

The complete outward maximal cycles are consequently

```
F0=(0,3,4,1,7,6)   F1=(0,2,5,3)   F2=(0,6,8,2)
F3=(1,4,5,2)       F4=(1,2,8,7)   F5=(3,9,4)
F6=(3,5,9)         F7=(4,9,5)     F8=(6,7,8).
```

Their true edges, and only their true edges, are

```
02,03,06,12,14,17,25,28,34,35,39,45,49,59,67,68,78.
```

Thus V/E/F=10/17/9, with four triangular facets, four quadrilaterals and one hexagon. No integration diagonal is a mechanical edge.

At t=0 the added point is not a vertex. At t=1 the three left cut points cease to be extreme after B- is restored. Cut endpoints 0 or 1 likewise lose the prescribed features. The compact b-endpoints discussed below also lose a true vertex. They are useful labeled algebraic limits, **not E17 controls**.

### Distinction from the older lower-factor family

This is the parent's independent eight-parameter construction, not the older fixed-b=1/6 symmetric-small-cut `P_epsilon` family. The old family's optimized-factor claims and identity are not changed or used as mechanical evidence here. The native point `(1/15,.76,.37,.67,.22,.46,.44,.69)` is retained exactly. fileciteturn67file0L221-L243

### Reflected region

The invertible map `(x,y,z) -> (x,-y/b,z)` changes b to 1/b and exchanges B0 with B1. It swaps f0/f1 and k0/k1, leaves f2,k2,t unchanged, and preserves the construction. The vertex permutation is

```
(1,0,2,4,3,5,7,6,8,9),
```

and the facet permutation is `(0,3,4,1,2,5,7,6,8)`. Transporting the physical metric and its inverse proves the reflected-box corollary. It creates no additional catalogue count.

## 4. Compact coordinates and actual volume formulas

Set `beta=b/(1+b)` and apply the linear map

```
T_b=diag(1,1/(1+b),1).
```

The five initial compact vertices become

```
B-=(-1,0,0), B+=(1,0,0),
B0=(0,-beta,0), B1=(0,1-beta,0), B2=(0,0,1).
```

The entire positive b-axis is now beta in (0,1). All ten compact vertices lie in the unit Euclidean ball because they remain in the original compact pyramid. This change is affine, with constant Jacobian. It preserves uniform filling and transports the **actual** centroid. It is not a projective image with an ignored Jacobian.

For a native physical metric M the compact physical matrix is `H=T_b^(-T) M T_b^(-1)`. It is not reset to I. Every SPD or nonzero PSD matrix in one frame corresponds to exactly one in the other. The quantitative trace in Theorem 1 is therefore the compact trace; in native entries it is `Mxx+(1+b)^2 Myy+Mzz`.

Put

```
p = f0 f1 f2,      q = k0 k1 k2,      a=(1-t)p,
sf=sum_j fj(Bj-B-),                    sk=sum_j kj(Bj-B+),
D=2-a-q,
J=2 sum_j Bj - a[4B-+(3-t)sf/3] - q[4B++sk].
```

Then the actual compact volume and centroid are

```
  Vol(P)=D/6,                 g=J/(4D).
```

These are volume identities, not independently assigned moments. To prove them, split P0 into the two tetrahedra `(B-,B0,B1,B2)` and `(B+,B0,B1,B2)`, each of six-volume 1. Remove the disjoint cut tetrahedra of six-volumes p and q. Add `(Y9,L0,L1,L2)` of six-volume tp. The signed six-volume coefficients are exactly `(1,1,-p,-q,tp)`.

For a tetrahedron with vertex sum s, its first normalized moment is s/4 and its second is `(ss^T+sum vv^T)/20`. Hence these same five geometrically determined pieces recover all second moments and the actual covariance as well. The combination of the removed and added left first moments simplifies to `-a[4B-+(3-t)sf/3]`, giving J.

The code independently verifies the global polynomial identities for D and J against the 16 outward boundary-fan triangles. It verifies all 34 stated vertex/facet incidences polynomially. For the exact controls it separately reconstructs every supporting vertex triple, all maximal facets and the actual covariance.

Throughout the certified cut box, including beta,t endpoints used only in the certificate,

```
  5/3 < D < 2.
```

Indeed the worst products give `D >= 173711/100000 > 5/3`. Thus no actual-volume denominator vanishes in this certificate.

## 5. From complete rooted packets to U>=2

For compact centered vertices Xi=Yi-g, define

```
Aij=sym[Xi(Yj-Yi)^T],        Dij(H)=tr(H Aij).
```

If an SPD metric had exactly one strict unstable vertex r, each other true vertex would have an incident edge with Dij>=0. Such an arrow strictly increases quadratic norm:

```
Xj^T H Xj-Xi^T H Xi = 2Dij + (Yj-Yi)^T H(Yj-Yi) > 0.
```

Choosing one exit per nonroot therefore cannot create a directed cycle; every path terminates at r. It supplies one of the rooted spanning trees covered below. This argument includes zero selected derivatives and incidental weak contacts elsewhere.

For any selected tree, nonnegative weights wij with

```
Q=-sum wij Aij > 0
```

contradict simultaneous Dij>=0 under every nonzero PSD H. Singular matrices are covered algebraically; no ordinary equilibrium interpretation of a singular metric is needed.

The code enumerates all 17-choose-9 edge subsets, rejects exactly those with a cycle, and orients every surviving tree toward each of the ten possible roots. It obtains 4,641 unrooted and 46,410 rooted trees. A separate exact Laplacian cofactor equals 4,641. Every rooted mask contains a verified stress support in **every parameter cell**.

This is complete primal coverage. No stable-root fan, selected dual chain, covariance floor, nine-vertex theorem or independent polar metric is a premise. Consequently any actual same-inverse dual packet is excluded jointly whenever U1 would be required, even though dual packets are not separately enumerated.

## 6. Exact whole-domain matrix acceptance

Write the six independent cut fractions as their parent centers plus `(1/50)u_j`, with every u_j in [-1,1]. Define the polynomial matrices

```
R_i=4D Yi-J,
P_ij=-sym[R_i(Yj-Yi)^T] = -4D Aij.
```

They have degree at most 2 in beta, at most 3 in t, and total degree at most 5 in the six u variables. No Taylor remainder is discarded: all 219 occurring cut-power monomials are retained.

Three closed rectangles exhaust the full beta,t square:

```
cell 0: beta in [1/2,1],   t in [0,1],
cell 1: beta in [0,1/2],   t in [0,1/2],
cell 2: beta in [0,1/2],   t in [1/2,1].
```

For each rectangle, exact power-to-Bernstein conversion in beta,t produces 12 matrix coefficients per arrow. Each is still the full polynomial in u. Thus a positive lower bound for each coefficient throughout the cut cube implies the same bound for the entire rectangle, including shared walls.

There are **1,021 distinct integer stress rows**, with supports of size 3 through 8 and largest individual weight 516. The selected use counts are **724,538,376**, respectively. This gives **19,656 verified coefficient matrices and 58,968 strict diagonal-dominance guards**. These are counts in this certificate, not rooted incidence registry increments.

### Exact acceptance rule

For each row and each of its 12 coefficients, write the integer-cleared symmetric matrix polynomial as

```
Q(u)=Q0+sum_{alpha != 0} Q_alpha u^alpha.
```

The source constructs a nonsingular rational congruence G from Q0. A 256-bit integer-square-root approximation followed by 20-bit dyadic rounding is only a way to choose G; all its ensuing inequalities are tested exactly. It is not a numerical positivity verdict or a physical metric change.

Let `B0=G Q0 G^T` and `Eij=sum_{alpha!=0}|(G Q_alpha G^T)ij|`. The three exact margins are

```
m_i=(B0)ii-sum_{j!=i}|(B0)ij|-sum_j Eij.
```

All are strictly positive. Since |u^alpha|<=1, for every real u in the full cube,

```
x^T GQ(u)G^T x >= min_i(m_i) |x|^2.
```

This follows directly from `2|xi xj|<=xi^2+xj^2`. Congruence and `||G||op<=||G||F` imply a lower bound for Q(u) itself. Dividing by the integer coefficient denominator, the row's weight sum and `4D<8` gives the normalized physical stress bound.

The exact smallest lower bounds reported for the three cells are

```
0: 3349446076527671863653 / 10128152536144630000000000
1: 43892039403808145137157099 / 313144111067964976800000000000
2: 221634722607491382497129 / 1952139855997184000000000000.
```

Each exceeds **1/10000**, by integer cross-multiplication. The integer coefficient denominators are respectively 1080000000000, 4320000000000 and 4320000000000.

Thus every complete rooted packet has a certified negative weighted arrow average on the entire domain. The positive real b-axis, all stacking heights, all six independent cuts and every PSD rank boundary are included. No feasible-cell pruning or sampled-extremum acceptance occurs.

## 7. A quantitative actual-shape collar

Fix a compact-coordinate member of the certified class. Let a second actual convex polytope have the same labeled maximal cycles, with matched vertices satisfying `|Yi'-Yi|<=epsilon`, where epsilon=2^-25. Fill the second body uniformly and compute its own g'.

The reference vertices have norm at most 1 and the perturbed vertices norm at most 2. For each of the 16 boundary triangles, multilinearity gives a determinant change at most 12 epsilon. Therefore

```
|D'-D| <= 192 epsilon,          D'>1.
```

For the first-moment numerator, the old triangle vertex sum has norm at most 3, its change at most 3 epsilon, and a new determinant has absolute value at most 8. Consequently

```
|J'-J| <= 16(12*3+8*3)epsilon = 960 epsilon.
```

Using `g=J/(4D)`, `|g|<=1` and D'>1 yields

```
|g'-g| < 432 epsilon,           |Xi'-Xi| < 433 epsilon.
```

Old edges have length at most 2 and change by at most 2 epsilon. Also |Xi'|<=3. Hence every actual centered arrow tensor changes in operator norm by less than

```
  433*2 epsilon+3*2 epsilon = 872 epsilon.
```

The same bound applies to each normalized nonnegative stress combination. Since

```
872*2^-25 < 1/20000,
```

the reference lower margin greater than 1/10000 leaves a perturbed margin greater than 1/20000. The complete tree cover therefore still excludes U1 for every SPD.

This is a true-volume perturbation argument; freezing the old centroid would give a different and insufficient claim. The requirement of the same genuine maximal cycles is explicit. No graph-changing collar, global realization-space radius, or polar-centroid assumption is asserted.

## 8. Exact physical controls, including an unbounded 222 ray

All controls below use the compact coordinates, their actual volume centroid, and one M with N=M^-1. The standalone source reconstructs every vertex and pole, verifies all 120 potential supporting triples and all 68 true-edge primitives, and supplies the full covariance and census.

### Unchanged parent calibration

At beta=1/16, t=69/100 and the six parent cut centers, the coordinate transport gives the original b=1/15 control exactly. The transported parent metric is

```
[[589/2, 1424/5, 946/5],
 [1424/5, 174464/375, 5264/15],
 [946/5, 5264/15, 310]].
```

Its compact volume is 47426669/150000000; undoing the coordinate scaling gives the parent's original 47426669/140625000. Its census remains strict356, weak000. This is the same parent, not a renamed construction.

### CUT_STACK_BOX_CORNER_222_RAY_V1

Take beta=t=1/2, so native b=1, and

```
(f0,f1,f2,k0,k1,k2)=(39/50,7/20,69/100,1/5,12/25,21/50).
```

The actual compact volume and centroid are

```
V=373099/1200000,
g=(467859/29847920, 898401/596958400, 77156369/298479200).
```

Let

```
u=(2,3,5),  v=(3,-2,0),  w=(10,15,-13),
M_K=K^2 uu^T+K vv^T+ww^T,             K>=4096.
```

These vectors are pairwise orthogonal, with squared norms 38,13,494. Therefore

```
N_K=uu^T/(1444 K^2)+vv^T/(169 K)+ww^T/244036,
cond(M_K)=K^2/13.
```

On the **entire real half-line K>=4096**, the exact census is

```
S={0,1},  U={2,3},  H={45,68},  physical weak000.
```

All 68 primitives are nonzero. Each primal primitive is quadratic in K; multiplying each polar primitive by the positive K^2 also makes it quadratic. The code expands all of them at `K=4096+s`. Their 204 exact coefficients have the sign of their nonzero constant term, or are zero. Thus all signs persist for every s>=0, including the unbounded tail. This is a whole-ray proof, not a finite metric sample.

At K=4096 the physical matrix is

```
[[67145828,100638870,167772030],
 [100638870,151011553,251658045],
 [167772030,251658045,419430569]].
```

This genuine own222 body has C34 but is **not** a 110 attainer. It demonstrates sharpness of U>=2 within the newly closed region, not sharpness of the global minimum.

### A second new nonwinner at the opposite cut corner

Take beta=9/10, t=4/5, cuts

```
(37/50,39/100,13/20,6/25,11/25,23/50),
```

and physical `M=((5,1,2),(1,3,-1),(2,-1,4))`. Its compact volume is 956953/3000000 and

```
g=(-4728607/956953000, -3935985379/19139060000, 97988573/382781200).
```

It has strict468, weak000, again with all 68 primitives nonzero. It is preserved as a real boundary-of-the-certified-cut-box control, not as a survivor or additional coverage count.

## 9. What changes toward the minimum, and what remains

The actual parent's **entire primal U1 cone** is now excluded, not only its TREE410 packet or its earlier conditioned metric cube. More importantly, that exclusion extends over all positive b, all admissible t, six independently varying cut intervals, the reflected region and the stated full-shape collar. It uses the actual common volume law through explicit moving COM formulas while allowing the independent edge multipliers that the previous flow restriction had forbidden.

The new theorem needs neither S1 nor any spectral upper or lower bound. All weak-arrow boundaries are included. The exact 222 ray shows why it is inappropriate to impose the joint S1/U1 covariance window on arbitrary members of this family: these nonattainers can have unbounded physical conditioning.

The remaining native problem is the six-cut complement outside the displayed boxes, still with actual b,t and common volume. No full-cube exclusion or actual U1/110 survivor is supplied. The large-cut and degenerating regimes require new certificates or a structural argument; failure of a finite row library there would not establish feasibility. Nor is the native eight-parameter family asserted to exhaust all realizations of this E17 incidence.

The useful continuation is to enlarge the cut domain while retaining the compact b/t chart, exact five-piece volume identity and complete rooted-mask cover. There is no reason to return to the proved-blind centroid-balanced subtree cone. A full common-inverse analysis becomes necessary only if a genuinely complete primal packet survives, not because a restricted aggregate fails on a body whose unrestricted primal cone is already empty.

No whole-E17 registry count changes, and **34<=C_min<=622** remains the accepted bracket. No new attaining upper construction follows.

## 10. Complete deterministic recovery capsule

The sole source below, including its final LF, is **27482 bytes**, SHA-256

`7774c98345c9865abb4c67c01cd305c5630b06f2d353b1f72d59a3953682e174`.

It is standalone CPython 3.13.5 standard-library code, written for Python>=3.9, assertions enabled. It reads no parent program, saved certificate file, numerical optimizer state or external moment table. The compressed literal contains **every accepted stress row and every cell-use list**. Its decoded binary is 13686 bytes, SHA

`4ba07d9c90ecc42dae2393853f435a8f3c77e5b8e633548daee7227a815bed76`.

The format is fully implemented in `decode`: base-128 nonnegative varints, the row count, each sorted arrow/weight list using arrow-index differences, then three sorted cell-use lists using row-index differences. The program regenerates all polynomial coefficients, rational congruences, exact margins, rooted trees and physical control data. No continuation-critical array is hidden behind a hash or download.

Save it as `cut_stack_allroot.py` and execute **all three parts**:

```
python -B -S cut_stack_allroot.py --cell 0 > part0.json
python -B -S cut_stack_allroot.py --cell 1 > part1.json
python -B -S cut_stack_allroot.py --cell 2 > part2.json
```

Running without `--cell` performs all three parts in one invocation. A single part's PASS certifies only the matrix checks listed in its `verified_cells`; all three are required for the full continuum theorem.

Expected JSON marker in every completed part:

```
CUT_STACK_E17_ALLROOT_FULL_B_T_V1 PASS
```

Exact report pins:

| Report | Bytes | SHA-256 |
|---|---:|---|
| part0.json | 66393 | 7ea9e1a68992a339f3d0268d082e748a180e3d7b3472254e7a85a1b9e51cddf6 |
| part1.json | 66403 | 38fefdd1a5d85e38b355996cb9c06acdccc7272cd8be7800e9cbe952f534caaa |
| part2.json | 66399 | bf738f27fa436185cad58730ed6dc3eb5d72ee15519670ce819bbe1af687c42d |

Normal exact execution of all three parts passed. A clean source-only extraction and reexecution of all three parts also passed with byte-identical reports. These are author executions, not coordinator replays or proof-assistant formalizations. The finite exact acceptance accompanies, rather than replaces, the realization and mechanical proofs above.

Convenience copies: [standalone source](sandbox:/mnt/data/cut_stack/cut_stack_allroot.py), [part 0](sandbox:/mnt/data/cut_stack/part0.json), [part 1](sandbox:/mnt/data/cut_stack/part1.json), [part 2](sandbox:/mnt/data/cut_stack/part2.json), and [complete Markdown handoff](sandbox:/mnt/data/cut_stack/result_markdown_v1.md).

### Complete source


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]
