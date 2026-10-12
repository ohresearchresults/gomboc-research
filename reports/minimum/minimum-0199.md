# minimum-0199

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# PENTAGON_E17_THREE_CUT_ALL_SPD_U2_V1

## 1. Result: the moderate body has no complete U1 metric, and neither does a whole cut family

**The full primal U1 cone of the literal moderate-cut parent is EMPTY for every SPD metric, not only along the four supplied Schur pencils.** More substantially, the exclusion holds for an entire family of three independently variable cut fractions `(r,s,eta) in (0,1)^3`, on the parent's unchanged true `(10,17,9)` lattice. Every member has **at least two STRICT unstable vertices under every physical SPD metric**, including all finite mechanical weak-arrow walls. No S1, apical-U, polar-arrow, conditioning, or selected-complement hypothesis is needed.

A complete CLOSED subbox `[1/5,3/10]^3` stays inside the genuine minimal-four-arrow polar chamber: all four consecutive arrows are weakly impossible, and every proper three-arrow subsystem remains strictly SPD-feasible on each same actual body. Nevertheless NO complete primal U1 metric exists there, for any root. This is a global incompatibility result on an actual family, not another root-fan or apical-instability test.

The exclusion also holds on a **radius 1/20000 tube of actual own-centred, same-graph vertex realizations about the moderate body**, in the exact affine frame below, for ALL SPD metrics. Thus an open neighborhood in the parent's full twenty-dimensional realization chart—including its seven-dimensional fixed-actual-pole fibre—is U1-empty. This is not the entire twenty-dimensional chart or the entire seven-dimensional fibre.

The proof is an exact actual-centroid, true-edge stress cover: **533 integer rows, 1,758 row/cell applications, 210,960 shifted SPD Bernstein matrices, and 632,880 positive leading minors**, with a second exact determinant evaluation for every block. All **46,150 rooted true-edge trees** are covered in each of five closed parameter cells.

At the central body all four supplied apical proper-subsystem pencils attain strict **222, weak000**, for `0<delta<=1/20000`. These give a sharp U2 control for EACH proper subsystem on the SAME body, not U1. The new result closes all other metrics of that body as well; the supplied theorem had expressly excluded only four particular tangent/footpoint tubes.

**None of the positive construction tiers A–D is achieved.** Instead, arbitrary-root U1, apical U1 with a proper subsystem, all four proper-subsystem U1 realizations on one body, and110 are all excluded on the entire family and the stated tube. Global compatibility on genuinely different completions remains open. There is no canonical-registry subtraction or new bound: **34 <= C_min <= 622** remains unchanged.

## 2. Sources, reading, and identity

The new journal was read consecutively through EOF, including its complete literal parent. The complete Schur proof and source were also read. Earlier unchanged sources remain available; there is no missing dependency or scientific alias conflict.

| Supplied object | Bytes | SHA-256 |
|---|---:|---|
| research-journal(20260923-055204).md | 280247 | 2b3a8460644e36632e41f92f8d18c2a69ba370a797d5d0016f51abf4daa2b132 |
| SCHUR_PENCIL_GLOBAL_U1_TUBES_V1.md, [internal-source-reference] | 19148 | cdfafb30c57898d24345c62b407652dd54a01de90df481bc6be9a06b7b5043b4 |

The journal has1407 raw logical lines; Files rendered1419. Its delivered-file hash is not its internal working-memory hash. The Schur file has332 raw logical lines and333 rendered lines.

Authoritative literal parent: **minimum-0197**, SHA-256 `a7b006ad09534e46e35a14bb5255b09a5f091f2f1672ad26878cb0d4d6dbfc94`, OWN_CENTRED_E17_UNIVERSAL_PENTAGON_FACE_REALIZATION_V1. This is the **moderate-cut body with apex0**, not the coordinator's distinct one-corner family with apex4. The delivered source `pentagon_e17.py`,18130 bytes, SHA-256 `cdf46290aadcf61f5127120a0e267d62c7041d227c047194f3fd86d775043f01`, was read for its exact construction and audit routines. The parent’s full geometry and same-origin pole prescription are literal, not reconstructed from a summary alias.

The supplied Schur source was extracted unchanged and executed in build/check modes. Its12232-byte source SHA-256 is `2f4fcfd1c2cd73fd47c7f95565cc373c5435ba88ab562f674773a824e3cab37c`; its301990-byte report matched `e9b76379a35c176f33d573d7b9a194630e3293e669f920eee894a0eb09bf16ed`. This turn replayed normal build/check; the coordinator's separately reported earlier cold replay is not represented as another new audit.

The new theorem uses no external research, old catalogue, research connector, unselected archive, or parent-code runtime dependency. Its source is autonomous.

## 3. Exact actual three-shape family

### 3.1 A fixed affine frame, not a change of the physical origin

Use the raw labelled frame

```
A=Y0=e3,  Y1=e1,  Y2=e2,  Y3=O=(0,0,0),
B0=(45/92,-113/345,0),
B2=(135/283,1808/1415,0).
```

For independently chosen `0<r,s,eta<1`, define the complete ten-vertex input

```
Y0=A
Y1=e1
Y2=e2
Y3=O
Y4=(1-r)B0+r A
Y5=(1-r)B0
Y6=(1-r)B0+r(1-eta)e1
Y7=(1-s)B2+s A
Y8=(1-s)B2+s e1
Y9=(1-s)B2+s e2.
```

The code calls eta `z`; it is a cut fraction, not a coordinate or the normal Schur parameter delta. Integrate the actual uniformly filled convex hull to obtain g, then use `Xi=Yi-g`. The raw point O is a boundary vertex and is NOT silently used as the physical centre.

The relationship to the parent’s literal raw coordinates is the fixed affine map `Yold=C Y+b`, with

```
b=(-48/89,-48/89,1),
C=[(16/25,0,-7/25)-b,
   (-48/113,24/113,-103/113)-b,
   (0,0,1)-b]
```

as columns, `det C=55296/50285>0`. At `(r,s,eta)=(1/4,1/4,1/4)` this is EXACTLY the supplied moderate-cut body with the same labels. No new body is substituted at the centre of the theorem.

The three parameters are genuine labelled affine-shape freedoms: the four fixed vertices form an affine frame, `r=Y4_z`, `s=Y7_z`, and `eta=1-(Y6-Y5)_x/r`. They cannot be eliminated by an affine change preserving these labels.

### 3.2 True maximal facets and edges throughout the whole open cube

The entire family has the following outward maximal-facet cycles:

```
F0=(0,3,5,4)       F1=(0,4,1)       F2=(0,1,8,7)
F3=(0,7,9,2)       F4=(0,2,3)       F5=(1,6,5,3,2,9,8)
F6=(4,5,6)         F7=(7,8,9)       F8=(1,4,6).
```

All seventeen true edges, in the source's lexicographic order, are

```
01,02,03,04,07,14,16,18,23,29,35,45,46,56,78,79,89.
```

The degrees are `(5,4,3,3,4,3,3,3,3,3)`. F5 is a true heptagon; no integration diagonal is counted.

Geometrically, start with the pentagonal pyramid over the cyclic base `(B0,e1,B2,e2,O)` and apex A. Cut the two nonadjacent simple vertices B0,B2 at equal fractions r and s on their respective three edges. Replace the first cut's point `cplus=(1-r)B0+r e1` by `Y6=(1-eta)cplus+eta Y5`, using a new plane through the existing vertices Y4,Y1 and Y6. The first two cuts give10/16/8. The last operation replaces one vertex and adds one edge and facet, giving10/17/9.

The proof is not limited to small cuts. The source supplies a separate exact continuum incidence certificate. For each listed face take the polynomial normal from its first three vertices. Every incident support equality is an identically zero polynomial. All56 nonincident support slacks have tensor Bernstein degree(3,3,1), with898 positive and894 zero coefficients. All74 within-face oriented-edge convexity guards have degree(4,4,2), with1969 positive and3581 zero coefficients. Every guard has at least one positive coefficient, no negative coefficient, and full inverse power-basis reconstruction.

On the OPEN cube every Bernstein basis function is positive, so all130 geometric guards are strictly positive. Hence every listed facet is an exposed strictly convex polygon with exactly its listed vertices and true boundary edges. Each such edge has its two displayed adjacent facets. No further facet can occur: the known facets already form a closed component of the facet-adjacency graph, and a convex polytope's boundary is connected. This certifies the entire maximal lattice, not only its f-vector.

The closed parameter-cube walls are used as algebraic certificate strata. At r,s or eta equal0 or1 vertices/facets can merge; those endpoints are NOT asserted to remain E17. This is distinct from the finite **mechanical weak-sign walls**, all of which ARE included at physical interior parameters.

### 3.3 Actual volume and centroid, with no freely chosen masses

Write `D=6Vol(P)` and `J=24 int_P Y dV`, so

`g=J/(4D)`.

Using the actual oriented boundary fan from the raw vertex O gives

```
D = 203306/97635
    -(113/345)[r^3+r^2 eta(1-r)]
    -(1068/1415)s^3.
```

In particular `1<D<3` on the open cube, and `D>=1` on its closure: the bracket is at most1 and `203306/97635-113/345-1068/1415=1`. The compulsory tetrahedron `(O,e1,e2,A)` is retained.

Here is the complete polynomial first moment. A row `(i,j,k):c` means `c r^i s^j eta^k`:

```
Jx:
(0,0,0):6615782221/2542024860
(0,3,0):-115344/80089
(3,0,0):-339/529
(3,0,1):10057/15870
(4,0,0):4859/31740
(4,0,1):5537/31740
(2,0,1):-25651/31740
(3,0,2):113/345
(4,0,2):-113/345
(0,4,0):130296/400445

Jy:
(0,0,0):24898079588/9532593225
(0,3,0):-7723776/2002225
(3,0,0):51076/119025
(4,0,0):-12769/39675
(2,0,1):12769/39675
(3,0,1):-25538/39675
(4,0,1):12769/39675
(0,4,0):4281612/2002225

Jz:
(0,0,0):203306/97635
(4,0,0):-113/345
(3,0,1):-113/345
(4,0,1):113/345
(0,4,0):-1068/1415.
```

The generator derives these moments from the actual boundary, rather than accepting the table as arbitrary moment data. At the central point,

```
Vol=3435181/9997824,
g=(1111571226551/3577534900640,
   2785510668367/8943837251600,
   69222241/274814480).
```

Applying the fixed affine map reproduces the parent's volume and its exact genuine centroid. For nine controls—the central point and all eight corners of `[1/5,3/10]^3`—exhaustive supporting-triple hulls, halfspace-intersection reconstruction, two vertex-apex fans, actual covariance, and a new zero-first-moment fan after centring all agree. These finite audits check the controls; they are not substituted for the continuum lattice and polynomial proof.

Every actual pole is computed as `q_f=n_f/(h_f-n_f.g)` from the same centred body, where `n_f.Y=h_f` is its true support. The complete polar face lattice is checked against primal vertex stars. In particular the five poles0,...,4 form the ENTIRE true face at apex0, with consecutive primal-edge correspondences04,01,07,02,03.

## 4. All-SPD proof: a normalized true-edge stress cover

### 4.1 Remove only positive edge-collapse factors

For a lexicographically oriented true edge i<j write

`Yj-Yi = f_ij e_ij`.

Use these factors:

```
f04=f35=1-r
f07=f18=f29=1-s
f45=f46=r
f56=r(1-eta)
f78=f79=f89=s
all other f_ij=1.
```

They are positive on the entire physical parameter cube. The corresponding nontrivial directions are

```
e04=B0-A,       e07=B2-A,
e18=B2-e1,      e29=B2-e2,
e35=B0,         e45=-A,
e46=(1-eta)e1-A,e56=e1,
e78=e1-A,       e79=e2-A,       e89=e2-e1.
```

For the other edges use the full actual difference. Reverse orientation negates e. Let

`Zi=4D Yi-J=4D Xi`,

`Aij=sym(Zi e_ij^T)`, with `sym(ab^T)=(ab^T+ba^T)/2`.

Then the exact normalization is

**`Aij:M=(4D/f_ij) Dij`, where `Dij=Xi^T M(Xj-Xi)`.**

No nonedge has been introduced. Division by f changes neither sign nor necessity at any physical parameter; it only removes factors that vanish at nonphysical lattice-degeneration walls. Dropping this normalization when reusing a weight row would be incorrect.

All34 symmetric3×3 polynomial matrices have tensor degree at most(5,4,3), with1612 nonzero power coefficients in their six-entry encodings.

### 4.2 Complete finite inputs and certificate size

For each of533 rows, take the positive integer weights mu on its listed directed true edges and form

`B_row=-sum mu_ij Aij`, `w_row=sum mu_ij`.

The rows are inequality multipliers, **not vertex masses**. There are2413 nonzero weight terms, largest weight3473. Their support-size distribution is

```
3 arrows:80 rows
4 arrows:189 rows
5 arrows:181 rows
6 arrows:69 rows
7 arrows:14 rows.
```

These are global noncoplanar primal systems with uniform shape-parameter certificates, not a claim about the coordinator's separate coplanar five-support sharpness question. No minimality of the533-row count is claimed.

Five CLOSED cells cover the entire closed unit cube:

| Cell | r interval | s interval | eta interval | Row applications |
|---|---|---|---|---:|
|00|[0,1/2]|[0,1/2]|[0,1]|348|
|01|[0,1/2]|[1/2,1]|[0,1]|337|
|10|[1/2,1]|[0,1/2]|[0,1]|357|
|110|[1/2,1]|[1/2,1]|[0,1/2]|364|
|111|[1/2,1]|[1/2,1]|[1/2,1]|352|

For EACH of the1758 listed row/cell applications, the exact certificate proves

**`B_row-(w_row/1000000)I3 ≻0` throughout that entire cell.**

There are120 tensor Bernstein coefficient matrices per application. After subtracting the displayed scalar shift from every coefficient matrix, the source checks all three leading minors strictly positive. Common integer clearing denominators are `178697229988392000000` on cells00,01,10 and `357394459976784000000` on110,111.

In symmetric six-entry notation `(a,b,c,d,e,f)=(00,11,22,01,02,12)`, the three checked integers are

```
a,
ab-d^2,
abc+2def-af^2-be^2-cd^2.
```

The determinant is independently recomputed by fraction-free elimination as

`[(ab-d^2)(ac-e^2)-(af-de)^2]/a`,

with exact divisibility and equality checked. This gives210960 shifted SPD blocks,632880 positive leading minors, and210960 second determinant evaluations. The source also reconstructs every original power polynomial from every cell's Bernstein coefficients, using the exact inverse tensor transform. The coefficient stream and shifted-minor stream have fixed hashes recorded below.

The tensor Bernstein basis is nonnegative and sums to one on each CLOSED cell. Therefore the shifted matrix field is a convex combination of SPD matrices and is itself SPD, including all shared walls. No numerical eigenvalue estimate, discarded cell, or sampled feasibility argument is part of this proof.

### 4.3 Complete rooted-tree coverage and the global consequence

Enumerating all nine-edge subsets of this true graph gives **4615 spanning trees**. An independent exact Kirchhoff cofactor has the same determinant4615. Orient each toward each of ten root labels: **46150 rooted trees**.

For EVERY rooted tree in EVERY one of the five cells, the program supplies a row whose complete directed support occurs in that tree and whose shifted SPD certificate is valid on that cell. This is230750 raw root/cell cover records. The number is for this literal graph—not the older bevel graph's5440 trees, and not a canonical incidence count.

Suppose a weakly nonnegative physical escape tree existed under M≻0. Its assigned row has every `Aij:M>=0`, hence `B_row:M<=0`. But the SPD certificate gives

`B_row:M>(w_row/1000000)tr(M)>0`,

a contradiction.

If the actual body had exactly one strict U, each other vertex would have at least one nonnegative TRUE outgoing edge. Choose one at each such vertex. Every chosen arrow strictly increases the M-norm squared:

`|Xj|_M^2-|Xi|_M^2=2Dij+|Xj-Xi|_M^2>0`.

Thus the choices are acyclic and reach the unique sink, producing one of the exhaustively covered rooted trees. This is impossible. A maximum-M-norm vertex is always a strict U, including tied maxima, by the same identity. Therefore there are **at least two strict U**.

This proof addresses full global U conditions. It does not stop at apexU or at an unverified topological arborescence. It includes incidental zero arrows and physical weak contacts, because the hypothetical nonroot escapes were allowed weakly nonnegative from the start. No polar assumption was used.

### 4.4 A short actual-centroid routing constraint inside the cover

Row0 alone says, throughout the full family,

**`13D10+13D20+24D30<0`.**

These three edges have factor1. Writing the actual centroid in the raw tetrahedral frame as g, the negative of this scalar equals `S(g):M`, where

```
S00=13(1-gx),          S11=13(1-gy),       S22=50gz,
S01=-13(gx+gy)/2,
S02=25gx-13(1+gz)/2,
S12=25gy-13(1+gz)/2.
```

The certificate proves S(g)≻0 for all actual centroids in this family. Consequently the three surviving original base vertices1,2,3 cannot all escape directly to the apex. A prospective apical-U1 tree must reroute at least one through the actual cut geometry; the remaining stencils exclude all such complete reroutings as well. This simple moment-dependent gate is not, by itself, the full U2 proof.

## 5. A complete three-dimensional subfamily remains minimally four-arrow infeasible

The all-U2 theorem does not depend on the polar chamber, but its relevance to the assigned chamber is certified on a substantial closed subfamily.

Transform the actual centroid back to the parent's raw frame:

`gold=Cg+b`, `h0=1-gold_z`, `t=gold_xy/h0`.

The actual five poles have the exact representation

```
phat_i=p_i/(1-p_i.t),
qold_i=Lg(phat_i,1),
Lg=(1/h0)[[1,0,0],[0,1,0],[tx,ty,1]],
p=((0,0),(2,0),(2,4),(-2,5),(-3,3)).
```

This accounts for recentering's PROJECTIVE change in face shape. It is not an independent polar recentering or an assumption that the raw pentagon stays affinely unchanged.

On the ENTIRE closed shape box `[1/5,3/10]^3`, five actual-centroid polynomial inequalities give

**`-3/1000<tx<0`, `-1/200<ty<1/1000`.**

To reproduce them, put `Jold=CJ+4Db`, `T=4D-Jold_z`. The five polynomials are

`T`, `Jold_x+3T/1000`, `-Jold_x`, `Jold_y+T/200`, `T/1000-Jold_y`.

All375 tensor Bernstein coefficients, degree(4,4,2), are strictly positive; full power reconstruction is verified.

On the enclosing CLOSED t-rectangle, use the actual planar edge vectors `e_i=phat_(i+1)-phat_i`, i=0,...,3. The two nonnegative displacement-circuit rays have supports013 and023, with their coefficients given by cyclic2×2 determinants. Both have all three designated coefficients strictly positive. Set `lambda=r013/2+r023` and `Q=-sum lambda_i sym(phat_i e_i^T)`.

An exact16×16 closed interval grid proves35 guards per cell,8960 in total:

- the five denominators and fifteen polygon convexity determinants are positive;
- all six nonzero circuit-ray coefficients and all four lambda_i are positive, with `sum lambda_i<40`;
- `Q-I2≻0`, while BOTH individual circuit stress matrices have strictly negative determinant.

The minimum rational lower guard is **247/250**. Every interval cell and shared boundary is included; there is no pruning. Interval dependence is conservatively enclosed by exact rational arithmetic.

The two displayed rays exhaust the nonnegative displacement cone: their positive coefficients at indices1 and2 determine the two combination coefficients, while the independent edge columns0 and3 determine the rest. Omitting arrow0 or3 leaves no nonzero nonnegative circuit, so strict feasibility follows from the linear alternative. Omitting1 or2 leaves one of the indefinite circuit stresses. A positive-definite tangent H pairing positively with that stress exists, and the same linear alternative produces a strict k and then a genuine3×3 SPD extension. Thus EVERY proper subsystem is strictly physically feasible on each body in the subbox.

But the combined stress is negative definite on the tangent plane. For any physical N, with `H=(Lg^T N Lg)_(1:2,1:2)≻0`,

`sum lambda_i D_i=-tr(HQ)<-tr(H)`,

so some selected arrow is `<-tr(H)/40`. Hence all four weak arrows are impossible. This is the same minimal-four-arrow phenomenon, now uniformly retained in an actual three-dimensional completion sector where the FULL primal U1 cone has nevertheless been proved empty.

The strict proper-subsystem metrics may vary across this subfamily; this section does not claim that the original four fixed matrices remain witnesses throughout it, or that the distinguished apex is strict U for all those existential witnesses. Explicit apical witnesses on the central body are preserved in Section7.

## 6. Uniform escape gaps and a full-metric actual shape tube

The whole-family certificate yields a quantitative **normalized** escape gap. In every rooted tree, some selected arrow satisfies

**`Dij/f_ij < -tr(M)/12000000`.**

Indeed `B_row:M=-4D sum mu_ij Dij/f_ij`, and `4D<12`. There is no asserted uniform UNNORMALIZED edge-arrow margin all the way to a vanishing physical cut edge.

On `[1/5,3/10]^3` every f_ij≥7/50, giving the physical margin

**`some Dij < -7 tr(M)/600000000`.**

At the moderate point,352 of the same exact rows cover all46150 rooted trees with the stronger point certificate

`B_row-(w_row/32)I3≻0`.

Their1056 positive leading minors are checked separately. Since the minimum central edge factor is3/16, every tree has

**`some Dij < -tr(M)/2048`.**

Now let Xtilde be any ACTUAL own-centred ten-vertex realization with the SAME labelled true edge graph and

`max_i ||Xtilde_i-Xcentral_i||_2 <= epsilon=1/20000`

in the displayed affine frame. Exact checks give `||Xcentral_i||<2`, so every true central edge has length<4. For ANY SPD M,

```
|Dtilde_ij-Dij|
 <= [epsilon ||Xj-Xi||+2epsilon ||Xi||+2epsilon^2] tr(M)
 < (8epsilon+2epsilon^2)tr(M)
 < tr(M)/2048.
```

The exact last inequality is verified. A hypothetical nonnegative escape tree of the perturbed body would retain a strictly negative arrow from its central certificate, a contradiction. Therefore **every actual body in this same-graph tube has U>=2 for every SPD**, without any metric conditioning bound.

The radius is in the specified coordinate frame; it is not compared numerically to the differently normalized Schur-tube radius. The theorem does not permit new edges or facet splits to be ignored, and it assumes each perturbed vertex array has already been centred by its OWN actual uniform-volume centroid.

In particular, the supplied full-rank centroid actuator and seven-dimensional fixed-ACTUAL-pole fibre cannot produce U1 by a sufficiently small completion change around this parent: all such nearby actual realizations fall into the tube. This uses the parent's actual fibre theorem without claiming its whole global fibre has been covered.

## 7. Preserved actual reciprocal controls and sharpness

The central parent’s four stronger H/f data are retained exactly:

| Omitted polar arrow | H | f |
|---:|---|---|
|0→1|((1,1/100),(1/100,1/10))|(35/18,1/600)|
|1→2|((1,-1/2),(-1/2,17/64))|(31/25,149/60)|
|2→3|((1,1/4),(1/4,5/64))|(-1,8/3)|
|3→4|((1,1/4),(1/4,65/16))|(-1/20,2/25)|

In its normalized actual chart A=e3, define

`Nc=[[H,-Hf],[-f^T H,delta+f^T Hf]]`, `Mc=Nc^-1`, delta>0.

If `T=Lg^T C` maps the new centred primal coordinates into that chart, use the ONE physical pair

`M=T^T Mc T`, `N=M^-1`.

The source reconstructs all68 physical primitives and their exact affine-in-delta coefficients, verifies the local three positive arrows and apexU, and recovers the complete positive breakpoint counts20,22,21,20. At delta=1/20000 the full actual censuses are

| Omit | Strict S | Strict U | Strict saddle edges |
|---:|---|---|---|
|0|4,5|0,2|18,35|
|1|4,5|0,3|03,89|
|2|2,5|0,1|07,35|
|3|3,5|0,9|14,23|

All four are strict222, physicalweak000, with ALL68 primitives nonzero. Their signs are fixed for every `0<delta<=1/20000`: each signed affine primitive has nonnegative intercept and strictly positive value at the upper endpoint, with a nonzero coefficient when the intercept vanishes. This is an exact half-open interval proof, including the unbounded-conditioning approach delta→0; singular delta=0 is not a physical metric.

These controls show that the new global U>=2 lower bound is sharp, and that each proper subsystem plus true apical instability remains genuinely feasible on the SAME body. They do not supply U1, and their two spanning escape components cannot be presented as one rooted escape tree.

Nine additional exact identity-metric controls in the NEW affine frame are preserved: the centre and the eight corners of the closed chamber subbox. At the centre and the four corners with r=1/5, their strict signature is659; at the four corners with r=3/10 it is6/6/10. All have weak000 and68 nonzero primitives. The new-frame identity metric is not the parent's old-frame Euclidean metric; the different census is not a discrepancy. The complete supports, moments, poles, metrics and primitive lists regenerate from the source.

## 8. Scientific effect, failed simplifications, and scope still open

The investigation first checked the full primal escape requirement of the moderate body, rather than searching only within the already closed normal-Schur pencils. Integer stress discovery then extended to three independent actual cut fractions. The final result no longer needs local polar-arrow assumptions at all. It must therefore be credited to **pure primal geometry and the actual volume centroid**, not to reciprocal coupling or defeat of a cofactor relaxation.

Numerical linear programming and eigenvectors located candidate multiplier rows; those rows were frozen as exact positive integers. The final standard-library source independently reconstructs their polynomial fields and verifies the complete continuous and discrete certificates. No failed numerical search, rejected weight row, or failed unsplit coefficient test is interpreted as an infeasibility proof. Conversely, validity of the five-cell certificate is not inferred from the numerical locator’s success.

Two shortcuts remain explicitly invalid. First, universal freedom of a true pentagonal polar face and strict proper local subsystems do NOT provide full U1; this entire actual chamber subfamily and a full-dimensional local realization neighborhood are counterexamples to that inference. Second, keeping raw five-plane coordinates fixed does NOT keep the polar polygon affinely fixed after true recentering. The actual projective centroid map was used throughout.

The global question on ALL actual E17 completions in the minimal-four-arrow chamber remains unresolved. The three-shape family ties the three fractions at the first simple cut to r and the three at the second to s. Six independently unequal truncation fractions, genuinely different base/pole shapes, more distant fixed-pole completions, and other incidence classes are not covered merely because they share local pole geometry. The small same-graph tube adds unrestricted nearby actual shape directions, but is not a whole-fibre theorem.

Thus no arbitrary-U1 chamber witness, apical-U1 proper-subsystem witness, same-body four-subsystem U1 minimality witness, or110 body is claimed. All four construction tiers are excluded in the precisely stated family, not globally. No canonical type ID has been assigned and no global register is decremented.

The most useful continuation is now to leave BOTH the complete equal-edge-fraction cut family and its certified local same-graph neighborhood before pursuing U1. The exact normalized-arrow stress generator and the explicit centroid-dependent routing gate provide tests for proposed departures. Merely changing H/f/delta on the moderate body is now rigorously exhausted, not an open optimization task.

## 9. Complete source-only recovery and execution pins

The capsule below contains the entire **39189-byte `pentagon_u2.py`**, including every one of the533 literal integer rows, all five row/cell masks, the352-row central mask, the full actual vertex/moment generator, true-face continuum certificates, exact Bernstein and inverse transforms, both determinant tests, all46150 rooted trees and their cell assignments, the closed chamber certificate, all actual controls, and the physical Schur-tail checks. No source file, matrix array, certificate table, old report, cache, numerical optimizer, or parent capsule must be downloaded separately.

Executed proof environment: **CPython3.13.5 standard library**, assertions enabled; recovery transport uses zlib1.3.1. Original build/check and a source-only cold decode/build/check completed, with byte-identical reports and stdout. An initially time-limited combined cold command was rerun to completion; the reported pins are from the completed runs. This is an exact author-executed reconstruction, not proof-assistant formalization or an independently authored mathematical audit.

Save the following capsule as `recover_pentagon_u2.py`, retaining its final newline, and run

```sh
python -B -S recover_pentagon_u2.py fresh
cd fresh
python -B -S pentagon_u2.py build > build.stdout
python -B -S pentagon_u2.py check > check.stdout
cmp build.stdout check.stdout
```

| Object | Bytes | SHA-256 |
|---|---:|---|
| recover_pentagon_u2.py | 21152 | d10ff6b31447157312cf302e1ec923aedbbb82e12f4409b20cb1bfdcdd9c6696 |
| decoded pentagon_u2.py | 39189 | 5a8a2e139b587623fe2496648055de6b4b50bc166f401b5b6a7c5699e1e654c3 |
| pentagon_u2.json | 15150911 | 51cc9851f802ac5403d013a902ae113d8a6dc2584046f35c5f5bd26ee67ec7d6 |
| identical build/check stdout | 713 | 44a02c03fa4d59517048a14ce1715969309bfe0d4093125ad98a2e178f9712fb |

The coefficient stream hash is `f390d3d0844e93135dfb7e93edc1e50dfd5f4de4006aeedee9704ba545363469`; the shifted-minor stream hash is `01c693bbbacf53bc71678cd4c46149cac489ee6cb38c845b29f4b5b50ef3feb3`. Exact stream ordering and encoding are in the runnable source, not inferred from these hashes.

Expected terminal output:


[Encoded source block omitted; the code in this passage is incomplete.]


Complete capsule:

```python
#!/usr/bin/env python3
"""Complete self-contained recovery; CPython 3.13.5 standard library.
Usage: python -B -S recover_pentagon_u2.py fresh
"""
import base64
import hashlib
from pathlib import Path
import sys
import zlib

DATA = """
c-p0XYj@i=w&-{L3e9xQu_(h10lww1>pF?kq?5OuOf$MVT9ioHwDpQ4J9cyW-|v2bq+}<Zo|~>(BnWJ5Z0t8c@Tb2$x?Zmyjmr6>
Vt&(J-fb=xbFcOHzyJN+$(ys|U*5hMp6F<J_Tt0I$?)mNv*GcpSHshH&xRk(@RRPfv+K=bzL+hp*X`mq8*kd<VzntJ<v80EhpngY
2wvMe)ZSsxUT?B_o~`osv>dIn)!k8hzG$x()0<+Y+8^HhqT1tZd{ML)tM)Qm74uDdQceNP$8~mI^aQ!~!ISpEX?qEev-8D#cx?`s
ckR)2InDnE8jr79X8;0Fxz48T1ypOVFS2FP9$$}&cDZhMR%)$&ciQE=-Eoz6{@XijKb<btMb1^eX4C1q4c)i0>3IQomgDB2U=XWp
lPN$Q20P8l*}A=$v^UTv5UM@N#zlLYZ8jzRLg5O~KQ1qOuhWkI?9rsWbe@%$s{JetKP{%$vqHfTFRAr%u`V~|4YXQa7Y9Xt4seS3
`Q`#)ZWgOUoRn5MTP{|c_C>b703xc(^<u8pck9+<wU`0XHdxx0O7Gy7AI#v&mQKerE}X0YZn>DR?UUzH(9YKF=Uk`Uz{nSiX;o*r
TIAQ`jT$dzz%v=OzuyNwZMB}CrX3)$rvl|W3a)%0H~wlBtB9^5l_*13MtSh7RS2~`xJy(F_deW(@Ebvkgr56w@3c;yrJL*JwCJp%
yCUzbi%n;%pm3b_1o&uz^Zfjjt_!^Wy<B!CYSP!e!TzM*(*p<owT?dsysWNy@{F!C;*>%a{a)_?tGAxGY3F&z4^#rEKkpo9?J3U>
@Y;2pqbCL*YcEhH_OMXLZmhJgZH*SN&3fH_x0v4bTJ5};w1>lTUT%g%7{_#?Zd2ER2W`AL9H)6X-gIt(VPP!ma*jeYE;_dg%bj*H
T^DVxayY(U2|JNWoo_&9_|NG*2XKF2)mwh@?GMM|k>$BXV?jtPQUuXiI7h3L5jq?%mUkU!LFBnoH%OoblmoNO)*Yv}>R%1g)!{kJ
$rX=y{|0KWip}+EPQ&heyXxIEo3CtR#Oemo84g#3ODZ^71n0%MAP608Lp<05DaZ=kdW7riQDcMx0&n*ZWTdv{>cOf~Y5xGrZPnTJ
^!sG{_J`0adk8bEO;1Pa>n<hnQTs|*^LGD^>fNe4%gC7;0mD5+@9x+C4aI2~sSL-C4fRo8-aJgSF0i+%Nw!>kwe_wD{cOHwN@&Y4
CH0=o&x;OJ!RPRQmx*aHh7t?0`0{YaAQ+a!hhtlL47%G^U)I&HXPuj_Xf8ytSOKAy&iA>+X|)jG{U$J^+f=t?Hb-_I=+SLA9d)}|
%MRj}fdKc?JXvghJekx4`0k-52R~{uhMU`+7Fm~DQ2kr3m@hV4u#q^o-5)?6uNLd|R+CQF*Msh;Zw3b${DCVyP;%vBnafX=Txl%R
{8W%AHeM&I01{5{P)T1Fo?yV15e$u(ZkU9(spzt!W4_YP(TPrh7pd^Xq-17Xr<#q<u{zP}#HhClX9Vb_4_4}l>nONfsbhyOY}o@<
x^VZq13;iA%4Jn$t)3XFvL+}Gl~bb!9~j3n+kCN_Wz+KaA|ImhZw$5`Vm<5!2Yd86-KAAayoYs)+TVA2I3zT@c(q1@8p{=!T)6^+
&GktA@ISP~FkfhqL;4NqSBQf4+3BtEH=*B{enIc$W!*Kh^%EC}BnZ&Gp?g9@?oZH3AZ%;_dI*FRv~F!71VlX01cC6v21MfD2?~}I
o-p%*B2+lx29fRIgi(ka_t5x{R?`zeRR(&pAg>Qfa9BP3(=P@oHu~HzfNKW|f8D{r*{Ls+(34+mr7PByLWS^{7iNnYxVP)hXPo{|
seAORo%mMMtLa%AT&q;Az-jDEoCD3)<8GbyKljT)t$I5Xl(Y%h4E(bX9?jq=Pe~&0)`)le(|(#mkI1jTBAe#Ky7>Ry8r#BOXoWv0
qP2*9QojoN*=7a)FIzC;!?a_K5ZDVa#x>d<VPhpctc2GQ?tOMXf<DrkI!FIb`!eT#_mjGF)UQsh@jefZfV4!`^gGhkYA>!gX@9V#
(T_hM>57!*cgw3}wFm?&(gNo<dpu$fiutfW@_}myK69IyVuT!#4V*NE8i35h;J6`Ra+ob4V9CXmC6aai4een9yG8$UuunIacvB9X
M}`Mms!OIM(@`rHAoi=-<2F=ooaS_WRzOSzy^8+1o(-#sgYYYxt#SIAbI_II|J^Lyp92f;PiEn-&%r%X{*a3QKSZp^w^<d!@XfK5
`5K`%qos}rDg;0YyGZ$E+V8W34jYo}I)kQs11OSc7=C*448->c8p1&AKszI4x>w*1V)3Xh&ail2BhKLE6!Y|(`^V8{kuOq^W$Tz?
2Uyl{MyXTog8fjS^~mZo1k}Snho}}t4gs`Xjzs&RCc-+-W9|0Fi}|LUUl-EjYQcc2u~Hw5A3n1v;`QKYmaVTq3of&?4<T4r<0U^z
@vlXCdl=sv$6px;_544ne*Cy|_1|ECq1(|Q%@9t5$2wR`Ats91ZJB|62geH9m9^%D8GMj+M#TyOwxXPOmLTzKHCkNHb1(<RIq(z`
=BGA2Xiv-a<_Oy@uQA3hCX;epVw$9!=fy2VbLAYLVCDH@R%TNrNf{g2gI8UwQv}ly-?q~ge$0VI2-TeI8}|*|#QhLMe=W-Mi_N-X
?n~9_Oc&~+bkv;kDFx_|VwG)*4!V%r!(dj=>R_m0wC4M|4ugsZ%AsNZN|C9ZL2QlU1QGd#)1|8`xT1taXAW0Rce?0yJH-J!?p%}y
(}mORUJ&Su8uSdP4G<j>3>li8&@2-}OGp+Zcti(Vq0cdeGy_5EU!i3r+h3JxEY(=58>I$I4VIb#3w^;M$g&ZCQ2CNdapng#*AN=5
R_iAS>m*@R&Nsz*v9g2cwTo<g(Ozcdit=4x#)>g$&PHO1_(e$r=dktR?Z1X+C%>Jgm}1gB%xB=Apl5uzH3?k#zVhHQY=JEMpas32
7g336dA(3Usdlk6fd-+%B7-nmK`)VqI_yDfAHl&R{G0TA(*kfV!Vi=O4X{7$E5GL@3Lb~>*ozUH0P8?|XhL{lZ7*n<o(5G7)qSO-
UJyWkUVt6?RKw_2*z-KBVIr*IyR8}<i!Y1>K!#Z6ML1v_zcB(45CS{U3p_x`L;QS2z2f*>0B;BwfH!V0FbK{?gyBBKdm2E3<JB>s
g5cp1jsVd~h@Mo}3z42W!V-^Y1VcrdB#c4~qro;<gHZAi5;oB|YM(~!(VTd#80Qb^;t?7?pka{AhAKpel~2!I1PO$M{;?+0wMCEu
oEaDzbQlm3HDZdS)GZ$&CB4wl<c3(mC}^HggSbUii7GlEu0eVlgsKCkVi3cKm`VoQ1HLg%49*%3Fu>{>k?^oLAK66{_P|xdKhQJ&
4Va4p;)?|F1BwxCkdQP!071ARhy+1+*aABDh<zgDVt^YH@(E64=rgM!kt<#!t}-}_LS^bO?#0w8O|6T(L6oFv0;ckX2tG|44k&P;
jc0K*h`9-ns4~qgURWPVgGd_?0q7if5mBe!0%92$1yS5E(wex_C;pC*FG7+AJ8v*Ac8ZYM08`>_5{yvOn6L?Pa-?Y{49;vwlTL&7
2`0o&y?`bF2Tkk@SS8FDnzTU>QTqtz&fq9nz+vkBip0d-NR}u;q&>Vx)&Wtg#KC}wha}OOc`In4+(CuVqnWeP&<pu_0v)hw3Va-6
0tlll80nBzS^yma-FX@-oIN594p9?hhgMjK5l|7abQ`V&vz-u2$Am55)q-xIbF8d!Qem1{rY#7XPEQLD2E?BRAvY^~IN?b0fS8wt
;UlxL^s&A%3<-*XUjPPFHWBeO!SG32Fx3LY36O-@w0Z%x9cVY=f&j5b0V9o50|`;PMgp63Cq0Z?q{9<Yw1%h>^Ry;}4E2rdm9$)$
Y>x$<XTWWd<Pwpz5neW^qqN8B2(k6GC^s|<BHJzvlW3=XQPDn0G?WvS2w7_cP`zjtZX6%=ief{&t=Sq;kHDO$8|(xi>L{o*7R{<B
1lo~Gfx19Z;24BNnwEzgv%SE|NIB>vB9%g#7w6uEksxlGM@>>6P?_A4Hj+Y*%^Hmmc`4y(($!2D((MsSh>N3xD<#%7Bul9gFfl0_
CYoNOSy9Kt7A_5fiHQ?L)&d29L>YM&rNHZXmI@&$DMQvNAPx+P?qs)7TA)uRnN{o51sg-_HjuLSNFb3l$OIvT7}*}xBjJaP2!9cP
PYmo5OC(q|0-6*1>V&zPZ5F~%BqSlKSR6l=C5n(l9t@~|oCY**K-CaM-dYsER0>f=CZt@Ek5NhxS)z*Qd=_)D7AU#MGBL~n4$QI{
^<=0qTW+LVRB5nEi|fSljHVg$iB&y@(IQ8ynpi^;i_%7d$;upu7ofDoqR2c()@5VGh9)LW6_L*Xg5L5(D>94utgiePQ8gw^TzrO1
?z0$ck}{S%<Yyw92Db4@(-<v$6ANT<aY9xptx&8r@d9gi6AP0O0;on~M2=KAa<oV>Nfx<=>||)7yo=qDZvsS#MR_Ad;ksp*mqI49
heRXS)njh*P=1j6V^IUzZE&a&SC`cYPZMc2k6b?Xnn<igI5oLE*4y%^y5Z_*5y_XuQ5b6$43s9~e_@N5S{S4eI}^l#$nL0~iQ);`
E76u@+YK@bGiJr%s9A}=AsL}a{70gTHbNup0)V%CDNTqiNVy{u`kv@n^xTMr09`C0nS;iL3@p?}7Y0Dsxd0~v&^1X*NQTyai*Uvg
j%FM*FDmDtB{B;luVd@tkv8y=X~{b=K2Iwc8Wplb%>fC~fxRd;iyo;al5wM0fhJU%&@c?StS|#qjXe+&bo6F5@o^By#Dz?Dbmv?f
|L7K5H=KAHoajHabSPOeLKZ-BUJR-QLuMWw{{Tnqk=Y?qljlcTz-v`=gB(cuN_@24nw699kt*U~1erG?*%5;j)dq=dc5H=`OgA!-
xW#P6$<xP&At(XV0lsT(1i8NwH<21cQDukGZEd+E9&utqfsPT^(r2}2gn+DEJocKo4MbVc9XYC47?UYPMZz{;f)qo7Mjf(pWU=uC
5B3Lqwt7D4NzyL{xrI61_hiD!BvE&U47w4|l!Ky3qy&KrCxxOBnS8+GrbpV1NTHd*QOrnH8TMajz#50fUY=n}(o6z-k?YRBRoEkW
kC^2u56JUGa4PlBE~trEpT#z4b!*>-EHUm)VCWvZG%oQFbG|0sM_7<%M-C<>Og=iYE&1RHhi{;ESS4#zrsTqr4yQ8Gm}EKG4>srl
v!)2hgc~t86lbu@Nq#HYao}KbVko(w$tNMpWW+r%5gQb-OqJTDa7u(AVOJ8lfJIk_GQUPu4l}{Qpp&h3fDBeKFj_)`ssah)ieJaW
aH*q&WYJ>mTYDAL4EgMkSgXm(o8}o@Fq?YtIjj)5V3#Je_L9AOEe^ZIP(~eaFe7Y|5DNvYSAb@8&py5<$q4opXwp4a$JJ2S|FDLM
1tw~E8q@}A(=cjxi8xLp!w2HYm{<%;#QqhO#;oqhSRiK`<Oudf{6IXcK;*(BvrFof6F8Ppg*nmc5}AFDb~v*WlMRniy|Kh_ToJH`
(lXV^HA{)X5h7w}49Wl2u?W9r%Nd~NaLMV%*seu!Jmc$1Wh233(&I4PShj~5^dvUY#3c!5R6MTD-ZgL>snkRQsvu_HjnV)BTyfk<
VY9f8hS=ESfGA+c4IMC*h+ZWRjT2nP+PjeLKB_rV@noAR)FZXyYpXp22`<UU4cUDnppiIu6p6BrXdP9=isq4f(q0oTPPZ>%ebA8F
P}~VjT{TNQ8?z*oHn77ZR6JzJ03&MB5WZV^f<}Be6rV_91&aj9Y~V?TMvKgPV);0O!G5)6YX%IKf%G&DKvRwmNsiLVHkG5im{Stu
=EO7wfD;WHEoZ|~5)qWl8S(}VD)5;VA;bb(LGFc@cpUCBdJ)FAk?1OGo+Xx#iFz!$A%!|59<kUJe8{;})(YC@w>Y*X2Umv@`LZ-?
N;HH_K5`f(s4%ezf*~zpM7OYGY%>-V{As^2kFL#5A%$8L@5Uk*KFKY2Xp<MLJ|c0bwVfccAmYbx(82i=?7bC;uY{Z#Q15}HipYyL
XzIji*47~tzmPHktW}Zwv{*gka^fYH;Eb~b9FJ4d!=vcY*s#}=)FBSgb6tv_Sy<S6(JsYbQNS|5vPF?_APG%U&E((c#Cko%Kj`0K
8i<8Yg0M)u8jmpr+K`+BG!7T7K{b?;WyfFJ;E*{(OPU7<+{`*bbifG*He+m1h-D20@v(LBh~2O_W@AG61V5D61a+#-Ka<Um#Y+}`
3~25eStQJb#5Oa)+(XGLlD5bqON=U+ZNn*J?Mb|-ZL)y|$azg8o`#{URl><SV)(>T)JUiZ&wY;PVp1riw+$sf;ZekXI@u3Hkt|L+
S!OU79*0=0J_26Ypv(nvJn0Z)(;0zSQ_`I~675;N8dH+BGRs)%i)4V(m+&tnMTD*rQ<O|cBx!Q55lbdwEGPydri&7C@ra>4$<Jxd
Mu(EiL#05xW7zrt2_qSXiS7DK&|?i`1WO$YP~+BW*sEPERITXMB2S=2($=%2+)zRh6UsL<<MfjeVJ5#7+ZyXvdz4l6<B9<_hqmbC
Q5HdBchLhzvYm#}3#>G_6wI(zB0bOg!;`#Ai>SomnQNOxbyh$;4N^-cu5&fKNW(HoI#$ypi>pYnt1F3rpM4|XIi!lmE_0Ps<3%G0
KREhp1V)%6;3T6jVPsrqV-pD@sISoGnTSV?*fN7UjFwV3l}NA%f8@Z#CZ>1_B6jp`4#KsJ60#m<bzkA=%aVXGf}>41Vrs66sl<5<
#c3m!73Ve*58mgcAM3gi%WL8GI%cWF*hVhA#1%Ij4xRzhaTH{-GZ%>xhA9=MrQ8s+A3^eYg^Zj&S6udrE}U31l?xn6?%cRmhigtd
V`8E9N`3a;nPVv8C7w0(EMZ-1%`}3Gm}n+yXmM1=fel0{v@xCpE|ka$#b0LbGe%NhhWuN}-gr%d$>?dlfLG?&O2lkYbj&GS!jOC@
gcb=dMpki{DL8K|x*%v#Vt{-k<H}kF4@KK(-{wBV-ym7{dF_e)g+QDY5g~GjJ;`oK%8-M1FJxaolC*i{08u(45{PV`{jFJWZ3xc+
7U7`nf`s-Yd%(FAq?|7iR3uDq6Pl)BI5-<9{`HQ+vh(grY~x!VMhjGB1&sj4<eRWrC@U$IQ85x1;UiCrGp<R3Fn!Oi7~4_``vcBv
c)nOm>sk5iCvt>qYCqAl5w+OvhJ$60@e<N+)}OT2l)`k%t=SNlQzo49WOc-Buf<oS=$_4K<(kAcL+FwfW@}-?Gva5-2f7^gm_(vx
v|L<+k{jY4vRlF(`jW?Ut&i_o<>PY#f->e|ttTjc#pMWMd0s!#ytE$6%yFv6po*{7FvPrDi_7EZ=p?SStL6k^VAC@k9kcSH(ZsTp
WXR77cwtwwHHvus-Xm7>L|cTC?=jLW2*pQ?Ic@>M#In#}Je&1n?dtLpVN#{sIC;eDfrj&;EJ3v4pl0|)dUItdpOub;);_JQh-DG~
vPvt5u8mK%XRRta7%pd7O(1IsoS0{`Az_3y3p}k9cA8KYJ48bmO2_zC#m5}@%c>(ckfgq8=qaK+TL#SwknCZ^taPgN1WgJ)@Hix-
6q5vEZnYjNp&CtqwHci4(RRT#kzFr_*xjb7;%X^F!c)YkR)AyxIdc+J`3KZqSTzy5$}(wW!Im;07=5y@LMG9(+THFAAhS+!Cb^Zy
N=R(|pnCb$)Ai`MNyNsXC9`Rlwi@{*X4y!x>YTuiSnLuZO2FPW>r9>lN_esMW@;1IxGBh$9+QNGu!_rBNXa>o^Q7w)0t!HMwIhV+
&UusCl={|KR>;IH;>F0$L|o_Kjo~FYP3sOecHz}IN+P(j=Z6F4h;0JJx}3$-o}>+ovHl5>Gtf2<7O}M#*)pw4pK4P*WczG<5e5n?
SQ}C9oKg=h8w1NYCAT9qCEjAM$CLbJ!mPnDkqy7K&#N`n;uD(SL>9gcB_1jJ(4u@!V#97u{mV`cyD3KuKCLA2A{=cTX~+=z34u+*
$wDmq%e>hIljSrzT9)vv17SEiC6|JSXJiT9nqbdnOO4DDuX1Y6N%%5Z2_}bBY#lPvIP47YVo}05J#lL&G=ve7<tCNnlaesjQbjDY
l9cC!tFgfg#x-6<g2LHc57&Ru5h16>iz+ulHo(L-ZR~Q2Q#T@E2|;z0bYPy>%>@)vvB3FB&+a}VzL5pdfZ1LmZ{AsldeW`q9^Vx<
<O!7Qk!;sUP%+1Bk9e^)<{9C&d+kS@(cvr!EreI*n0ef@lgU1V&BapK$eD9l)FZ~BP{EMvz_yXoT>*2Y3E5opqO{?p4d)CZo)}JI
M&#s?N9;F(C0_>3Tkky1Hu}D#%RScbo=JG|FbvsdMr_|G(Fe9K!lesdUTN&daGPla!@i9s%p}!EYMZ?@TB>!eLq%&1)kJE$JYuyi
335^|2qo5?@!52Fyv*U(p*Jr<XtzqLa%Pzm#CF>Z365k(UD+tYCSF^=h&5lVWIw3yHasJqNZqO>Tzmjoo#pjGN)AvCod;|wt|gcR
V&P0DI{`HN>>S#fhyn0=vM1X%DDpDA)-Ee8S{C~_!zUR@GRzbs*~T0ZXtt%E&nX2CH*Ic~7qT_koKO<yu66xAffErDx+kK~HoWrW
4Fyyor(@WiZ;ZkYKsKB3C^T748&`0Wp`lRSY6}uM>294JA-6H%^k}ty!43w;QL^A?Y>J(F;r*+u|Jg2K=%YOnVonSim)9YU&l!PO
G;|fHv+HE1JP<#qR+~Z#imyl^F~YRNiJby%0}62<$)mt7+5U?$x9P3ehQ$Hp>m}q>bxO;#Nnr{e4ZEj)P%Cf4^r&3$gw{iO3$&%W
_!{iUO5P-t4UwF(U{Us4Y-;!~?;B2ftm{QOjL5Lv=+W@EWalDNv0B9q>_)8EdOI#F0zokn?q%cVao}c&Df8jiGDr?B=7xAXL}>R1
Q9v2V!b8k!^?}GHJ4GCeXyzQO*+{^6c88zKDL!(XJV}KojkK}&q`cA2$YQ!zB`Up2(~<CbiFo2VVaZ`k$h(Z|B}HQ`iCwk~tK^V%
tt-1v(Lh*j2Z`-oF6${<64RdeP<F(yHa3kknP=DN#FlXsW$dmAiBKdV8Cib^jRa{xM$)<&JP982kqLOagWdEe4u!9`aP%l=p^Xi=
YX3+)aL(NNWG-#KDrE17U9O<gPZC$}5-F(S6R!$TLJ=jh_i>AIETQeDT8{9=OGXXnHzNAjdT)^=<7o9%Q?}8BoSWfYPMVhzafywZ
;5H;5(>_ddc7#M9is1Sl(}G>TT3upxhv>&U)5wJmS&hczCkK)`4EeQ)Sac8PyE)t;rjB`oL-m}cKV;=(gKE~N;uZ12uUJ0D(@37h
cSYm^+4#h%(!g#R;W@D)D@%8pct-nnpaD^byz-!mpCqhzg&}uzq{s129iqo}i6{~smb7egO*gfiO<%d9?sc6)HJ-Sa0)qETg%oOw
2g<uyb+ww2^sJD0y%;q~BH1S%cF5xnn6|{Pk<U7-+D;SLfLerxSC456nxwK4ahEHuCEaJL_aDTo4(e@DEI(oG?IgU6V+2g4M|lf4
r3dVWn5s8qQmctMk>OYQEqc!-vF0g|L6}M+csG-lg$`E12@9szaG`X}PNQ#Q4$pdHLYL6G2@$arXI|K&<9!@nQ`jj}D=$m1HmU7J
wNmf$D<y(k$f*;T(;7PBFoCoauY>q89cJ_4?Y~ataEs>OS+?wy^Nqqcm=4#=X}RhAz4v#=z7<99HO<?r#aH`K{av0x89uVFGs$y&
!~UoCyHznMZ`=4D=IX9JE~eA<QJX5X$BV@($M-YofS|lsZZ6uhMc(!f+iw=_yj+j7RbJ%nX^~A1TTf43y&66{K08i3t<Ik7?y2@(
HuA@Qtm828f*>wT5(H70#oC|5#)WHd97b^v<V9GF;z=^{C%H~WK{U~$EQ<0;G=hH_+<V0+E5`l={^gVLWD>b>72(xnGMeOGG?^5W
F!!<vl;wFcNg{ZR|Mnb(=x9U-NI!M~n>^BiTSVh1Fo=yCje&i}CNq&22Y#Lx6Tl|V5Sti!_ma`5h@hKMlqI8RLU+X&YGDTjATpj9
#AY-Z6^so$%;8xw0a%mK7_bTQ2|QzLG!aJ!UNH&A{@5F3nGT?hiSs=0i`)Qxv>RwokH<lvlOhYv$eqLx59e-D<Uo%si;8>_0)ZyQ
I4Zo!C`%?m6k)%4WPpG)`lKKP8O?C)nP^;$@;skZ{{$mODI05TJkQI=(6bj97|$fk#uIPsg+NxobL@>1FUclx;Ngfvn1QS)qR0a@
3K-zni$+i{%Jd{EM&lSUf`8cY2x*ij#fVCnM#ZFn@nlFNKsayGNYj*gvG!of^w`e>WP&Kjg3S0yI8G+oHNZ+qJj(JU@<st*0_cph
NiZRFLI7!?OXx5IUV=U{9&_O#T0CWpPGianp0X`;9N_LZXCF?6ua8gvnF3q8V;`_G$kr~gwFWXFTf5BGa22>fkPO+H7%9nsBVpRY
FhNvC6JT)oI~wKVpk`~m&DK15xi=!VX5@vfTdjYee0YmTD!Gnwx?bz$GeB`mZ9MOkX?n>j;Ie+l(-W;wZWYN0>5L{kmkL2XeTxND
LWeY=#&r16yI03=PKNK&T?O@AEt{`t+V{qd{KW&W4h%x;9Dwo0_kLeI2ZaF@u^T!T3Od1FI`&e^94@0Rpj;NZRM>2MKrf<WJ-Whb
kqUj=7HugN`rxPDYmDQTeto<T>XrvoAtsD}*aqLp3Y{7SLLb95dOiN_^XI20XGr4%2oU0gP_C}<o!hsso@ttcP*5cR2N6NQr^dF{
noiL|gU43~+V$w#X&pa*E;EB~9Ctf-48fh^-Wz8Sbg(ytKvhS2as?4W_ucUa<f*-EeLf5~$4{nrH#eVN{xj2`!js?Qs}C>B_wzle
H9UQB3^k*X>xLO<slf9KKP<c;)Bb1_m>?LrNfu1pM1$n%Ffv(g!Z?b@BRBW+FbCa{_<Pk!8J!z^$2n6YHCDMQ)Fi#B53T8BSO!GS
;rRr9;kg>ixi}l(>2>26odzK?sWQ8H;8-9$Zf6ChY%=Nfc&R;m;Mk#Nn=!W;+f#zNBj-Mpyx1U8Eqeq&=A@~%F!7ilI(MM)(Cj?y
;sHQ>YLJV+e2<Onc|m-95cO8hZ@4!)!vrpm<N%Jm)t;x^Mb)r5B4qV$w^Qz4I^DcFK28o!>aPa<@t_{8ypK+YWsU!qmW@$2AFcid
YRGw%?`op?eN8l%8CqO#iq&_?e%n03X~aNon=|(C=~7s_Qft9dt?!@eG+U258@0<jRJgi7rC+YIe3fm=ac8EQz42jEz+|%u@N!ko
$K^7c-eb)BL@x0Zj$K+^-KW)+_5Jw77)^%-N_RQWzD#<SrdBFi?VGfTjO7b_^Z&;A*{zu3rX?q6Wz%dm<l_oDOFH~y3;$Vm+vyay
7G-`rf6Z_3-^vU8jsj5G^>mZE51AwC=o*ju<0HkE_s@F3(?h=5!-rJ1b1;BC@rO<_*geAG${yjsrxx&$3qXa;9<8v23?HmO=QpH`
1&r+IrknEV3UH$?;Ez2{0WJ^tzCKg|ZsjD5{>32012OOnx{LbEKcQdWK9b|<Y9x1uFt<aPH&3A$SV=Ed>w-x)q@zAzn$&1~pNM6C
`|v3j55sqk%G>nYRZq_9;3Gro!z=)rJq~KTn5yOWQ|1)lygo!9eW);Kh9aY}J!9ok&9@uY=(gJ<I#i=^00#8Q6Lgaz$*S{A8mDH^
Q8xB~jCQu+5f{Md8+ejlarw=DDw>X_@Ji0ip!tOx5W-tIUnko*145!bvd3J=p&A9v`wd}{rK9?gBM`SAa5KwQF&{4=c<S7WN!U7`
@_Bs@-DU+<S`Qy!X)E>nG{!4OVf7nluyuqVpAU4~I7Va8dic~#3-23(xpI0I$D6G)0dK3rBkzM@9i|W+r$%oF4nrC2o(PC%#BSEZ
^I|b8Hmf^6<!e37##eZ@$`Mwji+MIH*2BhSeXh`?RFiFPdVWfrFi-gmJwASFB4?6K=u9$Y3r(ZY9?N)n|1_Q@AFzl@eqOb8sqG~n
{6%N!P|HbASOU-0S>lO|Z90{y$K$dLwRG&Ls<U%oD3=u$jWZRu4{5EAhZ%Ek_CzAOWeeCiVW{0EBHBJ0!)Q{+9?m6W8_TUDLu(7s
o0yWD=Ik6;HO)o^sD-tn1{@9S%@=dDJ$W(T>?tOKlA(hew};2N;OWJ99Lt^}Y~}HW^)|>*de0;sjTW~Qr&#Y5LzJV@IBgsugy#p{
q6jt)Bg>}K&dtxMyRDgO9)+Tv+S&ZBgZiu-{JhiZo^?haYsn`Y{ZL0&NHtDQqJwL%%6XnL5s3sT{S_?&UfsEBoOQHL0a)W;Li^7i
pG-#t-TeH+p{n1D)q*RgKPCzeN~l7oS<yU#%Nm63Y@SmY%^eg)eyd$f(r-mi&hnC@1ONCFiTyF#7n6riKeGg!lr@GpZ-~(q`qT|a
U~+hqO|J_&*R(#KZbo4&)K`EAwD5cyl6DVtw4VTk=0R1enAjsxF^e{2Mc=^#r*RNqz8Xw9fUud5l2W5`vtuo#Mf)<%|KS~p`+=Uv
tjyESbg_R?I**|5HWp%mf(PVW1FSUNbNA#lV<^U>r*@pQQ5Ay>N7<?<*K76<0Yfq!9J;Tz!j{3&G+S>{#QkV}ZjX1};qZ|?QV}sh
&$S!??~oq4Oy|YzrgOQgN6URajS+(+YITXNK#1Y5qT%5mg}2!6!TKDaEz6t5CY2uU>*fZ`N+n)B{FwT?0vZy?uG}678eQt*YT!J=
!T-1;X_A7^+$K^H#ESCka{zV#AsYNIzVv2Qtk=WFvFV*-#P=+fWAcs~LUjhr=Z89QE0OxP>3b|g#64$!NR1ZszD)alWHmem?%^Zz
8mIZ4JnKOVrsaOBkMQOagARK`5y(OPq{N#_NSa*KU-j|$@0x9}1(pmd<Qikb%r>eC4<unVt1LyGpQf`ro0<i@W9xo?t+Y={0qlM4
>^@G*$0D#_Mb|aj;X%qXt0A_}p=$td(RuOUUMxADQ8Rp0Ww!@gx&re)rrRZ5zjZtrg1`WOOAE0R0M62Cv;JCcE;?U!o6zl-`WED4
`M2~79VAU^zY{1QqP(MJg&@U3$2FX+f#I&9OjEvYwa3Vd*({Y4^AFb-nF&JRz}fd6tcvksm6O{AB%C7q;?a4jdo-FZ&_{ER#tSra
)wJRe6rKTi!GT~!L!4wZ*$-&V?^$hfoc{wuD)qp>NT*|%VVC}?F3i-8a|p$Y8Lnuc<-ubRca7VK%{3s=@0asU=cWry8eZ#Y&}@f_
NC<g&z06UbX%zc=y}f<(p|SD)-v6ENIfv{6cPf{TKtM;mT>yJ(@9=T~gGZeV&(N?v0ONXH<Y~WrNGFq&@tODYO-CjG(~>{`T>h5^
rMk)FxI&gbYL4(ob%GG22%*0M{rh#Z*kn`k3BK-1%F+6woNQ9Af^>THNXXry2>R<feY2Ps)zO)Dz!Jap4+tvg$go@PUk!G_A9M&l
4&&;v$JWhtb~StGaBK$lzmX|C%1xSeN27zhn;+#KU3bU(rki(*?&KirPT(&T72V=s423zvs52p%%8klB=Vw>ZjH*>B&hPas%}uwH
b;k$L8n6Ul&`klMq-jEdivP&ajY4GvH;*2{UG7np*`H1M4Nf`m(7gv0Vh{2Jko5-B!%ztr54;YnTg(A7y7BnNle#oRH#d}WgiBoG
!}(%LOKu0czEyY5?lI_CU)=zfBK!NO=-O>!tST;8l?v<O(W?!8!Bv4s<@p>>%B}gZJ}q>ascXC=D@XitzF6e!PBb_kSr)O!s{gf`
k?TP}WJd+QMF$}?&mqR7XjRF1oMHh2BrCzHZp#}-E=Y+LSY4&8a4LNQnsu(gp)B*^3JHs_z(<>xv+LQAIJwA&RpM<3Pw@0{q8QBw
>(1(=%^J1Zf;6>ms-qw#-V*Jb8to<_h~5|)t%~6+-8#9LS9hGF|5$A_7QAZJ0nnGV)!xz@|FPO=HHF_I%TCvQ74W>npp<8v|40*z
mree=QOmr;iwP97NOwf*wEsPR+CVhF%}))dYp~_e5XV4}5P<B1g(vFPJ_{$pnVA|C@9))ovNx!lKHHuE>`qJV&=WV-K_L7nIq8%c
59=#h$4{ke5-Q+6ax&91g}+0r(ey;QF>@gWl3WXTeM5en1yYx|R3w1d@&{e^T-6q@Hg5=YBW@iE`|=OC)>&T8&#icPT`6C~Nai_s
GMi$B0tXGr_*V^g!Lo)OviFi&8w++YFV71IcpPPAlDgWdKYO4)DLArtvM`DN93?DOKLJj)g$?ooX_vNG=)X()25-{Nj1xMeSiabF
aXp>3v+EoJ#|(F7K;6Z3eb~m2I!T7-dM2ES-zoxSzAo?_@l7$kvma^#_RdBC|B#{)1UUp=TXPN)Q#Z(YP8BL}!uNqgx^a?k9Y=Zh
a%;E@pl(rQ6yILSt#fpda;k}LIbfWpDK26+Q&ekkOt{{ib8yl4Oviwm;A+Eq4R)DyAKE9ld%Sgyb_vRPvReFJ%<1z-EW5neQwQA8
3c-Qibe-*x1COJA%p*LaluVve+5H2mC)vF7nLljviPF(WztVV)&Qe@QqR5|C<((sz$3IO|{>fJhD9wf+E@&<fJ@DZItefBP#|t|A
)szKK$jDxd;lgnqh1Iek=D{et3GN1Xhn<Ba^^Vr|lTx6tm)om6RQ16H9r;|s&DQr4ZXWpx-GNQYt9u~Uj`a>30DGI1*6%iot1WR$
0oFU?@-sDKXvS3=M`+v3M&750%5Szm$e_+xMN0PO;%*I+i2888zFv2JQ}0zVQLmBeU_f3wM{iPGP<>smmd!e^)f>?KG`~=5nST4@
=*t)UyUfN{)l^erN&&fZN0LsBC9CDK503|Fy^i=={npP0G(*2(BK9}RydFWtk;--}j%>wjKzBr?FJJo5S+nXJ^&XSBSoM8BAJ84Z
go?Qu?^euh#qogd2quoGBCsH>1ScgODuIU$K0e@KXqN<zQm&8P25tC|?`8A5OW-M&$i=4*z)5}t=F69dz`RKNbi6lZAK^mXR4czH
&lC>Mv8v?;l?k2co?ZQ=R-i|CRRv>wY~5?9lv8IPe?B?~`18VPW)aDpzfOUh(l@*2uU@Bp?WoiARDDc8su$@Cg&pw6B2v60+l0wm
vCdm5Tt*x5t;1MASOM@ErG}v&c&O0f%mAe#?J&-YaaN48{T>h5pdm@Bd=5iB!>qmfmHrkJ{yN6?KBVTtPv+EVi~HZuaE>PHw6;v2
Yxft*({Ht2pKN`|4ztNw$_n{&-vg&=GOBLf+Q*t?{hkMI-DHHnEmj37mmcBDLPtM>GUw>GO6%dyne*m{J8G1|?x!@R(c3SBkW~UG
#s?s&z*tsKD@{klLQ6X)EPqpIH)<@$fODFDB4}`<2W%)oBFghw#%gdT$bz>u<8OShx;zJLomx>zEr4P$B}V{`K&jCMVDKIjI;-q!
ZJg?l==}9nv&zcb64Xdc*3QKNKLYgB+&Ox0HOdzU`>*s1eXQV5>|`USMhjT)`;!tJ4NSOk07I)`k`ZrKc&zQWVQ#kp|Au}3)c$~e
COCiBV}efK2A~fKtiS^$$La=MDTt`r^mRx4LghM}743OBufDFyo?MRKC@9v4I1~sNw|uMbe*Pq}PE{tn^M30iMeK)IH6uHU8m`Y>
I=kuc)*r<?)Eo%+xdjpnN$~|dtH-IXGmY<^9$`qH&Rs*`2yMdqx4N{J&G*ihKuVtfff=i3#CgCffasntraAcufc^3F=fEL$uiDXt
o9Y964txfVLx(Qi!J`XT(WS;qOpj)pER{eVWDVm4)N7=l?34|W%|BPS>2K<WJ~o<uV$Xb0<|!_!-DIm0*RxqzP`UEbbo%^MvC;(t
fEPn4=N$%(^&~}8pT1Yn<8Xbw#IJusIF@}yVAy|g3vK5^R9T>{RHJBwx(SM4aKj0XWLV<{WdwOhpKcv)(v6I~zgM|1w6t1o?!=eb
8>HXyZrC&3ie~=|RDbUy#H&9ytrxUt$%i{%qL=^)dic%6^>ndW4~J=IZ@So1dl%)N^Uyavd7%r_PEL=$H8@>>Cp}$&+lhDZOiGc5
F3Rm3)$`6pSt&ZH_c)b?t@i)H<VraPUbtA~-1!uOv`+oO#Kq43g@v+XkZ*(9+s4-~ANUd|cg>)W1a#F>@Y-L%A0@cK4K30Ag^zhw
@D2oqIuOYJ$rn7E82<P(p3Rzn`Yq3`fkVt77<KEh(hVRhNOzl5peOeUMll`OGz|2dzx4gh`#1@2EG!<ly{+B+OlQ@renfcUPlKeZ
AAaQ1cJqkHRDTuHY;8S!;A@Xmb-Ey#yvSxFu-Y3$|KdWlz9v(-gz%<z8Dz(`L%~M1FHt|bu%GN)stfC&N?mn9rnD#;&J4KiC4@xi
zT3oBLm&J2-PG)kR(aOz-S2gE=wozV^<iQn`3gUn)%C0GT;=XAu{D1Bwj88Fo1*ALS-*3+ubqE*;5^g?h6*SH3pi|ls%*ty>e?x-
LsRUcOQYj&m=&B-+~<-jTXI={*=%dnyP>yn?!~qAP0IE(n+Y`$N8E{94j!3(y3vCzYh3|HFRO{~!CD#uI*$zA>A}OhKF$4IpN0~d
i}_7)D?o*?GP}4$?ffIKGpwZe(iYqU7~C6a;P3_}`50ISLTU!On})ndFM$0xW3XI`aV!c&EQEjXYRJpp@MOJKK)z9)4O944@4-Ow
K)}ePd?itah{e`Y`7>~-f#EJMQ~JylI0`VWIM=^EKsaE|eZTvx%YKB-EnhV&0B>KUQ0L(C5}gZ>s{Vz7Yj?2EuR6G{)4fm!RD=&S
KEOTwRBp3?aD6}z2d#&8CoOlEG?xlrtDsFkM-MJ%E^#@ts?%6?KTp$+uY6^kYD>Uqj9YAiDj9b3y=6_*d?Q@8z->|oGCJONTD_`J
y=p=4Ra7~vqc^DzMGssycc(HT-#BVjEQ@TD8qx=&k+3E1TCtmA%SRC0*0;n?kKQoj*^i}_R(m0ys^r~o<8(()66i{8cbn1V2*3LL
J{|Y>-tR$7gBQqyd!)+vrsBmtOp={nXSkwG?i)P60Ow}k-c*c<h5Z%FYvXgFtO*DBNZ)&8=#d2_JikYpjr(lxr|tfG-q#Pb?^KsS
oA<KKUpoiyWvBmp-s!J=m)1?TU=Fr{uBD0m9<1f%fi*)VG)bAS*VvL40hy>b;$}4*qMKcZXgieWZg=vhwC0CPA{A3o39h7;m#Vto
&D+7V(MT2yTlc2Dem$kJS*u9~5Dk1&R^j(<sbl5>DDKc}(fIa}r+j}`gRv)#n-NIj(CfDT_E2mXW@0WcmEB1<yr9p+)lbt4^y;ft
z&I$-_FIFb7^{a*tR5IPxAEP3Dx3Mp*9U34#Ml#h#t+tk%uS1wMMUOic)o(@;7xtcl1qOZm6+MRp!=r#2BF)<$?Y0xtwv}QDM6{H
oYDwtu`16Ya-9x&mMHidgX)$y1}?5wL%T#lL4~A+ermtPD0wo$V0o4;aW&$4LqRkJ+LjQCEKi2x&sMmARv?Py{2YSm-%^fJY!nC5
P2nS#-jAB#`NdWUDM3ynj6z-TDxHZpRlVBP)Q_@<&lcbcq1xa_4CQ4h+`~1Sb@(NVSB?VXgx`OaRrH(AnSHN_(hk3&nyQ|0BaGV5
0JdxiqR6~Pbxq1c`2OFN9g+_M6SHG%{{@DZZpHQeUNE3FjLMG#j@+ou3pLsKF6E2oq`H5hEcXlNXp>#1{aXOIkACPx-S&HC&=|nK
2S+zI{B_$e_z2Vc*gpVnp#OegzYke2@^^4sv+7)_=>z%j=BCe%)C7l8_VjIkYO>SWd$&h#-6+J7zFmu$06~8tpXcBG5trCU_*Nba
4DPxe{2dJr_*OPHZ*`6cs?JnheXsNP()oLYZU(5fM|g1{1&r3s4JPLSrx%11+>RjHziI5J&hzx!RdLs&n1P*?;!X)3)T#Y4=$22(
>p|if<f!XZsnD?}-f+MBR1Y4zq~y~SnSr(XZWRiX>IEixu?RG4<n$Uaf%>kxl>Uedo2A$f?Fv|cYbcv^za5MoWe*OK@>2u@tNiT#
v13yR3>X#C<#;{=zF67E0SqcD!*zZZ56yLX8`u;yQ(bg)mC{^H@Zp>BmQ(&hJa8n=V?$ss;g<+>aD^6Lp4bwuTh*byL|(4`)0b}B
?bl-xx;JCz==HqTA(+*jbzYCv8CuHm14*1M<v`0-^9I$%VE?L&KG{JaoAn$~yJCfU8DWp<h=uh!!d^AAF3r@K@;}hWPq^Q(ye;xJ
c7Y4h*r?qBHMIB&Y8vKpzL;B-+f!O-fMTpA3X8Npfw~5fT7fRgDUPU?w#h1dy@26Wd)V6-*>rNS010ewvU1wChU?I-obGUyeb1}Q
Q!}Dn%s6Mb51waHHw0yU-o24^W!$>^vy8nn`WsxKZulFo75~)!1jcA`CyC$c>)jZ%U{V^|R70;9S@@H~(>p|VbVqypztI+desi#M
Em+<-kLZGSyI`#pWQwt^s<0-l8mntw{o2+R^ex*?L*MS`{95(0GAVAC^gZ0P!|0JLL+gQR+=Di*??Gh%+^u_1m;<Ll(+X&c+*4Cy
4_szMaPYu;4=C2ygp3ugc1_ZWqLB}?jrA*1Do{l7;hXf$SnWs%bV$o$z>~u;9<tLh+<IezZfd`7v;uLEV3w2#zD)%P4UI9ClO!+P
Q}6e7<>2_(X$7Qc>(y;~COB4E=YLCqO%cPu$0fLHKnCkUjjl`ZV<4&mz1eBJ#yJG9addr-Ik3+P!eMosRvWx(_uyH|FDN|+ZRvS#
sFEo3Aap+fJ%}gf_yGhNRO1_jx%hs5551T_oP8-Y<XA}IL8E3>NU&Tyc*fTNO{%zHB`RPQIy-1Iu-F39+$+7)<gwRk<6B{%<kI^u
iM42VOZwp6dU$q`elM4R8@+LTAno&BHwoBmbbIgE1Br4y$-j`6O8Z;up)@JQWNTM9b|LOp#!|{nQRp_C^qwzzR1v|3>5n()Z$4&q
RK@C83Rbp?*dGd(H(RgwN{HLoJF^u?lGU$6D~O&rbd>tI+Qh{c0<9=PDXy8<apk>0o2*iQkM!Sg3qde2;}#&2=Md6Zy3iZ#71sFZ
VYfb|gAjCxM{eja2;&3~Ix<EZ9Va^W;y4QAScD)9BhS}~iByp2DD+M2`*<b|dG(1lu{K^5M0j|QA3{yfBuNywPBZ(m!HkpBwJ7n@
5uyPgj2DJsfahA7$a4cX44@^&LFrC3#LbaMw%!atx8WAoC;i&Vu6n8>9b7&HB0@l_@)Dxb+V-#&?{w`p&&I4vi+XViF~(DkFf+Vd
H@zci6?dV0-{9YF*F5G5e!QdX?CKEMC+PI}m$z?*CpsFQz4&l)GJN{+Y<T?Y)$sJ)v*AZG{G|63NCIy6<<lbM&hEFXkC32Hx;l4g
2%buj?tR7p52)Y$ywCZ(qphV@U<X_nqFs<^+Aw}BfNHYKxXAYqs#t){Vkns4N+UU2Q(A&;JmF5%6E}V0swXCWV(bcCGp_%PP}k+{
kXfPeEPbXnUjfkFWC3$OfvEy>u)y8CTL6Al*=n`;DwbmF5zzr-;$gMmXunr4CC49By(($dVN=JYq%w(|v_8DJUJvgp$rP{Ec)D2Q
2GI-LnaG-mvIDiKf)*tr64@(uu7p-)OR~M7Ji(j8rKt7Y8oZ0TCdmPUXfo}3OkHKG^K#DHDowSoa<KxETARLGGs44PY*m|m`9Xc*
V1?cQ@}wOHuhb9GlN$o>EH8$e>rsKrawWJBAOJKESX97Nt@u@ybX!1(4aP9;bnjo}uabv~2}0+;y^2w<ar4QnoZhuTF4}-Y`{U24
IpSp?awQK40qX6D6Cl$m?h%0CgtiEf4+=#fWrur?Jtzevym6?=8kbF0=QqyZQiJvFJ!bxFHh+)Yi#@eR`Q|-d#K}r<Fi&aDPHxLh
XYb=WJ1=_e<=y6DF>fC{X&;=nVO*OGU(dZZhs!&5Q~pPwfO1H;{gxw23w18ni}_)GJzK6j_C4^Gqc9{Kg2TQ}&w$GnI)ih}An&}@
(89N^v&}_kuh}<(+~b$x8v_JSnMc-J9)4YcZ#x{_Z3<36p{~Q%u0_Kw55d>V<vG3;h0EA<MhA@i`03fl<5!}{UcPyD0{RWt%2BDE
4$nS(JRwE*>iF#J<x{wRbN2GX$?z@If*MawhVPC~PZ2u-_x$B2(1)+yo}N4#;u}z>!@%<Z?%ByNCm)8Vpsr6(PfmxteIHcd%jaiM
6L|E=tG7@8dAbV@wJPnt9)5WHmTG=@`5Ms$Y)^+LpH4n}X01CsJ{!I|IX*obp8f0XE|h=0c>4;ldJBl_;ag}F4A0&UJ-XEH@b$|#
1oZjaj~|A|AMoI~r!S6QKLLbyNB0r%d3|#B;pNkz5Dsn7$p^p;)cL!U;Th88!|}71A5Wz(lJR?hsH=A`p8|w;AAp)bn~zUUKcAkR
ygo%xAKoFcUOqh|fBf|63#fl~{PNX33cYzd{HS4UZ=m|er)Mw0FhS9Wlcz5ME`t9AK;8nGp!AnlZ=WE_Z$IMvzBqpK%SjDsd5CXZ
E4wqoQ9JL%QDJkBc#Xr;w<ph^zkK>qtQyqbQ!83j_`WK}{T1Kc!cN9tfLk7cS$g~7FM<ETo_Fk^q|FDY3x^;~!y#&y;c&0VTBh~?
0L51Zlm
"""

def main():
    if len(sys.argv)!=2:
        raise SystemExit('Usage: python -B -S recover_pentagon_u2.py fresh')
    data=zlib.decompress(base64.b85decode(''.join(DATA.split())))
    assert len(data)==39189
    assert hashlib.sha256(data).hexdigest()=='5a8a2e139b587623fe2496648055de6b4b50bc166f401b5b6a7c5699e1e654c3'
    folder=Path(sys.argv[1]);folder.mkdir(parents=True,exist_ok=True)
    target=folder/'pentagon_u2.py'
    if target.exists() and target.read_bytes()!=data:
        raise SystemExit('Refusing to overwrite different source bytes')
    target.write_bytes(data)
    print('PENTAGON_U2_EXACT_SOURCE_RECOVERED',len(data),hashlib.sha256(data).hexdigest())

if __name__=='__main__':main()
```

Optional convenience copies: decoded source (`pentagon_u2.py`), exact reconstruction report (`pentagon_u2.json`), source-only recovery capsule (`recover_pentagon_u2.py`). The embedded capsule is sufficient without these links.
