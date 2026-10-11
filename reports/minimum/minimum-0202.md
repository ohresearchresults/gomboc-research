# minimum-0202

Historical AI scientific report · saved 2026-09-23 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# UNEQUAL_PENTAGON_E17_GLOBAL_U2_V1

## 1. New global result and exact coverage

**All six edge fractions can be genuinely independent while the complete primal U1 cone remains empty.** For the actual seven-parameter construction below,

```
0 < a,d,eta < 1,
1/5 <= b,c,e,f <= 3/10,
```

every uniformly filled member, centred at its OWN volume centroid, has **at least two STRICT unstable vertices for EVERY SPD metric**, including all finite mechanical weak-arrow walls. The three fractions at the first simple cut are `(a,b,c)`; those at the second are `(d,e,f)`. No equality within either triple is imposed. The final nongeneric cut has independent fraction eta.

This is a complete seven-dimensional cylinder with unrestricted apex-directed cut fractions and final cut, not a small perturbation of the moderate body. For example, b/a and e/d can be arbitrarily large. It uses neither apical instability, S1, a selected complementary tree, a polar-arrow hypothesis, nor a condition-number bound.

The main certificate has **903 integer stress rows, 1,473 row/cell applications, 8,835,901 shifted SPD Bernstein matrices, and 26,507,703 positive leading minors**, with a second fraction-free determinant calculation for each matrix. It covers all **46,150 rooted TRUE-edge trees** in each of four closed parameter cells.

Two additional results clarify the boundary. First, the ENTIRE independent-cut cube `(0,1)^7` has the same true10/17/9 lattice and explicit coupled actual moments, and obeys a uniform three-arrow routing obstruction. Its full U1 cone is **not** claimed empty outside the displayed cylinder. Second, the whole closed core `[1/5,3/10]^7` remains in the genuine minimal-four-arrow polar chamber: every proper three-arrow subsystem is strictly feasible, but all four weak arrows are impossible.

A new unequal actual control inside the cylinder has **no unstable vertex on the heptagonal base**. It has strict424, weak000 under a small rational metric, and strict222, weak000 under an exact unbounded metric tail. Its only U are the apex0 and the off-base vertex7. Thus the global obstruction cannot be reduced to an inherited permanent basal U.

The union of this cylinder with the parent's previously closed tied-fraction cube is a strict enlargement of the accepted excluded set. The cylinder alone does not contain all of that old cube. **No whole-incidence exclusion, complete-U1 witness,110 construction, canonical count subtraction or new minimum bound is claimed. The interval remains34<=C_min<=622.** The notebook explicitly distinguishes actual controls and family exclusions from attaining the mechanical minimum. :contentReference[oaicite:0]{index=0}

## 2. Evidence and source authority

The complete updated journal, including its literal parent payload, was read through EOF. Delivered journal: `research-journal(20260923-064747).md`, **298756 bytes**, SHA-256 `7edf842a434301421766dc91520ab64763e72428056b6ce7e385b828314d2686`. It has1591 raw logical lines; Files rendered1603. This is the delivered-file hash, not its internal working-memory hash.

The authoritative parent is **minimum-0199**, SHA-256 `818ef0f09b76ed0128685b8ca263e1898784ba9fdb4a78881206817ae46020d0`, PENTAGON_E17_THREE_CUT_ALL_SPD_U2_V1. Its complete mounted39189-byte `pentagon_u2.py`, SHA-256 `5a8a2e139b587623fe2496648055de6b4b50bc166f401b5b6a7c5699e1e654c3`, was read for the actual chart, stress inputs and audit routines. No generic replay of the accepted parent theorem was undertaken or needed. There is no source conflict or missing exact dependency. :contentReference[oaicite:1]{index=1}

The new generator is autonomous: no old source, report, array, catalogue, research connector or external mathematical source is required. Earlier unchanged local-realization and Schur results are not reopened. Their literal moderate-cut apex0 identity is retained throughout, not replaced by the coordinator's different apex4 construction.

## 3. The entire unequal construction and its true incidence

### Exact seven-parameter chart

Use the fixed raw affine frame

```
A=Y0=(0,0,1),  Y1=(1,0,0),  Y2=(0,1,0),  Y3=O=(0,0,0),
B0=(45/92,-113/345,0),
B2=(135/283,1808/1415,0).
```

For `(a,b,c,d,e,f,eta) in (0,1)^7`, set

```
Cplus=(1-c)B0+cY1,
Y4=(1-a)B0+aA,
Y5=(1-b)B0,
Y6=(1-eta)Cplus+eta Y5,
Y7=(1-d)B2+dA,
Y8=(1-e)B2+eY1,
Y9=(1-f)B2+fY2.
```

These are the COMPLETE literal vertex inputs. Define P as their convex hull, refill it uniformly, compute g=integral(Y)/Vol(P), and only then set Xi=Yi-g.

The original pyramid has base cycle `(B0,Y1,B2,Y2,O)` and apex A. The first two operations are independent simple-vertex truncations at B0 and B2, using their three incident original edges. The last cut passes through the two existing vertices Y4,Y1 and the new point Y6, removing Cplus. It is this through-two-vertices cut—not a generic third truncation—that keeps V=10 and gives E=17,F=9.

The parameterization is injective in the fixed labelled affine frame. The apex-edge heights recover a,d; Y5,Y8,Y9 recover b,e,f. Writing `Y6=alpha B0+beta Y1` gives

`eta=(1-alpha-beta)/b`, `c=beta/(1-eta)`.

Thus no four extra coordinates are fictitious mass variables or relabelled affine freedoms. The four fixed vertices form an affine frame.

### Complete maximal facets and true edges

For EVERY point of the whole open seven-cube, the outward maximal-facet cycles are

```
F0=(0,3,5,4)       F1=(0,4,1)       F2=(0,1,8,7)
F3=(0,7,9,2)       F4=(0,2,3)       F5=(1,6,5,3,2,9,8)
F6=(4,5,6)         F7=(7,8,9)       F8=(1,4,6).
```

The complete lexicographic true-edge list is

```
01,02,03,04,07,14,16,18,23,29,35,45,46,56,78,79,89.
```

The degree sequence is `(5,4,3,3,4,3,3,3,3,3)`. In particular F5 is a true heptagon, and the polar face at vertex0 is the ENTIRE pentagon of poles0,1,2,3,4. Its four selected consecutive arrows correspond to true primal edges04,01,07,02; the closing polar edge corresponds to03.

There is an exact full-domain incidence certificate, not an inference from small cuts or sampled hulls. For each face use the polynomial normal from its first three vertices. Every incident support equality is a polynomial identity. The56 nonincident support slacks, four nontriangular-face normal-component guards, and59 projected within-face convexity determinants are positive throughout the open cube. Their119 separate tensor Bernstein certificates contain **297 positive and693 zero coefficients, no negative coefficient**, with a nonzero positive coefficient in every guard. The source verifies the full inverse power reconstruction.

Every Bernstein basis function is positive in the open cube; hence the guards are strict there. For a triangular face, a strict nonincident support slack already proves its normal nonzero. For each nontriangle, the certified normal component fixes the projection orientation and the59 determinants make the entire polygon strictly convex. Each displayed edge has exactly its two actual adjacent facets. These exposed facet polygons form a closed connected boundary; no unlisted maximal facet can be inserted. The resulting body is genuinely10/17/9 throughout.

The construction also has a direct geometric interpretation. In the B0 corner-tetrahedron coordinates

`Y=B0+u(A-B0)+v(O-B0)+w(Y1-B0)`,

the first cut retains `u/a+v/b+w/c>=1`. The final plane has equation

`u/a + [(1-(1-eta)c)/(eta b)]v+w=1`.

It contains Y4,Y1,Y6, retains Y5, and has strict separation from A,O and the other retained pyramid vertices. The exact polynomial certificate supplies the complete all-fraction verification, including combinations for which a small-cut argument alone would not suffice.

The walls where a fraction is0 or1 are algebraic certificate limits, often with merged vertices or facets. They are NOT asserted to retain the E17 lattice. This is separate from finite mechanical weak-sign walls, which are included in the U2 theorem.

## 4. Actual volume and first moment: three coupled tetrahedral removals

Let

```
k0=113/345,
k2=1068/1415,
D0=1+k0+k2=203306/97635,
D=6Vol(P),  J=24 integral_P Y dV.
```

The three disjoint removed tetrahedra have SIX-volumes

```
R0=k0 a b c,
R1=k0 a b eta(1-c),
R2=k2 d e f.
```

Their vertices are respectively

```
(B0,Y4,Y5,Cplus),
(Cplus,Y4,Y1,Y6),
(B2,Y7,Y8,Y9).
```

In particular the first removal and final cut are coupled through the SAME a,b,c,eta. They cannot be replaced by independently chosen positive masses.

With

```
J0=(A+Y1+Y2+O)
   +k0(A+Y1+O+B0)
   +k2(A+Y1+Y2+B2),
```

the exact formulas are

```
D=D0-R0-R1-R2,
J=J0-R0(B0+Y4+Y5+Cplus)
     -R1(Cplus+Y4+Y1+Y6)
     -R2(B2+Y7+Y8+Y9),
g=J/(4D).
```

The autonomous source independently integrates the displayed actual oriented boundary fan and verifies these as complete seven-variable polynomial identities. It does not accept the moments as fitted completion data.

Since `R0+R1=k0 ab[c+eta(1-c)]<k0` and `R2<k2`,

**`1<D<D0<3`**

throughout the physical seven-cube. The true core tetrahedron `(O,Y1,Y2,A)` is retained. Each finite control is additionally checked with two distinct positive apex fans, actual covariance, and a new zero-first-moment fan after subtracting g.

The relationship to the parent's older raw coordinates is the SINGLE fixed affine map `Yold=C Y+o`, with

```
o=(-48/89,-48/89,1),
C=[(16/25,0,-7/25)-o,
   (-48/113,24/113,-103/113)-o,
   (0,0,1)-o]
```

as columns; `det C=55296/50285>0`. Setting a=b=c=r and d=e=f=s recovers exactly the parent family. The actual centroids obey `gold=Cg+o`; there is no independent polar centre.

## 5. Complete all-metric exclusion on the seven-dimensional cylinder

### Positive edge normalizations

For a lexicographically oriented true edge i<j write `Yj-Yi=fij eij`. The only nonunit factors are

```
f04=1-a, f07=1-d, f18=1-e,
f29=1-f, f35=1-b, f56=1-eta.
```

Their corresponding directions are

```
e04=B0-A,  e07=B2-A,  e18=B2-Y1,
e29=B2-Y2, e35=B0,
e56=(b-c)B0+cY1.
```

Every other direction is the actual full edge difference. Reverse the direction for the opposite arrow. All factors are strictly positive at every physical parameter under consideration; the source checks each polynomial factorization exactly.

Put

`Zi=4D Yi-J=4D Xi`,

`Aij=sym(Zi eij^T)`, where `sym(uv^T)=(uv^T+vu^T)/2`.

For the SAME physical M,

**`Aij:M=(4D/fij)Dij`, `Dij=Xi^T M(Xj-Xi)`.**

These34 genuine primal arrow tensors have degree at most three in each of the seven parameters. This normalization is part of the certificate; transplanting a weight row after dropping its factors would be incorrect.

### Frozen integer stresses and full continuous coverage

Each of903 rows assigns positive integer weights mu to a set of directed true edges. Set

`Brow=-sum mu_ij Aij`, `wrow=sum mu_ij`.

There are4482 nonzero weight terms, largest weight1808. The row-size distribution is

```
3 arrows:81; 4:222; 5:320; 6:214; 7:61; 8:5.
```

No minimality or optimality of this count is claimed. These are noncoplanar GLOBAL primal systems, not the separate local five-support theorem.

On each listed row/cell application the exact certificate proves

**`Brow-(wrow/2000000)I3 > 0`.**

The four CLOSED cells split only a,d at1/2. All retain `b,c,e,f in[1/5,3/10]` and `eta in[0,1]`:

| Cell | a interval | d interval | Row applications | Shifted SPD matrices |
|---|---|---|---:|---:|
|00|[0,1/2]|[0,1/2]|388|2,249,046|
|01|[0,1/2]|[1/2,1]|370|2,228,848|
|10|[1/2,1]|[0,1/2]|361|2,126,917|
|11|[1/2,1]|[1/2,1]|354|2,231,090|
|Total|||1,473|8,835,901|

Initially each arrow field is represented in tensor degree `(3,3,3,3,3,3,3)`. The common integer clearing denominator on every cell is

`2084324490584604288000000000000000`.

The code reconstructs all original power coefficients by the exact inverse transforms. Each application then uses its frozen subset of valid quadratic degree reductions. For a cubic Bernstein coefficient line `(b0,b1,b2,b3)`, reduction is allowed only after checking

`b3-3b2+3b1-b0=0`.

The reduced quadratic line is `(b0,(3b1-b0)/2,b3)`. The integer implementation doubles the denominator and uses `(2b0,3b1-b0,2b3)`. Thus this is an exact representation change, not discarded coefficients or a lower-degree approximation. The chosen degree in every axis is2 or3 and is part of the complete capsule.

After subtracting the scalar shift from every coefficient matrix, all three leading principal minors are strictly positive. In symmetric six-entry order `(a,b,c,d,e,f)=(00,11,22,01,02,12)`, they are

```
a,
ab-d^2,
abc+2def-af^2-be^2-cd^2.
```

The last is also evaluated by the fraction-free formula

`[(ab-d^2)(ac-e^2)-(af-de)^2]/a`,

with exact divisibility and equality checked. This gives **26,507,703 positive leading minors and8,835,901 second determinant calculations**. The Bernstein basis is a nonnegative partition of unity on each entire closed cell, so a convex combination of the certified SPD matrices proves the displayed field inequality everywhere, including shared parameter walls.

All NumPy proof arrays contain Python integers with `dtype=object`. No floating-point eigenvalue test, feasible-region pruning, sampled-parameter inference or external solver is used by the verifier.

### All roots, all true-edge escape trees, and finite weak walls

The exact graph enumeration gives4615 spanning trees; an independent fraction-free Kirchhoff cofactor equals4615. Orient every tree toward every one of its ten roots:46150 rooted trees. For each tree in each of the four cells, the source records a valid stress row whose ENTIRE directed support belongs to that tree. These184600 assignments are raw labelled certificate records, not canonical counts.

If all selected tree arrows were weakly nonnegative, their positive normalizations would give `Brow:M<=0`. The SPD certificate instead gives

`Brow:M>(wrow/2000000)tr(M)>0`,

a contradiction.

If there were exactly one strict U, every other actual vertex would have some genuine outgoing arrow Dij>=0. Choose one at each nonroot vertex. Along each choice,

`|Xj|_M^2-|Xi|_M^2=2Dij+|Xj-Xi|_M^2>0`.

The choices cannot cycle and must reach the sole strict-U sink, producing one of the exhaustively covered rooted trees. A maximum-norm vertex is always strict U, also in case of tied maxima. Therefore every member has at least two strict U.

The hypothetical nonroot arrows were allowed weakly nonnegative. Consequently this proves strict U2 even when other finite mechanical weak contacts or harmless zero primitives occur. It is a proof about COMPLETE global U conditions, not simply apexU or a single optional tree. No polar inequality was used.

### Effective normalized escape gap

Since4D<12, each rooted tree has an arrow satisfying

**`Dij/fij < -tr(M)/24000000`.**

On the closed seven-dimensional core, all six nonunit factors are at least7/10, hence some selected physical arrow is `<-7tr(M)/240000000`. No uniform unnormalized margin is asserted as a physical edge factor tends to zero at a lattice-degeneration boundary.

## 6. A full-seven-cube actual-centroid routing theorem

Beyond the cylinder, one short stress remains uniformly valid on the ENTIRE `(0,1)^7` construction:

**`13D10+13D20+24D30 < -(5/3)tr(M)` for every SPD M.**

These are three genuine edges from the surviving original base vertices toward the apex. In terms of the ACTUAL centroid in the fixed raw frame, the negative of their weighted sum is `S(g):M`, with

```
S00=13(1-gx),        S11=13(1-gy),        S22=50gz,
S01=-13(gx+gy)/2,
S02=25gx-13(1+gz)/2,
S12=25gy-13(1+gz)/2.
```

The source proves `4D S(g)-20I3>0` on the whole CLOSED seven-cube using2187 tensor-degree-two SPD coefficient matrices,6561 additional positive leading minors, full power reconstruction and the second determinant calculation. Since4D<12, this gives `S(g)>(5/3)I3`.

Thus an apical-U1 candidate anywhere in the full independent-cut cube cannot route all three surviving original base vertices directly to0; at least one must escape by a genuine indirect route. On the cylinder, the903-row cover excludes every complete rerouting as well. Outside it, the routing theorem alone is NOT a U2 theorem or a proof that a selected tree necessarily contains all three forbidden arrows.

## 7. The entire seven-dimensional core retains the minimal four-arrow chamber

The actual recentering changes the five pole positions projectively. In the parent's raw frame define

```
h0=1-gold_z,
t=gold_xy/h0,
phat_i=p_i/(1-p_i.t),
p=((0,0),(2,0),(2,4),(-2,5),(-3,3)),
Lg=(1/h0)[[1,0,0],[0,1,0],[tx,ty,1]].
```

The SAME-origin poles in the new frame are exactly

`qi=C^T Lg(phat_i,1)`.

On the WHOLE closed shape core `[1/5,3/10]^7`, exact degree-two tensor coefficients prove

**`-3/1000<tx<0`, `-1/200<ty<1/1000`.**

Concretely, put `Jold=CJ+4Do` and `T=4D-Jold_z`. All10935 Bernstein coefficients of

`T, Jold_x+3T/1000, -Jold_x, Jold_y+T/200, T/1000-Jold_y`

are strictly positive, with full inverse reconstruction.

For each t in that enclosing rectangle, take `ei=phat_(i+1)-phat_i`, i=0,...,3. The positive displacement circuits with supports013 and023 have coefficients

`r_i=cross(e_j,e_k), r_j=cross(e_k,e_i), r_k=cross(e_i,e_j)`

in cyclic order within the indicated triple, zero elsewhere. They are the two extreme rays of the nonnegative zero-displacement cone. Set

`lambda=r013/2+r023`,

`Q=-sum lambda_i sym(phat_i ei^T)`.

An exact16×16 CLOSED interval grid verifies all8960 guards: positive denominators, strict convexity, all six nonzero circuit coefficients positive, every lambda_i positive, `sum lambda_i<40`, `Q-I2>0`, and BOTH individual circuit stress determinants strictly negative. The smallest guard lower bound is247/250. Every cell and boundary is included; intervals conservatively enclose repeated variables.

For a physical dual metric N, the tangent block H in the common pole chart is SPD. The combined stress gives

`sum lambda_i Di=-tr(HQ)<-tr(H)`,

so some selected arrow is `<-tr(H)/40`. All four WEAK arrows are impossible.

Every proper subsystem remains STRICTLY feasible. Deleting arrow0 or3 leaves no nonnegative displacement circuit. Deleting arrow1 or2 leaves one of the two indefinite circuit stresses, which has positive pairing with some SPD H. The finite linear inequality alternative then supplies k with all retained arrows positive; choosing the normal entry greater than `k^T H^-1 k` gives one genuine3×3 SPD metric. Its primal metric is its actual inverse, not independently chosen.

Thus this full seven-dimensional core consists of realized minimal-four-arrow chambers, yet its COMPLETE primal U1 cones are empty for all roots by Section5. This is pure primal incompatibility after local realization, not a new reciprocal-coupling victory.

## 8. Exact unequal actual controls and meaningful failed extensions

### Inside-cylinder control with no basal U

Use

`(a,b,c,d,e,f,eta)=(1/12,1/5,3/10,1/100,1/4,3/10,49/50)`.

The ten raw vertices are exactly

```
0=(0,0,1)                    1=(1,0,0)
2=(0,1,0)                    3=(0,0,0)
4=(165/368,-1243/4140,1/12)
5=(9/23,-452/1725,0)
6=(18231/46000,-15029/57500,0)
7=(2673/5660,44748/35375,1/100)
8=(172/283,1356/1415,0)
9=(189/566,16901/14150,0).
```

Its genuine uniform volume and centroid are

```
Vol=6081756283/17574300000,
g=(24679422265548511/79172303292094000,
   280332514959471109/890688412036057500,
   365870976923/1459621507920).
```

All vertices and poles below use this ONE centroid. The source exhausts supporting triples and reconstructs all intersection vertices from the nine actual centred support planes, verifies both actual mass fans and covariance, and checks the full same-origin polar lattice. The pentagonal chamber guards hold exactly, although this particular point lies outside the small seven-core.

With

```
M=(1/1000)[[1,0,0],[0,4001,-2000],[0,-2000,1001]],
N=M^-1,
```

the full strict census is

```
S={2,3,4,5}, U={0,7}, H={02,07,18,23}, weak000.
```

All68 primitives are nonzero. Neither U belongs to the true heptagonal baseF5. The pyramid's guaranteed basal-U property therefore cannot simply be inherited by unequal cuts; the notebook's pyramid theorem itself has its original, narrower scope. :contentReference[oaicite:2]{index=2}

### A continuous, unbounded sharp222 tail on the same unequal body

Let

```
u=(0,-2,1), v=(1,1,2), w=(-5,1,2),
M_L=L^2 uu^T+L vv^T+ww^T,
N_L=uu^T/(25L^2)+vv^T/(36L)+ww^T/900=M_L^-1.
```

The vectors are pairwise orthogonal with squared norms5,6,30. For EVERY real **L>=2048** the same actual body has

```
S={2,4}, U={0,7}, H={07,23}, strict222, weak000.
```

At2048 the literal primal matrix is

```
[[2073,2043,4086],
 [2043,16779265,-8384510],
 [4086,-8384510,4202500]].
```

Each primal primitive is quadratic in L; each polar primitive becomes quadratic after multiplication by the positive factor L². After substituting `L=2048+t`, all204 coefficients of the68 appropriately signed quadratics are strictly positive. The source contains their exact generator and complete values. Thus the whole unbounded tail, not just its endpoint, has all68 primitives nonzero and the displayed census. It simultaneously proves sharpness of U2 and a persistent absence of basal U under unbounded conditioning.

### Proper-subsystem metrics and a failed frozen-metric transport

On this SAME unequal body, transport the four literal chart metrics

```
N0=((1,0,-20),(0,1,1),(-20,1,402)),
N1=((2,-2,2),(-2,4,-19),(2,-19,147)),
N2sharp=((12,0,1001/1000),(0,2,1),(1001/1000,1,1)),
N3=((1,0,1),(0,1,9),(1,9,83))
```

by `T=Lg^T C`, using `M=T^T Nj^-1 T` and `N=M^-1`. They respectively omit arrows0,1,2,3, and every retained arrow is strictly positive. Their complete strict censuses are222,323,323,222, all weak000 and all68 primitives nonzero. Their U sets are respectively `{1,2}`, `{3,7}`, `{3,7}`, `{3,7}`. These are physical proper-subsystem witnesses, not apical or complete-U1 witnesses.

The four stronger parent H/f controls were also evaluated at this new actual centroid with positive Schur complement1/20000. All four give actual222 with apex0 strict U. Three still realize their intended proper subset. The parent's omit1 control, however,

`H=((1,-1/2),(-1/2,17/64)), f=(31/25,149/60)`,

now has the RETAINED3→4 arrow strictly negative. The exact value lies between−1/10 and−9/100; the full rational value is regenerated. Its other retained arrows0→1 and2→3 are positive. Because face arrows are independent of the normal Schur complement, changing that complement alone cannot repair this particular frozen tangent/footpoint choice. This is NOT a proof that no other apical omit1 metric exists. The failed transport and all four complete physical censuses are preserved rather than silently dropping the failure.

### Other preserved exact controls

The unequal core point

`(1/5,9/40,1/4,11/40,3/10,13/50,7/25)`

has strict659, weak000 for the identity metric in the NEW frame. Its complete hull, actual moments and chamber are reconstructed.

A distinct outer point

`(1/12,2/5,1/3,1/10,3/5,3/5,49/50)`

lies OUTSIDE the new cylinder, still has the same true lattice and a minimal-four-arrow chamber, and has strict222, weak000 under

```
M=(1/1000000)[[159785,268014,-114641],
             [268014,675518,-246819],
             [-114641,-246819,96336]].
```

Its U are0,7, S are2,5, and H are02,14; all68 primitives are nonzero. Its volume is224551501/659036250. Full coordinates, actual centroid and poles regenerate from the literal seven inputs. **Only this physical control and its local chamber are asserted here; its all-SPD U1 cone has not been decided.** It is a concrete continuation seed outside both the tied family and the new cylinder, not a disguised all-family exclusion.

## 9. What was tried, what is durable, and the remaining connection

The new route released every one of the six geometric cut fractions, derived the actual tetrahedral removals and true maximal lattice, and sought complete global escape-tree obstructions. It did not reopen the moderate body's already empty unrestricted metric cone. Numerical linear programming located candidate stress weights; the frozen positive integers were then checked independently of the locator by exact polynomial, integer-matrix and graph calculations. No failed numerical search or unsuccessful coefficient test is promoted into an impossibility theorem.

The durable results have three distinct scopes: the whole independent seven-cube has proved incidence, actual moments and the three-arrow routing gate; the full-height/final-cut cylinder has a complete all-root/all-SPD U2 theorem; and the closed seven-core has additionally proved minimal four-arrow polar geometry. The new cylinder and the accepted tied cube may be united, but neither is silently substituted for every realization of this incidence or for the entire fixed-actual-pole fibre.

The actual side planes are fixed in the raw construction, not after centring. Their actual poles vary through the explicitly accounted-for projective centroid map. The seven parameters here must not be confused with the earlier seven-dimensional fibre obtained by separately actuating the base plane to keep actual poles fixed.

The countercontrol shows why a basal-maximum-only proof is insufficient: both U can lie outside the base on a whole unbounded metric tail. The failed H/f transport similarly shows why an old strict local witness is not automatically valid after an actual centroid change. Neither failure affects the complete new stress cover.

No positive complete-U1 tier was obtained. In particular, the actual proper-subsystem witnesses above do not supply arbitrary-root U1, apical U1, same-body four-subsystem U1 minimality, or110. The full independent-cut cube outside the cylinder and tied subclass remains a substantive open completion region. The useful next step is to change the basal cut depths beyond the four certified intervals or the fixed base/pole geometry, while retaining the exact moment coupling and testing the complete global escape requirement. The preserved outer222 point provides one exact starting object. Global bounds and canonical counts remain unchanged.

## 10. Complete source-only recovery and actual execution

The capsule below contains the entire **62196-byte `unequal_u2.py`**, including all903 literal rows, all1473 row/cell degree masks, every vertex/facet/edge input, the actual moment generator and independent removal identity, the119 full-cube geometry certificates, the2187 full-cube routing matrices, every exact forward/inverse Bernstein transform, both determinant calculations, all46150 rooted trees and their four complete covers, the closed chamber certificate, and every physical control and failed transport described above.

Verifier dependencies: **CPython3.13.5 and NumPy2.3.5**, assertions enabled. Its proof arrays have object dtype and contain Python integers; no SciPy, SDP solver, numerical eigenvalue test, random seed, external data or old parent file is needed. The transport decoder uses only the Python standard library, zlib1.3.1 in the executed environment.

An author normal build completed. A separate fresh directory containing ONLY the recovered source completed build/check, with report and stdout bytes identical to the original build. The serialized handoff capsule also decoded to the same source bytes. This is source-only reconstruction of the authored proof, not proof-assistant formalization or an independently authored mathematical audit.

Save the capsule as `recover_unequal_u2.py` with its final newline and run

```sh
python -B -S recover_unequal_u2.py fresh
cd fresh
OPENBLAS_NUM_THREADS=1 python -B unequal_u2.py build > build.stdout
OPENBLAS_NUM_THREADS=1 python -B unequal_u2.py check > check.stdout
cmp build.stdout check.stdout
```

Do not use `-S` for the verifier: unlike the standard-library decoder, it imports NumPy. Do not disable assertions.

| Object | Bytes | SHA-256 |
|---|---:|---|
| recover_unequal_u2.py |32310|8485dabf7c69a7f3c1b86bbb9265442799f77b823ef7d11dc0f28b602e1d0075|
| decoded unequal_u2.py |62196|c469ec9b127addd02fd2f1e5059b9ce63b8afb7d35f80b828f140bfe572fe7be|
| unequal_u2.json |14359014|cad0d532998d9ba934b8c653d125a46faabb03009fec8e30008af1a01fe191d4|
| identical build/check stdout |743|92d57e7c3a44cd251846503310dfa084400ff9f7ca931ad4f417e85a4c77a019|

The complete coefficient stream hashes to `216ac16ef93094b76dc700ff04e4661c1e28104fa6abeb9da35990becfcea263`; the shifted-minor stream hashes to `35cd558e777865e6b1cfb4da3c7ae40e06a2a2712b7981966ce6df23ab3b2cd0`. Their exact ordering, positive denominator clearing and byte encoding are defined in the source.

Expected terminal stdout:


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]


Complete capsule:

```python
#!/usr/bin/env python3
"""Complete source-only recovery. Decoder: Python standard library.
Verifier: CPython 3.13.5 and NumPy 2.3.5, assertions enabled.
Usage: python -B -S recover_unequal_u2.py fresh
"""
import base64
import hashlib
from pathlib import Path
import sys
import zlib
DATA = """
c-pkRYj+#Rl{Newzk)NfW&}`8sq4}=(w+6lu{5^h$oEV<e7Lwk03;!i01bc?mAv`y?>T#)YBWgNaq`S~$ppH(y1Fjsvd^Uo|Mo90
Z`Z4rXY<9&+2U^R=Hupaxd?-Q{nvl}@$Ktxe|+`T={K+6{_yHQzkYlA+Eu6j`PJ8-O4*P8^iS@^-s}7EWRvYpXPepTdcK&iH}lEf
&1$(k-@BMCW~=dLxq319{WoZIFT8N!MUm~jy}kbC<DP#Z7e{;Jt1BzubK})&{BgZ^Ili0iO*bEJX6^Fq-E6WMj2F|r$#St7&lh{v
;C!)}UCdVN7kh7)dyCua*=jx+U+t}zS9i13-h91xyPi$=&OYvKF6Cmqyj@LZF9saq-odAPw~N`&x8tkRTmRzb<KEfr{A&9DO)h7X
_d5K+`D%H+cfOJl&X<ez-u(Jzx!UZ#v4XwvdhZSE%w_bO<?^blBO{sK%EU~T*D|kTJkP4v<IQENrFXNd$#r%ynP&P3tK3MHtNB@~
^^IH(?EB?-t+%pw>*XR_e_Usq`SmQ_l<~_Tq*sfZ!P`H*`mU`8Z@zDb!#oRFk;PFa-(u$Q>9RVj@U6<4%;THSf_%EHl-fbAnyi-V
C|9L?R`NuH`%$h(gV&$6o7<bK*>ElIo=u1A*=D#?FdL2b&X=pbb6KUmH{av?OuzqSeltAJ&X3*U$@BB$Lw7Qg{|3@uK0e;oeEk`|
kM;X-md%b24-d5Z;PspKud_qee}_8nGQ4L7A{cLG!#CfL_U7k%v*Y|kZwOrp`OJ<TuSWfs{B7{xufO}c9ljanqinPvj=p~TTCW_h
zDOhG-#5c~+rDE1@3eu{cyTcs1{>~tr)coXnzcV}G&*|itnu!Kl=-fn-53o%&9y8RS>v_nz`2lxSfocj#Um~hnXdyLtn)f^(WM%L
Kjf{H+EYh=@OqV(R_Exmymin2kU#%}AAJA$7jJ%OeUASI-@N)x7`}ZrUSFKXukL@U^P8`JzWveN&Hnq<>3_ff%h%t2);zOXr{916
s(n_wdUl?l=gnDF&ZfEZby*i@^<?bJFmrWNS9LraH|Nu{IIiltc3!&Ss_`tAxzDHhv%z3GlNFjyhvV#Qbhw&rZdZ#v&iDQEkC@o|
>|>%Htu(?T>)W%Z9y$26M<#M{|KN%7KA%ASdsdt-H#=>wZ?A{<`@hoiWVKwccODszh2Zwjj{V8OSpLX2caqt+T+4Fa&Fq`gGRM2t
31O@8=y0I4d^KCh_qKJZd3{R$4fc9H6gnC0@4wr}y>}=3(~d9scXj;!1VebgB~&&HetG{diMCgIf2>?OdPMB@0K2$ZX%Ba%Q|D!W
Z1=D4o|tf*+?AB}US+kfpIFfTGZQ{D(P!k<XQRh$%olf@v_;FF9!*<L<k5J&7FoSF?dEKkwK;pk`SW)pk(7@nZ!D8{e8u^@+D^v;
Q+M?*?R@lbY8TsC9le}BoX5pup|P-8Ti%LN`NgTY@6+oU8@cb#;?umOrK@ahGnTC%)A03L6zFU?$sR7Lu+1b}J+WT%#d5WNL;;Uy
Zm#6`a01>xo&YI&G>b0dIzD%aiEpO*N?T3o!?5ee=y&;GFg`y&U7nwdQc@v#5bLaNAVj-w+S02xZ(1Rtp-K^zrDf)ePAnf(dNs<n
O^q_EsI7=x)mlELZwD?9`2P5jSN#%s?>Aq)QVk<ISKc)A_E$CZfzJy45ScCY29qlp;odhw$vWuMQ$bjp(^Jv4SLfM%n~x6l+lxti
|6=lDvb^~?1hviA^Tm2IUQC2evTsIvv#Yg0srh6xynlRO%dN^^r9-2Ag${>rr0U<a?!DdmTk3+4Q0l=_S!{3GvJ=(;DZ%1pce;Gv
43{IhB>?GqJscfQg@4-Viwhx+_f%5P@8kiaoNtDIeSdh@e|(yr)UMq9O&UKvU7-i9^(1v`F}tvCb%coK4tCnJo?4^Y9-o#)>J2JM
Q@MP8pd(1tR!`Q`8qW{3Fx9)hy?QuDI)T636Rks`l6`n$+Vt+;I^m<|XGBHWSz_P!*_8l->G3*E?mA8G{)c~fdeQmT29ZXzS>4X2
^Sh@fX<t|;+s@ML=clU)owgiUswtwTo2YvXbJga*X`XflFOS~sw`cqNW4*n4-u7r}MQCxeT+e~Rhd*m0@_07Mrr9hz&o0}ak0v**
ibj!f?qHIAD*Om>_gdlF$D&2~nU;5ILwNeN%U=6Tp<~uPJWdafvsWSrJ{H?sm)Yb7w=Shvg+#hB%|7+GF~u`o`7D*s(2?zp^K|1}
I*_#R`FL@9v%LDaSYFS^SHquln4igfkB+`<hw`CNc0fQrp3I2J57S&fl(br9B&rbejmc_<KZyk2%4$>*h>_v*efoT^@cigQOYB5I
Bu`7(XV2RY(iI)Vm)iFa7*A4DT4g)ApJiWi+0N&)t0~w0XCr^1Vtx_ZuZP5Y3Pc6iXmqF|{%?<v3vV7hAb`Q%Pi>z>j-&_eqZ$1*
G8ycBm$!e&_s9EZ`;(*ZT>5^wuXRU9-}&|ret)_@+ZQRJVqBVRyBU!Gm7Yero}egc@5>zbt!`TVKjhi&6VeNG;}1T2y17q1?5n+Z
llIG;6mTtCCA)+69}d6Ev*D+C_S11Zkw3+WlBuYm?_4&V+^|?E{ioyd1jSxzd%3K%cCCLJHQ<y|)=5Mu4!uj{0ye%|KV=;qNuN|d
zMJR>(5v-Y`)Ydqv$p*#Klo1mxr6UKEI5%E!!M<2S@_8gL2ga1?&<vC5Ax3oV8)}L<(~)#{C9h-uax)2{m-(GqwLGk7D@diSXu~q
BS@lEZ5T&~%F}8l>$j<zzqNjwslsmb+j%w=^IE^1WkWTU<=drd%lWnqeW6V8tC6*YYmaNRXV<!7Y&I3BVUE`2X*O<TaQ2Y?<c)$D
+v5|i@H_*}izb(KnN2TdyT<xZ?#rSb-L=|Hs0^(Hu=3NfeibW3*A`#%lM~dv19<r49U+0d`oLv(s_<>Xb#1;8;Gkmu<LIHC#J1mQ
tMe0zFV6J#^)miD(5jB*#rWoCwwMkR+YkR+A>{j${X0S6&v9|37w=C-FTEkg?20r^VC6DSDBT-$e0Y=_OPIL%Ir}LShR@`s12eiV
R<qggX8i!vUXSmG!}rHylHHBI>t?-`px+E{M7fPJX<~ePwGn)_bzk(Q4@KK@^<li4o?eePtNHzKkzFmb%enH=6L4P{>djF7MWPHY
NBj8pUcSM@BoAMXM*CMwv0P>ca(j3=Ke$?oA#;fiTy8s{Ncnv>1CZXjK+N*!3g15{q;-2W8?R_qO=n_QO|FOgL&b?N<WfZBLVbNb
^I&U}tb}@OP>Y)v@b3+ek5zu_<6>kjdIrquq}Rqt*7pGF%q|AW!kewuvow3V#@=0fe5@_^8-0HK3x1o$$b?9?+I1j}M~RpEm6e~~
wTs!kAlQd<HP2}6DNQPkAE^w??u6!B{gdhC(Yn<S{idJo@%_v7wx3#b@>nVJwPr}p6CAYH9O<XDbFhBwo6uW$?dar5x>_AC#Jt~5
_#Kyed_P~y)ZPp?**Mb+V5U|U?|OMR(}E$(h0TsozL_mVw5ZnSBeQiYY?kjVeDB$ut#U2TW-BpAW<r@a>+EcKyO^$Jp)cCE%f&2P
%_gFf1%6I8?GFM%wI?_0_E>qX&xI#P`pA}Xb+Y72eZbldMOHFRFMw4Sxe@W*BMR=bHuTqxV9>kq)$L5chzx3dIlf6ERX7Co7C_W!
`)2uJw$f?&%S;f^5VfDfX(Bz#M!Q5kF#qMvF8SSH()&>OriX)j68F6<?<YF)C)A;#9rQ=Q+3;O9I%$>h?v(2k&Q6xI^Ya!Jj+Cvn
_-G?fucfK$b*E6U+9GI%6jP(!&MK`*4{Y^_1~%;@5%)%(R#RCUINHp!&9tRd*^G|nn{3`)KVa|8sHbI;2swr8ekhkpcJlaUKFZ{3
_7Q8cJIVV}VY<JWq9KlXOXTwmC8SB6h5dFj?M*_`L__vb+YsvNQ6?;x*;=S)CL_?cj${Nnoz9k!(`V0PeP$Tpba*vii}vega{E>V
Rb8W9XQhc$X#M4z_FHLrJ4r(=;+@gIgVfs`An3vDb!~wH_J{rFUcLm4Z1p5(NeY!c4WQ3v(^Da+wOBRMt}guf)p*m&_ZO@2-Rx>;
^xczYIZX_yHp*h&2&lPyaeFh>(GQ<x&tAM+iYSnY-I3s0{rLUi`{(+^$>{mB|GRiLdNEr}mebjAWRm1!w!EHgRv(9=(X}hr^Xc?z
1~<8SS4R8Q(Z#J$<d&?@=UFm`c0vcbqKlUH3xNyl8-gM;eNIMM@0Q=amHZ$*P2+Nk@f(3hO0tXo<2fFGcS881^o1w&USjsea-%Xp
Z>uyr<WM@|e73&5(KyhvOa>+51Pz(j81~%n0$wj-jN)_1>FJ5l#mSM<RI4~A;py!C>|=X1zCN1@jyW8kt%uTpY7~)z7ee4rcv7Md
p8PJSpgmB!-+S1>g^>053jG5=d^405_7{BA2Hpd&h!aW2X<8y$q+c{(L>1W46=n%V(2<xa#es@)A5D{R?cMAiz0eBT`;m2|zuH@v
ip%$QIqLOQ`Jbe8blF;9?uCeYUz9@?x$9P>e`^-k`}tz3Z@e0x&8{fw*)Q$38lux#yVZloHz(OKAnVC~B`^Ytr=28@I_kMSd2jSP
V{cu#RHU91>BjRGfeTrhEzDqzBk7>sRq^oXcAvQ?Bgi-mxtq(~QB7wu4u~^rpl6FI5puv9zi<sYtA(#W(}JqA?Le(k<hQZI*Kf9}
x06M1XBsnGw=!Drce7Ins`+F-lfJ86pQ#?+EtQh2S8&ROYcF41&hDr43lWQ*R9P*TVl$m?1X<7(@o#&t?=Q!<Yv|v-=0I&1jYO?y
oAr@~ocETCD~&nN_Qb*wF}vp~R=QY?Z!TZxAl7Oi2<c2jV{Q_a%rX7_ps}%`t43-Ts(hcm6Ld>Of4U=Ec5vhTKDln%*PjXb9?5fJ
x1^Oj8=>H=D;VqYu4kgL{+j>o=;zzn?W{#)X^SXO*g4?9q1wj$gq#P7WsIi{9qOMKYOcN;vBC7NcRj(Rl}4Yq{7?h?^Tq89>RG1b
d8ayc`kxS@<CQF1dwk$d_FaC&%VVv3((2zd29$JyWp^A;4@A3W&AmJMBtPuFxAP~)p}v&&;34<PC$GMHAsjKgSNqx?o1Z+6aL5>7
N&gFaidIMv9b;*uncmEZG1-_(BfRH*f1$x<SK}KYi(Kd8Y0~I9O<#X@DAk1;<eyCQkzSmg$iH+k){BGfov~i10dTxJK5TmSnckOz
6REh~Xq5+=zQ$VJ%<q<h2-I3pLZm=IVV}G#_#?or8SPTpqdR+dEgs*upwhwEJOg;gyY3x#|BimO`H@v@?_R#tB54G7tP=@LAJ-@H
uWiYbZ7f~U$tf<-h^2WahFClp{M+7})$%VhK@pk|vv)0p^P8*rOv(4d8m)*7n@{!f<zyyegQm*f<Z?Nm%+%7jx>|mCG5GH5|2qBQ
^`C!epFMjvaEBVa*FVLfk8<f7`4(dq<W4RH`C)XKmm0Cwvbr9G!!na%muqn-2gPAy*RDJ)2QF$G`h*6%nnPFC18F4JW{WI@!=lu;
#w;F&CTk93DYrwdohY=9-i;pJ(b_KN121i5(r$>Es}74oUKt8~XGE1c4$8w2w1%&=hCJd9L#1t$+Nn_Kz;vA6TMN<ypZUWgNDqRJ
J7#!`^jn@T4?RXB&H4PW@Y-CiJ(O#`SF_8Fj?~riZf#%gX`l7|4dxA%9p_Re0k5nNz0)eLvMxxYIc7FS9ahA!f)+G>Q0v0zzysdv
bgI10q(=>peniyBwbf7z@N}W`E&Z3b6qp&Oz0vt`gQyQTho#4&>GB1imC|QCpxu<J7`oH>(~;>+Nvp2lR28)hgHxd-QfMb@U4LB*
9af?Bo%SN=>!OlD;kCyyl{%j~f=2t}8X+frRc<4YCvt5&V96_aw>DU#Z;dWSsV|g=>%$riVCr*SJj@a1SynyT03zmD`%>icOi1tZ
+6!MO?bx~)nb$g}m<!MMIS@w#eapHzrL|%^qnI%VvMU`p1nXF0wy{dC1btRA=><4Ny9{EHC1`X>oYG;b4=EkgLhmKW+i^{bff9*S
C<CS>k<MYs`;88{kS=nLg>Ix<;8AH-$zS{Iu->JS4G6r!qSkn?ko`a=MS7`|pi5R9mbp=GfyMDk^8I3&NvwgqTUSo#+>@X@X^kx8
Aq2e6icGPzBGtW2R&A{$8dp{o)-1IZpKE8d7eVDmuYOcvP+2ozb-h{XkiAM1$_0<g0TTfk<4FA4cBM>2S_+`y2E(s&<*h~tFQAu7
#ClIF2lAHARdmLyDw&Loa|{XZ)3<nv07}r@CI$UXVoQ0)k+gM;c&{=OC7z6tw4==wI(yxWd+oT8GKS;8S5mt+@u;hz!cB|4PLzzK
0`ov>U}1CVxOT*Gkl+Cn21;0TUcPG+n31SWWG2*AKtxK68q}#0Bn@4s6QW8<4wPN#<VlO+Fr*Hb${$LH!ay8FCr8j0Wo)N(a-C?e
?2A{5UhwrH#Go|hNS8GxTZvI-0z~8>m1QARe|TN0Is;XfDh1@t;HXBWTmd>L^kp@sL0{#xVla876qpKCND7VVya*jAvFapZtbt;Q
JY>>Jc}4q=YLxq;@|2i!vb2sLbXJw!qDg@~9zhoYbFQ2gs@@vpV71^W%WAN($_0$K96+6GM@WfIJ5m_cJBSLBsZKB&5n_no5sZr~
S6d^d(Ms~*0Af)l9*abQ<(%?aP(m^C1|2$;tW+%y6OwDo&`2^NwaF$OeyybDxy&UeB|r)QegrPGNOuu<QEQVy6n`W-sq2JS$YPvU
#U9`&(dg8W-~%IYRVxF-AlhTFi_BEi(#CYE&UOI_R%@|L8Z?>72NinKaak*pK}S!@Ihdgm@>Io9P{D)oI&WiFeihj?h*sKQ6(P_-
3A(J1Evkrf9XWJ^4FroTQbHw3F);EL260$9nT`td5tTlmo_w^a79FM9M)3>53B;K!75TqGtBt;_<cL+Z=2jQ%tE6WA2p||C0k7jh
|CMSqvq{CD%5fP7G_B5Nr=nCBW7^2*y0Vp`$(V#$wH0O%<i1Yi2q`bMg*nNR5cq&Qdb1o<hl&qkp5zlzq+wL>plUs8YxI!%JAyY2
=c-tZQ1jZGS{s3~qQEz}<v~U{DMPA}b)mwPE6}gTR#!n?&^||lY?aXf)ML&SAc5pIOy4LK=$p`EnHcEl(m2dhBVk5GqSU6PeQBHx
YL0|6)R*NU1X#s|?UY&w#wB$E%=uO;L2_t{Fq@Gllw!EBUP)6|Fu^Go6fhPI0i^JXHXP7`3QSoHf)1G<T@QU*0jcf@g9AlD2sA<*
v<#(MZVDc_24fNIr}91P00)*oKxHT~YsW|cCAp09u*Q(1sSId~8Z#ObvD8}IyClpDBj*xgqyrxfX1X9#N@sCR)E3N&pwz~U!G7|<
n|NENc7#yCtr(%s520HuO#ejS0^li{KQ)A7D3n*Ys6;cm0tzB%6F><xrlbMem3$5{FQws5uN{F9aqLYAmJO680Yd@<f(De7!Go2u
34j~uExN=D#UX4x*BDr&QcC(xUxlIhKuKV>38aN9P4ZPG&~fSmx*Bxi3k9qMlV#qK6@^HIj0F8qp%rRq6*N#GI8`P<!G#8IZ)&t5
M5p9Z84V@*LWn8?R7=R}B_IVfL`WQ`cN@bgWH#+yRVEbY0eOrUiB%h}chJXy&1!?Q5sT}9usaY9rHJ`UFi>^f0QR3vae;Rf5Uhc;
2&75!)j5TUuL3wHkgpAp5QP!~!m0{tgv12R3bW{<KE@>_lqgMP8EV$<D!aoz1Pw*wW7yn^wm|HzgD#HrKt1gfBf)U>a1Yc;P-D`y
SoIc67nxOuKE`AZb|$p+j|5SfMd5&<Xk^zl4Otfqx>$E|>rSaF-=uMR11vK2w2+ma0`)#;6l5*pL)s&{0Y?|;je@yIL54*Qu(E{z
yJ18yS#DOUsu!hluVa9PtSps4GhGlQBSjFZ>H>{l#c&Z6UINKQQ^EDtK59$};B{q!qUbEdMFYi+B`?eXU}K<U-@PxIJu8CR-WQ|E
9{?v4l9efV%o<l=t9IlKgsmz<Xz_Uf8Evji<|7S@Lc5nkB?D(0N9i*vMLaObmY|A~<|X|Wpm-ItfL$1&-%bfF7Sg?nJHP_S44<2c
tMsIV3?r(NH)5D>%j*Ci>cufT$g8xJ2P<#S<w=oKe@G{D8%CYmq$X_bdlW^aYV!0U(Zmj}dV3m3(X>Ztrmjz2g-lU#rT2m}$?L!!
YO)2qkj^!o>XL#01E_7ny{g&<#+HZP=&=RVG{B;)W!!=p_LGFhm2@Wkk|GD1pqiuTkDx10?^XaR3AW0mVUXJFB_9$1q(ID7=K!!9
R3mEf9`sbxpt6N6vG(<0jrpW)?~?BU&O8PBTq~s-vw$!L03`}pC?0KJ$J7`Pa9V0}PXJy!#Xs83T3c*DFg~G2>ZcN~b4D@FL}+g7
UMK04n=IoRHQuDGGjAA?3b2$jeGADQ3CfeY&^Dauwg{h;!VOat#J=W$q8%7*D4w7Z{F&#2&hj^pA*K$KCZw(P=v<R~RkGQXF{rhu
U|{@GbS0(bxajnU6u$15TM-g!6b9#Ak+gB8FD0!ySPpq2I-ol544am9X95G2>bi!*W{YuY$QEWgvmq7iTStV0sP#2#(9jBI`a@Fr
yhC4xxq{WGP{SQIoDI@W$BZ7*sMLFPBuDmMky@uWA=)dvjnqN^(+ACE4RDYEdpdGp*oqh|M_n6c&5Z*?nT$iV3$=?mYH+gX|A*rf
^I7OLIBy~VMhsjjE^g;DU?h<?NtHS(ozoTyV0~{3QgKxY9vmT%Pu5wWVs;K1$d{ggp`ccWL#xX1rV6~=Y%!4!+u0}+a>x^G%I!V7
BZiybRajUrz(AW(HW0SY)ko{{Lj4wvEo@1LC!Q)I-dcr%%T3FrtYHknbJa9(e>C(#Ht?-ESI}U<u1Xc3s8f`c##j`SI<F>S?bMRu
MEVK>JE+xDi};ZV4CrH12J?A}zKn2K>saK$f)nN<W{f_j+^h4_<qa6AF5tf`LNxcVdP%i{{)O|QqWxK5LIW+9K;tC$H5t=Kf=1`G
3pst}d8CC0VeTSTC^}h(5;aN+$_Vn22a2wjb%Pa;6s1iC_#jilfDkM$QPlLbmnNPf+|qJSq)&l0EX$nl&eiM<5d>GTvqDo+R#Lm=
Si?engRxRbThrESB5VSgtO8ytMIfQ3m$FbtM$93)927-t$gnxB9QtkK<!Ub#6=a|HIVS}}*0%&DXv#4ML{<=}Mat3O&;wa%c!el>
e1nk}gu$}d<UA3xwXAyuVw9zI&^1+~O0t6eEgZz<^f`oPflh^-o;Nd1O^X8G3wNo%ju9YNgJc?dlZw*Rm*N(qmdc^|qUJ;hL4ar=
Ez-#0P;!MM&OpS%mvFa82hfpNU|dzrVX;c3o8n}AL;_Wy6A}=?!=J$ReMMPRCMPnd78aMtv6_Qb<UoU<(mQ1Y$PW$g!1+}Hrv@6#
x`wJMl<u(P3Pv302P<DvD-mwESkU(YuS!9TSTiKzyb)9m=ch8GdR`)9f7Ea>hC$bxSms+*TjmWgA*8FPYrqk}1P3mNQIT>3b3aE2
AjfUjRGfA?B_m^Xh_%(Qnxcb=4^R%n)fWsH6_8fyokzt=$tYMw;^+u4qZ6i*0TEt0Ar#c8<%QZc-mKK32tzv<h!Dx6u>w|b1%P0I
{?jzFmxVxQA!34!2L0&ISEf{Ap>!!LJYVDaxbr;Sl5pTRa5BI@*AO8Fy2NR~5aiYHS|L{E$!Oj)M8?>5z^h<C1h1$z5P8Fa>JZEf
xdxSBUHS?n?iqV3XlWp7iIu>+l+{&ynr+l<heE|x5tVSL@UeUCH~dR#rzO0A#jPs@VF9;8OhFM{4sY!$vZWWH$>|p>5S7A%wFyZL
FuKMeSPubK&^QZ?`I*(=Q&T8J0%;AN=yVsRQ7c<##|I0?bz}rAhd`yrA%LX|IvQ%c*Xw&ri|b$vF(*|zPcpBRDjSWNZdcLMjqBh}
a$3h1%K6ZOISE2Bg(~)1Ll<SBYaen0Xv=eLwEx;tK}(TJ&LS=j{VB{RI)Ex?q5=b80$Fq(9OkryL#v?;>H()b(*O_~CddgKMA^{M
1y2gRcgko^C!0!^=0KhI=CO`j&kcoVQIMZ73|k6Xi2727Ks_gd2)M>l!q18jx1*r;4d2s%tQl-8&>%DeG^f&`>xq|;Bk3YXlmU%V
F@}OX$heoP8=5f`*J?UAn#_4=t}w2a25D+KXXtQ&Ps=r=1WXW&aR)>ib9%4~6(zyBp3cYIh(=V8Cd7Y?p$9BOY}9<k8$&^tArMWY
QNRc<N_5l#bc_%(6<7dWGs4sgwy<!yIzo8IY^sLn$-`ykD#RiS<lj{4YH;jrh>VvZL&6~h>A^`2K{*`@HT-=+`B>#l1z`Y1=n!E<
5=La7L12Xi)3gWh{~{P%!EIDBPS9XxD+N2Q3>m#4a=RhE_Q5=EfGH3lmU@E@N3RctTJMC2xu^(-YtppBn*emHQvl)JtJE;0NXHA}
uA%DuPnBaG#@5mQ3PWeeUU^=bDuw|Oyn>1{-2p#FGPXjz8tyP%m=JQh)IgpHMb;{l6n(=nPE;Q%M2!`5>%1uDWwg||(b3r}>wt(e
T4+GHjzNC{HSbtU?YtNegNEXu<*P3PKW^_L>X8D~i75gUWOYb+<4oSvsMQ4HR`dh?WmFEw2Plb>QJs0Sk)0s7DjMNjJ>)3mWK~3~
OCX7$s?c1^pc7S*^tYIc-{h=iSTM%nt703AFEKNfMdtw63NsG^r=~yzM@=6eX=1a-o}z^;5jZfqXmUCjD>hJ)r(AF34Sg$^W14#*
PZ9|JL33acC{<jGoPYq`VHTBI9mpghb2iYzq6RQ_jSoP!(i1~{<V)&#IGzMnD`?9dg)8wip-EA5>;R1-aB2=JHP#rSt*kMvl?N;w
9QKv<pR=CRD-Kpv=>V^{G}AEdOiB!8y&YZ=Y4)05ne0*#l~MRJs#bIC1=Di6B?-<9L-dHSp=fA3lN#yC(c#x{Zb!z(lp5fU$4g4E
G)<qJTvxy`;mkzW=1TwqNQKg}^vJr-kQwApfp{EaC^_MCAoDO(Z9cPP2Es{=`E-H3XY4^Cv*H>xM=NSM#w~~=bd7ZQ0aBx==+bPM
nu76HjQy+GZUzp67gWC$wHQ;^XkT(YA9bRzhzq#2vDG5@FUk(GYv{IunANr#y3}&tuf|-$K)<;VS^+vY4CQDTDIEbO=J47<R94{p
inySrAZC7Bj`V{9S%WoerI<ktv4=`<0D3sn)qJR!a*<QS(9U3Tkp~p3sEp{w^9)1k+9(xSry9h8Jw+!g0jOz;i7T|zF2ciEha|9I
pD`1$L4Q;hMICu%;kKAOtPL(8wNN!zd84yi1F%7>kp1cTMPdtP5`oi-305VlH1L391r*0%AsdVpDOw2oR&-w0MRK53ux>CSBw02E
szSP&TB}IWIgDeA5;ur~3p7OPC16a&T+6azS{I^=jRs4gI2rmOFxskD^sY9_fp9VX-h=_$qC7=>i?Irt156hz5kQU>#@aSs!$5Qx
55k6}`P+aY8hC|eUJ?Jq7>mLzgDM3rgdGPR7($guiA3+XZy4}3&qgG2*0_Jc+!)L$5@Ykm<~@g{t#T%^e*w?ebbr(QH~xu+e;Q1A
lMr9o-8cIKj0K0GiV9sUCJEA|66gYsk&v{aYm_<yZ-!0QSSA@njR{iEi~xwgz^s#oA~Z5cSnCwhT@o!yY+eUTRAbJcM#K@nDe1nm
SX3})GWow!53P_Fb$$-6a%M8tz(>pigHJD@Zl3De<dw8XY59x1RZolMXfhB`F^rI#PI3bRF9c%X`v7gxsge_66%{?Yh@=szGn2J3
bA@`FOIfLt8CD1rA(J;5PAbowU0HTSfPn_-52G(9r$NXdO`~-zV?0^}T{T>pbS~Y@A`9Twtx9G!&`T8(=zvFC8>#7dx9BjLM`aED
HB@nVO7fw$@oXegS~dkb?USWan~CKc3Nbb~07z^sOkF`bsIvfGg204#^?%hNAv?#k9I#KRbBC&6u2Adxl#o|3MV%_rW1Va^Py0eN
!a&`SoGFWg!fvMfF(MKnJs&js5~b(DLf+9_XpmQBGhn(pu_Z)Q!H}t=C8d38LZ?(}ka9^sCFza{!2%{yP0K`PY|jA*#h}y<<wI0m
5Cxaasmp07M@AExQaVK>!@zmNs4X=kMQCWYEI~<Hngh-_h7?oQ-2@~VZaJ{F+n`|Ib&+%eYqD}-S~yrfLrI5*j<9OFr8I!!Kt+{t
5vi!GG+M`btr$>avbGw(s-SdQJyPu*ZSGwYr2?xu^<7X@)4f;|$kNJH2Wdyoh)gp-7&ScwcA&5k5y2!Kczd*;Rc@9N$iO>p2hmz8
Rcd4@Sc;4~GTe3o?1e?jf~_q$6#_?2+=As%tXtC-%He2-a76gAQC@`UUW6X{RyYCY3~icNlgc{|GrQebkv3MLuZor7j0lg2X8Vww
Yofr~(U*XEP>EGSZ%5ib5q3mi+M;d+0j(mMT+u|Jb1X2U7PH`bHkQIF=s%8ylGGtI&6!nU!Vokp`kD-w13svm8Wr-`LEMTU*inpl
pf_~ffe0Y{-H!05S5Pa#t=;518iGA48Db(8_as)qC{ANrbaFPOsGjc2z({M!gz&N=hN&PDN*WbS@;|Cs4jPSVs%mCUc=J*sXQd#s
5`2fMept8e*KKy{GNPjc^*eH=GC7lmm~Ip8GdLClV(FLx#{9}MNhyuh#pFmY82VtRtZHRpOUwdsL+x4Br9M@JD;0eKF81j()@g}S
EzerTgIaiP4M#DOUqCm}1(aFjndpV7l4(w&$ec(+%JScBj}^Tlo;wesRtwDOAOvN2uwqg@VpB0Novv{viETqcW9f(_VQM7$yCAa*
#v^iCVT>*Xb0dag!1Pp?wv$m1lRpdESG7;ls>Xsd@1y`K0srL|W2hmz0RcRN5Jktx!75Zt@eU-?9HJxCa1s!dd&_J#w>34Dv+NMn
i_8?unNUSt07Ew(x}=2ZdvnC2Nknj?Ma|6&>ivbUMFSXgZCM5wV??<{LDYfh42rm3kcIMv_}6^JaCxg+U>ljB_Gt?4rmMiZNaUi|
#-h*Ig{VeIO=o7qP>t4OfL<L{3Gp-Q&eC?df3eKrX6GIRCO&vN$P4&E;lZjQTPz{7LAt*BuFP)^zG4^|<`*`%AVNkw80hI!a}=71
R;gnap+m+uVYI^wlx<X>YB&Qv+9H|}31G-*Tp28qRAKP2ZQ*>eR0$X@Rp$(^iN0!P*Ogo=bOU<=^P1bglI^9#cW^(@InmSv7)FXn
oGdC!GteYTK)({)SUXG7afF19&h4D$rxG7C=@F_zBN|9_E+G>J%qqrXG;5Zm<T{T;(bx<i)woD%KF5mDU5RWTPNqwVyS?~Bxf6dd
)rJYJnNiJdlZS{pTurwnS6J)TfzbeFf-~~LaF_+<G^Fe3<O7T%Y;j<O662;9t@J&ZM5vA(r)mM#U1PKhJa;%SKbuBfnl@%$leS94
iGX@4ay(tVY6W{sbd(OEk`h-%%e&?~s<_qiIfAQYV3roueeNvmO0Ovm{|ZtckqBpqW<aUFjWv{JQJJyb;BiIHoSMcl9IcLMp|}V)
AJX>V;p%ac0WzdERS_=zNEZu@=7`j+oNXu~D?=}px9OXE*m6odRuOT!oK^|NOEBMgOtS!^!hFnyZAGG&-*&h}X0kK0ye{DX2Mkgt
Hv{>dKOH)3>n^7a2atfhO-w`~eZq<Fk+T{qhE2&<WiSsy0B)f`Km;Ln;yo~~td5N2<oER5IYx*bg}h1vO+my?351uJu85SLhCU(P
T^225QkkXVEc>hii#A-P9L-eptHZu%EV0)DAXK*4WZU3nH0aEFZ$hs}KDR`-3T&=?VUbymzDD8<h6uWh&GxO1foTgS6AE#ghlWBu
9@af;w(kYNwc$Q5x_v|EZVYI%f}_p=6avubX{0MPG~1p+ax=A#IR_RGQyzoc38{@0__`Mbp-+g8KZhQYG)wwZN|+7}cLg#H1%jKI
mo995&AM$0J3ecsFuJ0X#*Jg{AI!x@F@%mORcg#f&SZM-d3E%aLw13BJXROZEGGHq2*knOcLr8Hfgybm6&&Lxer-cGdy`kmG2RQF
*fv~ZN+T*VTuD*Vc)HF3bxX*;%B7e>@`{(1loz*NaSWuSZ<@|dO3})t;7f@#Bc$hOESeKX{nHe-Nl#~&TL~K^*W@APk{5)EIjxnn
qffm#NU6}IBvztSqd@fxiZF|}E)yVh48o?6j^(^qNXPX;I-Vh&suv(}2(u}1!D(9VL~Ho&+M;>=nPR$zK}QDSY9N7L9EP?%cS`^n
x?Y`Pr%u5-uqVv7BUI9G|6)O#kU130m}{8v%bmgI4`aN`X<Wo3EkVVDZiNU2udxHPL=?JkDe|nuVZMx*(s1CO82F^+E&r2tAn|)(
<|9;P#r*;Z9>>Z&eFe!{ohdQN6eOTCp@2y)p0LhSH&Nv1>^9r@p0o25AggTSbz`ol(t-#j<3yd$yN1KoV>^`6M1@D_sD>Fu>O^|4
%1GE}be~s<F4hc3d*%ieQ1NODSn4Ko&3%(RqiPr91Puax(4T|j7wQwcIvQP&#@j}dPBwdUqm^)e*MK~gOFER>T@AuB&q0x9q#fDN
IB0t6p0(%%aKspFCfcqleT^zT?yPf%6qA<57ReDcb8o7yM@=wEv31`X#O@5D2>IKfZ(UX5sZba=#5mz=FPJS(j|QCrk<N;`=ZfbB
!iF4TA=3tC7$RQ}LIKSFsex4r^U`y0gcO!m=L;kz(p}CZQ_fd1L<)6LG3A5q<iK5%o^cG%O$YRRM^FNX$pEo3A$-=+-29HtNyl&=
T>SLZ5le)i36O}IIBp3E+##U6ji6%%mtdqeqw72*8v)?G=a;eofw@j<Par}slkE+$?J70BOclLM<<`S)@sXlSH9+VICv<=~IV4Y=
X7)qQG*Ac;3N&w#mB>x_rDcmodd@+;#g5m!qz}sVoIw=nvD!L=RMx{|u0t+!+dGS7d<#98*Dv3?rYj38P<k`*KBk~0{D{>6wgcrc
8NqXI<%-U2up>=!8pfJ$S<zvYT+rT^$+v28o*D)Xd^y}=K_`Rvc%!<H9BCDvS<+38?Xy1Z3${p!Ii@<7E}imlqcf?l=ZUV8CtByF
ra#+ay>(}=B!rlfd2Eknp!ZJ6!3QG9y0-^Ed8x?(+@s@(z=QcC=~xeN1DE;Mqii|Qbhaq<nCDDswN6Pgl>SxUiYXg7lxdS%CPqz%
vK`z|CHGolV9o$M%h<o}nSByym2)q_);(>l72RG+sA&dSN~C1KP|J5*&rExV6peJbaR;Y|=i0gMtb?4sb|84JFMRFM8<KT}ovaZ;
e|}1wc2qDDoG0mn%_5|(vKVj($S#9^MnERVND>?=kql;;&ZXt^nCsi}xPhk}uvrSh2dWo3iqw6mOH~nT`7ZT~lZAa_009lQk?Kmp
)M3_?OCk|5dN)W8MG#ufFl=#X8~iBm1l_`!Xy@JJ+dZHrT3yW=+@oNIS+5<U5f>b0h}k*x0-9UgdvnoXV01cGb~q3R##4ken@J}W
`?HWIPq!Y1?&yJq`A`mcR>kAR!X6|d2rir28HMfEDv}o8=8pkxAYa<omg8!ULT3p_4J6_=HAf}|9y}Z|1~cBWl8xTrhtlyg1hWll
@IlWrrD{q?WcDI+qNcNrc8A3p7_oKOfm1TdjV@c3l`)z*SLjL#79$Rvk{qy?UN;AbRnryFFfBf}{=%k=<Skm5y2%y!*A{rOuo;te
0}dlgdnxGSV^&{aUVA^^nG!MPO^W$&FqLJHGn!QglO4S*W!q21n24hl5NaCJIin#lrI@BHWjaaA(088_8zLd!avo!fkp#k4Y@$T$
*s>+5GMNbOxXsTO*iwi*8#NrYni5ZhZGdj$KFol^cBOF>H520WB|JL|y1XI@s!@e)uGrfJyqP0w)Zy>~P%8F!F^wL6M8286&1710
?}_pk4j(J~?G)8cHG11<<wv7p&8;o$=qZ>*=|Gm6+g!IXZDqn5`M|!H4@^>p`&)HC^L_JP;%;smCSlQ~%w1*-7k(%87Un$ID^S!|
A!XG<T;X=-UW;%L)R14?vmKQ1N>~*tP5I)|+%meW3ptqu(j;6zBNb*TtOjoU4Rm}^aI1;QJ<4>=04+3KOj4jCoLF|O7dQAibLR4x
qL?Ey(6+|(GD0BFEtIZJFoTXJU}QX|29B}3p1hYl$8|BE8}}JoteMGk<xcWk-I)g^-6w8K2Y~O)$40Li$8!ygU-cJS&^L6BU6liB
s5b~^&<^B)%^kqAht!3I#FJFhn~Cg6&hUR!+_BA`<Mb42QVRdjH<mQH-O@N2v1=^Dv*0lSYUGxT&gFmwb=liU6_CXkd}=)=6a!~@
0R^U;wV9q%bA!0n<rLEJM<}tNWKi}3D6g@5AMC<2R6Mt}YecR9Y$_3Nw_I&^$bE~R35d;rNdy&S0O{G8zYIqfrgXuE6lQ774PTKX
ov@b<jv#6>d}%N{9$Uq<B)T9Q9u&Ys*t~62uF+QMErrDL30)TmN;wSZQPb_}>=GDbKY_790wa8LwPjp0DalU!VJ+x`kX*W+dkOS>
0%qISb|@H+X+&;|opoj476*Ho>l~IbL6M?Iq!Fs|8ts%jW~F(QIc$-{T)8d?U-LXc9*}~$;9*&C$CO=~c5R+J%!4H-5~kHp<QTes
jv>$A!*+|@Qg~@saBG+1p8_7eGNtv?GAn5oo4qq&w7n!M4TO=A(c%cFB@+yhTv(+YKbn77r2Io56VW|Q*|`z}lPfeb9+`3Ofk&W&
X-?;iN9OdhAfYoa5>dJ;fkWM9ACvdoGsh}&<E8DGsd(U_vI1dXFoA3G&~tA#J!u#kL&KJETrrl-*>rj+sH3m5U~M}(iTkh|&rXOT
kXLbDiKDp@3Cp+Qs9<_=&BL6qE7SHYMauf3=Vw%P=<?2=X{nxOeks7qxdl5=8I=~d)GR^zr*N)=nqdUXw!PSrOdI5f08c@TcXpHo
F13(H+NLbXvP<(p5<Wp91CnA#Hg?#UW6o-%m)fV4QDoy`D_7un>=2S*ModCFCGex=EaKo09${$cRrR|LkGVTdNHb%}_ByMgFLhcO
17|`=H1CIV-Gml|MAczwijYTFrlyJ0eC*qDG!}K18g;C>s&k}TDBL3#j~N1FOcP3hxp>0iIN6O^<Ry(l=e9}iUWdl4hqBx0R-{vz
suXW85i@AG0k*TI0pAOpBjafJD}~nG)-6}3d@`t(L1V6%V0n`{j{@T%Qjvj!z(byx!{F#qioT<0`gtr17r2BJm=|fQDbBEC8n3zP
gJs;%)GCQ|EQm<GRS>!7v6uR22X5F-n95vHHr>6{$GDUF$U~@Xqb5%RaNM>ccENzF7?U|sQl~K|U1<bRRo`Jd;hd!tJ7&5&Y}P>P
jP{fcdb6Ym?E;S}Q!3J94YrAlb^tEHW5L)QcLM01JlpN;xxT9Vt3k@2BQR$sD{@8(gj8$#!+Lo|JnfCgwK&(yWu#flBVsI<u}1$H
;d1F@RixgT)z9ECx=~fzvw2)mcDV;sGF_ff2|Y^bOM5ZpcUfWpgcLn`c3LJ@Ju+QFQv#AQcHAmLJJB}sM^d>%&$&0iT(M<JS?WtC
U29r(*73@k!~`Zdh2sh=BhF5gF~)B+nW%B;u<0CbP|LLQ$V7yU(-p3qort(i-C-h30vq%zd7pMlblxSOY;&8KXh(yUJgP9a-42>(
%``2hh}$;&6b9w_QyMocdF)R*y1>rTjdkjiq9i-|7%98Gd@~>F-ZZMz<6gvuXvDi-s+O8M^isLbw)WIJmce2<uP!BHIAl`>?tCwL
=-21A1CiM$IAT-%*N(f6kyA-`Ooe^q9!W*cc2D!*671DdizZJ4+zt1sM;So~MDglDkEzN&Q@N6PhQ0fANAUFL;OykQIt36k2hwqy
s)zSEIjtD0jLGp$mw&8qgeKvUWy;&B%RFZ_$McrFN^hzsmOv&Cgv)?%*G|`nH~=ZfQhJ;*vOPxtd-Rb%sE1KOz~fl=2Ak^Zo<}P7
l12j3uIL@L+yJ@<nz&7=!f~#i`SIo;W-P@r)Ujy<z#BWBT}J5xuN)kbzO-Z0lTV&=i6Qd5@(8DkoqywL4B!C0xb-hE@?(c(n#&(g
V}Dk}>0b>xA458&C)FWmq-;lXaoTyCjz0oWg0mW;PHqG8kU0&*hH${z>FzmA7EN{K9{FHfui%qIQ=Kn|s9O)|VN+fDR-V#mVzM4Q
NgggGCImz~7a-CbRNzGECXyO?&K5&6W!yS?lBbA1tOC&^HFWg=LwK@^y4OHKr+GjhMW79c4;#9?Es)^30}*?9d1`EK`@QLE4NL<L
=mp|LumHK`F;DqOcHmN=r?oKj$<sUs6uFJ<?+yh#POeVb9J!%J&P(74!bM~yX3j+(IMQ>aQ3se4%r<{flwp`WLWi4qfO=!9Wde`8
s9=}V(?ramfhQz(IrH0q^_??!f^GV>EdXUd-NmQVK9IGDr;9GDgw{X&35;7gH!yvjygniA5~7u3$AcyJQJqetwF6d?<DQAGHFL;(
7i}#L4Q)|vdq|toZ2zK*KGX&CY6wn|x69q9bVs?`_Wy8eS{~BWc|@3+6o_!<kTE*St1k7%4mR-iGY5s+ddo;R4bLF9#N(Qo5lD1$
)g$kciB6ods6G+8r|B+38UU4-=hh*mQ+N%Lm|}6HU|u1!3Dg@_QHSQ#{dpgWG>+~m%jhq-tG1@S7<sxp&e$cJbH8(B;7hkXsliO6
-s&;A*AO6+_ae{h<yo9KlD<LW0~6!S(-W~Tu;63{?pR^$12C^hJ2@TPNqIw{YUXi4%O4SWJG3#U&%h1^A>xiWb(gspIe}tnCweq#
FJ|%-k+Plb(X{9@H}Muo(SQJ{tF(!T@kh@PNa*qdEYHGTR+?WGc@|B#)71_dAS?41H-J{@`{8+v&O+|?mgvfE4~RJdm?m4s?XE&+
QR<@TlHb*LIf!-?Kw0;oEfSq^)G>A+7Tf#~vx$=Upk-f}ZA)-tA<jy%7*F-#%=pUC-S+q$?E1qo*j#?HW7Xf1l5|NyA40<%jgYdX
0XlIkCOSzWr2C-LR>X!`(>X)?+`QtLz-7lXb^^X?&=o8IPnfl?nhUPVd5R0HTBbVr*m=dUHHq^CZGkiI>G?8a5Ill_yq+~hluAtL
Y#UWDpO58#mpstb+fH*kor0SJk?WvYW%x~yWT(?Sj5IB4XH$o_sySb~Ug#ybuw%}bkoS%4>G3=}H$rFDgh$w?7`f-sDiO*6tR)X>
U=-OiX}gb8cnVIgCsuNYX59(g!1EOd%(RxnCQY7rR4_@`4i<qDY?xY5CpZHzX|&5918MrsfwJkgg?4c(LTtZ9SeD*jW9Mc->Xs#s
+W{LqQ&o_rqr|qQC3x}lCqdoiz~VI#jhzH!nK~7ZlXkZ8kGx`pp#k{q-k)e2c`3W9loJE<o*|DWc3Y_+k?2COSf%+XnE;EOD9rl|
_5(l`?p3VIow!H~u`OJ-H%(*EjU52Xgif9hYN<7z<0SA(hJLd(^qn0Z>zj0JLqE1(Ggrh8uCIEzA~Z;v-LStM7t2(MJRlXA=kzqm
0Rgt42VBR?rAhX&_h}|d1l5`@(Up*sIYV$+1)#3(w%>x@g1efbvdlBm^kYFaf6=1p5{kFT+730~&%D@qL={uCDxyE6`f5DIc6W4k
7)=bb!|bU3eCuosJUswvzUCGwBx3L|b<2=SRe5Ttvz>x94?+ocd~S@rZP!KK4D^@9zWe&WzHj@#1f721{AM^`Y_iRZ_083MGkkXV
Y-GP*$KT*f<=L}Q?`NaakCxfp(P;4Mn{U4Q;`gt9_~Prg+n+PbVc+vWJZ?*74ja#t;9Z@j+78pCWmzT1fMYyuyQ4Xs@I$8oKKLBa
1W$GF%$D`Uhn@#f+K;j52i*xl&r!?*9aq8X6Y)mtHJ^@rIx>+WvSX1Qi+nD!M+K2`5%|HHMae66tYnoESg=GFN@Vp`NOG-+5&1|}
^8^0bnx_TTQC%E$!3%oR>k9R1n^~U4+OU2Tu=zORZ-IJ^)w8`t@CJ(L<&~$oV@V@91J-%L)hbz)c?e=LT5ymJ;Q$@ghPI9=!`R{7
&RK1orz(rh_v!Cc=tty7!4Hnd0hKExVQOOFw7O7PagExxW-bQ%T?RXSF~S)Y?X{5vSMYsB;8nDp+uYk)u)#9tPFEXGY2ztvPD+la
G^?iMq;TO}WtA%HM3v~*`dsl96(^y_nv0a?2CSN$tBnI{{ElDEou4%yY<M(1bNCt%hUg1q)#u6K#*MNXDbtgT13w}QOI}s{tpPr-
;YKyaYi3#V*o$Dvd4UfG5}XeuV(C^Du17&TS{4glRQzag&^=F4FFf~&>JLJQje<M$)RmwDF`anDJ&nGMykuv~iXVKUf~*kK#w(l&
U9o-z>hYCHfC_BoD>Gs_*P@uPRadzQ2c`yI7FMaWVoSBD*+vcG@r?<bhLj=V6-^3@;lo^+4SyS{DYa{|Qn-iChnx)rGF#xng`A8M
au8O?Nmv3AFdHG~0D=k2;7q1D%xb^}HTj5Et7It$5FF1e^gK@_@Jy57y<G<Tj4Z})0)_N544$3#VDAvDiNL-G9KRHjNDa|Gao~9n
GQnNzMPN$-ww35?yav)$Kasg9Xofc<KME7oI*TD%JCW@~o(W&%ILN)Qb_%vr@Ye~7$Scr9D43uv=!lmT3ZZDw+mcS?Ak?VqQS!iz
PzL+7sVzA+l4T%ShSC&ANm(TzL4D+*0_BGa6cQ@-sfxTJv4zThV6L*!LEP&nghQxp!fUQs?fJo`>WE)8sf|{QZbQvZ)tslAhD~U!
r3OF$6&jCc8}+J$CfYr2X>B;ThNonNre;<2C{k6#-0{Qn1JoaLdeoy)ZxrekK8<<BO8VoFG1usiXjM3PBBKe>d42>IV%egqefe9m
tl~#~n9E;wMF?6hu&qTt*b^U2U0YX_oVB>LVm%T{KJfc4(X*X^W8otrck%(Ej%qvTJx)ywHlzT-8Uu5MW2mi|Ek#aF<ftM!ESge^
G4d`rEXI-_`00xn*`o+zj0M{%Ag3aUIu?N+)}x|eosy-T;{s{Gu>h0B5~s<>l517s43=1Ol7*mgRq%?m6G_mq#D>;bl6GRnb}G(v
g`@i;={Z(htctx6a+W2j*h*FN7Q|1ib52?9@VG&lSli^(>`zUnOsqLOHP@@ItrWk<5*zl1q#PSgPs1NeYuKNr;77?quzYMd$qhG$
7P-QD`M|J>9Me<e{AIx$YgHH}7rEiLys}4Y)@sskm8h;pSBb*@A$YrkYo7+R5T(BgYoEfiP{aSTs1}1Pz#^*3A0pd=50U;7%mp`;
SQi7kGyzNS^bYbxRiP|BP5{j(6pW$lVqxqfRM?dN&j4eP+W!_VCVKsQ@ED`)Q1SynT$-Ca0pl7?cKF!Yr~gejna5;3g3BCBw1*zz
W)9*P;B&#>B{AImoA7eUur*ix5qf@zntu~qw&Q4@Le2bPkR9x-+N49!IX&nPfHdK)<0&T(@boT_CQM9t+97q+@U&+u!J--oR{t8F
b~rgZ`aZfQ3{M~%d3g`8_Ai2LqMW~jwFz4PS;&po{SxrTy8Jze{Ts3MV^Hmz=1EZf8^N@J=%>+h2b+HZFDIaEn!!=c6%IWq9G@y&
;3c$N;V3%oR|g8y00n$}K|X<P3lD5tcp%ck-d}KkZGod?3eO2G?01R_nsJ4%*#O%KY$vdtVC@99L))$(W-mg?LYzWasOpfvngdj*
;*h_95=Hdp+(=FiEN?+%Q$%2-g2<+bRFx6zTO>VVfW0WJH$|{dPEbJ@P!uJfs_bsfOH<$_2S$8Tl%SS^_@*fFt7%19@B=^QTa*>6
*gTgQS%r~RI9;fyAQ+3vx>H5_ER_6<N)u8F!kePP?x><dice817%kMYl)pBpnu|`HUexSL%_$~IFNo5M8eCsAL?jI$QX%9oO%m4>
4br{~LiD0xBMlpApbClxrx%tvq)eGRegM{#IR{kck(UKO&`e2yUgkAFpt4E_-B&ut4<Pi?;Ski)@_I_1T3*^INu{w&>1zALnwR|H
75T)lN+aZwKOt9o0s|hWQ))O%TJ-D@>9|D3SXNSemT<hv2Sibcvk2rPvI<$fBpsKb;s*y707T2ED^*7R402>Ek&3vC>`b&~RL1J1
{@8XI2|`O^^s<1}P!{|>@v=Y;epzsW3PU@b=7P->G#bjH=FNsbt_B%I5d2SjNXv9o=s)El^(GK=6M%mgSpKt+vZP&Lh<^uPnk0D&
P5w4_DdgC%IZZjozXlF#P=11llu*CoLgl1CK#acyD*ki6Q;Ni2@}d4ZR{RAgYUEBrqOo6siunVK_y80_KKv3WWXs95%4EpD0}%}x
R{UUM<ll3wQn5dDu>K~`svYo_KqAC}qm*@Yggo@LIzxsA6#2`d4;-&K(FrB0rwr}T<FC14aX_u7X!L{_o}$rvKJW`JTKrPN(~epL
Sq}gvb^!dE-_{QCG50OpA--Ubb^s<l#|c^Px^2zF+Yl(`|D5+Wd2N%s_J6`p`#<HM#m_DUuJhmX&KC4PKJ?DkbhwhulH;l@seVfs
+@&!~SqA&08ZYs?zhwy@Sy@)BThqp-^QPpimlYeT;4CStz^lj)@=;lptV-oe_f1*pkKmN%h%9SopKPb*@1xg|mOSaMl$BAPT$_Dw
QoN=RDjNu)vcde8<hZf{8ZDd1LV|$?sI6>3mSqFqR@p%PRy55k<HjmSf2th)sf-(|ykMo$E-O~5SqX5d;vpRsd9>mY0u?=xm9T0q
f7KCL(GgjZUn@8wD|*%|Q?ZpNtyLaisUjCwKH6P6G|0x4XFK$-S422f0RF4!UayF7s(`hs%oAA!c($rgvTCJ2?_qApif+h?ZpbR~
N0g%HM^IX+h;XV1ykA8QDxwv7)~m>QDY)VlT|QO8G10SL5#Lk=`$92ai6oFYAx5tXl3ztSu87gA61xwpl0%}fs7j!uid0+)6>C4s
npe<`6^Xc_N4=`RlT`(pspx^MD)yx+`N5^GuuSwoRz|}WJ&;xH`4Oy?&D10r`X8&BR$W!Y2VT`kt*RRK#t=f)z~xdk6cH6YkW~Y?
Ur~otO=WdCI}K;21{L@HhghpV8l={T$oPMUgb52exDE^vrXL2a%U^RhCXD#M?RESWi1^R@9w}UY-2+*YNd9O1kpEj)^C=(YZ$X^@
ls7T~PO!ow=VZ=}yMf1yKOMXOZ7xbfp#{@?e;XL3%P_ey{~`C~uL4$jF%xe6CjhItG;^MJ{|he72YB@#@oDbj)tbN9-Q;j&I{Y;V
+jn>F!r9-1WBH@iyEyiNGjtc#7D(azRiCJVTMzvA8!+xKxJ?Olf6aMn*!J)HPz~?`={${l&7*4Y_m>^3`A#mwlMdB?6bwH=!4F)h
|B&nSDV+POuF|J*t>M|Hfo$g}rOvE#cvxzNh-(#0@;BlyL~3oYtj^8jk=OPhqI@-e@Krt>KLE^Xkx^2^{7*H1q^vewS6feNZUL(u
v~^84YEAD`?b(h;J3g|kzy(li?eXgZHA%2$h`0_Q-P$BrO=MOFj45DD0c%|cfS8&}ur^#)2ad?3S8Z7jHJwj&L|-)NLH=??RD*S_
_yIXu(}h|W%Ir1ivo1V8;03GcJ*`2eH6z1yQSpOwQm_q@YfV&E6P48^`cYyy8mW=L>_!P{s7b&z3AiQ!*A@L=bp`)dT>)j*6(_bT
_@PnZx~lM(jWC*18zifl-%vBZp{`*t)fUaGIkPoqR_R{;vXvUlS2t9_4P3Z2<H2=fI=G4KAn{mjnzU{>Eo6q;@K}@U+%~y-aT^dW
k|tk$^UXh%G`alnIBjzIL2o@wliVgy4yLp7z4gbdyV-g(TMa+Wrn5!%VK%?G++^#`YBs(e9S-)++D~7sX6wuG&1`rew$bQleK|kh
v~Px1_507ic=N+(UmiXhuh+BHW)Br!NWt=Yz8G(otG0DV>sAIZ#I4a_Z`__8A7=T<!TM-|uTH<t@YU<rDZYl2qjP+TCr20fQk)F-
u6;Y+pBzm0r$^U8zwXbT`~B(u`ToVhc>hBFPUQRf!A#1g@-FsD`Z64kewXi!7gJnZ`<<&GSA)I9?R9(Y_lM*C*@3h%I*@M{@~ZRE
{=V<pTHL%CUtJBQ^1qMUHXorCEnKa}A5UjL-;Qzf<;!s<?GE<NXS3<4jDJ1k#AZ@=y%|s54~J62Yo%;_KVP>_)@5%s+uW`edsj2<
a5iMeGwX6@owfCwNO$Jv^T~KKTMu8o(iM|8%+~E{x!lN0aWNbnt*+bS_3ic0ee%g1<T1}a80GAci)QVfbmP=6tgc6Gt6$c$&Cuxa
si%Y>+qTIA=0a!ZgUs%OIuGAG(7)^3o15io(;nk(yE(t#pBznQS68dqWVxEI+vAg?v#aIg{kqMMCd=9R<#>JB>YuCm*$bgjQJ6AT
nV~0d4A8W;myK_3*7}N>tkP^HlQ&e()7jfQTi!18Rl_&Ke3ZQz%93RA-DQPdDboFgf`6{|N%zX*{G^o|+P{}C1ypDSyLc`-bu>D%
dZDZL@4agOZnd<%33z!b{4`rFgu8`gj&HUT`|1_G-(VR|GB%q@=SKULK7ZYUsb9Xlm`sP-5_$aSY_i{8A4!3JoC)JjI?*tU`tb8%
h$14ijkG*3Zf~YKze@S&=jgdeujhIt4avp-T|67Tm@OvD=}e^3(Uw(G3)$I38~iZeEM`KMN(FLBN}8^g7=^B<E?y$s{F8S6iP94&
^GK+y)o;i1lcNu<^1&S%c$eKJQan0qg(?3sTP@e!V9IQiO*bEJX6^Fq-E5+QYwy8xhi3=v-Tv9+_{EDC*}LpeyS6u-wki%~{$;K9
tMrs|I361>E@s0D)V8-bKi|_){O)&p`#&5D_wKbf*UP(^mJZJ#9kP6Mv@3w_rTv4je}C*xp6iE5(R(E$5lL+3Y^Ry6)baaTFY7&%
X;C;4;>_`~(b06e-+CFuv0k3EURzvb>uY&&yHy)!*>swH$c*Pk#-GpI#Zk9lFJyIQi|KI4^~xwirn8YgYAu3h=E`?TJWbQOiU^Pa
ti~6!?aE(|*Y7hGaoNpyH51Kvt0npb1Rf@F-Y#bMBC@POy(ury`PRDsvAPy&Xj^=YvbW2{teah_yWU$YH+x#DO{ET`k<3BiTfvmd
r}N1MMBYNmm?$y+>MKNLDtYEg1^0ZpShw9|Wj(=tDg-9HAgv13r#@h&ZdR&IpS}L`tKa`{`uo>keRcZHtM9*mmf^L}KK<(J-~ZwJ
)8GI2#~;5E&Hty@&oVAcc0RwF$>Obr4yLo!Dm%Zr6+!vK>UK8jguY4GR=`mq00r_~S%&(Elx)c2dlC6!1cy#%VFFa9gWdXLS-1F$
9<JNo+-1N7r~TQ1xUnv`*7KX?dcK+8%}%A#a<y*5zTH?$GmEJ_FVv_Fi0DYqm>3fEI2Rf@r5<QI$#glppUy9YjEB&w%T=mj#Jp3%
wAAT({ugN1q_#{CpWj|xolb7gbj@xz^TmZJ;~Syq0~hvRy%I({es^Nu1HSvH-wXXtv9gs8r78vy<GVuqW}O`m#qu7BROzTyYP3VI
5(`T;c>#$mWucQ|gS~&-`{8o7cX72m8(-~d7iW97LT!5+DHU0~ly|Q7)|2toct!lSCk8NhKx<4sUI`h_R?pT3?gkJ08%BpF15XZG
pDXUVTt8OLi|qP3?@13GVV+&Cx74?2Td(Jw?obq==DHmY^)RTBsw#Y_%`FmZI=c|s5~fNtvmjAPM|QbRmwA3YZlx2Mt@Y))zs$0l
lPl@T-WPYWc)GBs!hrM5>8Ze<tMlw?nO)9X2#Z54cyYB9Bz(0LRIFEW&q`IyTtbd$<-OU}dbamwcscJ@&FX#9+Jl3=|0A+_GoM_~
HkZpOU%osa-j5D#ChoP(`Fbw2FkVb%!~5)uyAfOd;!f(N{*I^9)ZOLiaLE@)OVUYeNvhlHpD*Q4W?hhrOO<S=rz^D4T3e~%#q7cw
?)oGx9oW;^fwkFnWPN+q>xey}m(LHjeM*&AzgU~~_)MyOeS7swW4sff%Z}`C2ZsykqxE&aKWyAN>CKHI>^l(&<9qqweBgbpy*G7Y
BVuzpzx$<*B!U(mT4JRIl<2FDdSly{*SVMIntt>qZ}qtKM|1KLQ$jmHaLd|@HF4I}8;e%oKU4iamOt_>KVj9&@wJGQ;YQ`t<)xXM
?qIsy3`IGQw%G8SuU@@<JvzF%u{!ICboMg4u`1c6R{G2QW{8T}<)z>^;X|u@dp5keIi5dvCz*bpjJA51GDBGRNbDuR`ZZx4YD|HW
hAQYX<?=l9@(H-KYIRU?kYLz+7sSh>GJMtRHXpOuv6LMT-#vGue-9@o*|xx=K$WTXA!%^4Z=`4I2W4qg*F$~5KE|e!dtaM8Ievfg
oF(s5$-9%$OaH`}QS^RW<gMu4PLXu%YJ6>TsXdf|>wDFd@T2D_aa!`!tbV)WLpWI5!_uXfUay>8J@MX$&B3A&4SP4cw?=JhZGDGx
o!TO;ac0HuQo*AJi$|lC5|M20z$v=$^UNCU8N*NmV$uoqE!8?`Z*H>LRD^arn`Iy({iEMb)x?IKuwG|LamZ9=-?rao9LRk0vE{c>
pCe8$ZpQ*hh7%>VZ`;Z7vu~e?T+lDt_%l!`FS?gJJK5UnbI~Aj`|{bz=y|&6UZ{n~E3U(KN{q%&^p<;c%i~sR%Ep3*zSV|uK@-`q
`#Rc}@6w3V?*}Lrwnve``<Ndn?e4TAuU%U;`#e~)wf!|)LU+K9>-C9An&oPCnq<gl*_S$5@7~e7@aoMQp?_tHFQ1?;;o;|T|Fiw^
`T6Pc{CqvzNacszAR|7yY^B=4yLV#N5J6pLa*>}rrvaVkqy5Y507ZJk=?x7mpj^LNodewbMIiOSD*qKsr5ZtO-SOS*N-%=@i7uaV
JZx=Oxt&c$k9-$Xg)nc12R4dK-2m_g9I*S_&X3GnF~8TTxmhizw~DMWMXnrWtJ%$LEC8qPvLJg38hI{2<3M!D{`{pYv)(oMO3I8W
vmx-zD2eg;eI{KL`7xQaot8kOqNet5dYXZ6geh`y(LUrK8Tpmk0DShs;7|{`Tx_Aso8bl9z0h_qF1jU9b3<DZ6C)JeDxgFc;3@M9
1E8^mdZQgj)^-8KXvrIE6nC~wjrKz!rcYDmyP^kF-*XK;q#Utp76PN^YKSB-+7)%SOV1ivvk%)!eM@B*v_4s-gRi@0%FXghOpw_`
=J`TQJz3672y(W%8;g1J$n*jnzP;wcwZJ__8E4rY*uGaAci{K9TPOG9rJ6m$$m`)xN{M1uwCW~I#GAd#z}l1L^_dPwO<f~mo%f%F
_yZ_-L4^&a@{=l$pE_molL!f3jzlmhNLlc50N;t&3;+H4yRQ#L(2Ci0tLD053D)~KI=DnnK58$1I^iP<?AGhP^H;7u$@@*nKwb#;
9iFe2f0-?GNXaenz-=f`YLjbqxoowSJZ@&;SVoyGSM!VcLI?V%R$2b&OZ55ZhxS@ct{L5dUwlS^u|-1X^Xz;)neD#u4c(Lv#HP!1
Lbditq(5C@vWS!R_@`a1qE%FG;`4p_6p$uzcY25U)ma~>PG{SNIqS;wYLc!-qnBkTH}8JeDs%4L-L*sB&(IISQ@8CFLfxfKk)G}z
p#;$tN1IKnhU!Y5kT-VDH+$qzZeQyfZ8jOJ-DQC5dwYL+-cIjilJ)MFnV{C`-OH#=jC9Ji^oPu5UhasIxY>+s?mJN;bN?%Il}+z@
%l)V9%j^ewHj-C<vA$go|D1iB{ZSWVeKQ^Yadh<dZ98Aw>9-V<xE}s7d;3-d(ifj8%>L`&j(+}G|K5xz?>jOOK=e+u#CdiBN&WiG
i}_}Dy&iUSATvzF%!&ew1uYBwlJXO*=%0_rC)u^U87uea<Fk`Yi=bt8ThNzeBA?Htg`a=kw(zaB@b)d5_*R?vwrfJW+s&NfzKr-!
dUBFUGtw$PrQH*K;K$C**Q4MZoCLS#CyX4xoXMyGZ_=Pqscq*%uirn>O!I54{QUFdRt9^Yx5qQooSD#5UHJO5Oh+|J0^?3a#L3Zz
+4%i$tS%zq<OmLBc%1L$n)Hi@v^Fm9O`;AU%>)ALD-L^l>w7_y^6}&7KtDd0cKxny`eQ3Z)XK_S&BoLD;v%`o_#xz$ecyhc{n-AP
ecpbaY4fLq&iXae9*SnUU2Ix(HoIBPuc594WJ@Qr_54Ca_w8!d4%wZI-O1RUqzcB9&8;e#r7Ekd;m?_2!=GBJKNbByca+~(9Bup8
t(-llC^*+ydGr0>j?Tv|h3HShi2||Cy326VwRS!}J`5*qdw!;$B4$PLY+9BcU9_-UrEGNc=bmx;F*D>r<sfZO(Dt7*70%nXC-A8M
3Ccn)+zB;~T19u1CMHYt9h*^-ECT5$mM-Kyqb<vC>q=w(L`E;|9I1qm&n;s4OeU*s%YD9=y}psMEe88i?#sx0l!2+eqE__n&5rVT
QgiI;+H*z7nSSOcoyI+vj%^G3dY2_fpSPC>EZPFL&jHI6fN;V;&lX~dCb6L9sswI2IkCttAw2AHWm&i&q+)ij7!9CNhj31)*t`3Q
Gj)8wJH$T|Hw#SL!6Ec0Jb^-*1VF|{7~k$_OZ6uZGfbtmG4<+wD{@ff_;{3k{q{99j)@$)P^5dU+pg2MqeJuvfZ~3;!t5sc`DaFu
w@mTvE>pZScgN!e-OkbI34!{z!QRF4Y6?Xtofh*<#rxL&f{w*v4c&p(RD#U#<xsxu*a4f-PAL5`<_9eA%cYy~YJ9D3`E~nqcBg^r
$!vYP8h>bi>M(74k=-q?WI*kox+?9T#ZJE)ujXniD0hfi|KZg9?J7)f0CU%3&#Ok3qBq~0GeE?!emS*ruBj+YfxovJ2Or53i&GUT
B0li_OofJgmocB7YkyC-U6V2bYIxL7H?2So8+R)M9t=KzBletHbgnbqQn=S`&AAcF^oY%xWhE@U3^BUx^9P9ECUX!qtE`OaaXm~9
g|U$ao_OA6F}*$Nb+LW;02OL=qy62-^gPRQ)U!*qP>*jMb+TUU(HmKNllAN2*>d_(nFGY87st;Y&*!rfr8eH}&+0QZ_&f4D`s$+X
WaMSm^|Eg*TkJd)Y&Htg<gYtnOr1FIdbn8)zY=;EvKQL@v%NY|nY{MfUT^eT%@>iP)7jN#+?q=v&rOJkLAJ?;p9?bDWx~(jKrFmh
K9cDYHq$x+_9j9bpVOU^eNOjE_Fk2kv|>(~&*^26V#Sn0y^HS|y6{}Z$$8fzgykP~TpZdDqfDjHTj9Ly2jSIr2X#taA$qffRH|t^
ljCP^pPd+jgJ<?z7*<cXW>2<~S=%|*;h%hxQyS`p2<XFph5W<}DqQ)UtH38!iXZmGJ?_m<EKg+T^^j}-(&~$PIwFS{KYsS(vy-jy
j?2;STF)#TK~QjVC6r@TrEH6Io@t0YnR&g?t-fwEo8q+qOXux5*P_MWY`j8nQ#+oCs2k50v#G{8M3$;cP}*q!fq`XQv3ByL>A1XI
o&GN}+F<X0i_^r+8ET|1&kj_0z{e?V3=cHrSWoiNrbMC~AbUlMvzQ$?QN>z@pQEf$!+B{!UX$m^DaKfUqqORZ(L5f=a@^F{Xmj#6
s{<H^tli_}x078q7As8ISh%+DI)5VydyCTh$w|U?N58_1>%@%@g-*63a)ePIN}<HKmL<{W-t}*1-v_|zHxlHQW4G+y_n@tx;I;Kr
%(niAxlQ!yYI8bO6GAY9a8mnrvcqnPSJqE5%hmYeRM_#V<B;1nk?(=GRI8)Aw$pjgX;Sn-iw=sNvgFH<slUzc1c~w62m5x1Z~1T1
DDc?*KN|ALD7tTVEqAuO8=>kf{lAR%_51W*zM<W}pw$oAU3U9-Z2sQMwl@ARz3khEFMEmNzi8RM@4s5+QDzOHq|4=cwrH7I^U(KC
&(&A0`{a}N%rh18=#qZmNFtDz?)1~WCP(Xw1r3IY&^WAx1D9IpEDot;$w%^S|9;EZ!}0U8{jZ)+_P^TyDm#1b_vKqQF_o(py#QWT
7dk{2tm$nNf(L(>AKK`?IyzekPjrBp#k*NWe>B^%XF#&rK0nNQywxSkb}IDUT_d~rpwoLaSv&**sRN7SXPq6d{HTCVq%XO30k&@2
<2<WQww%3qinA9_aCRT`-?p;Wt*mzYA^S=_5v_Il=iBjgr3nseWZ;}<Hif6!ui13hH*WVbSvJJ`P80VpQr>IQh~{OOFBSsIiM+}0
JqLZZ1IS~)T(ESJGsLM5j_$ce^i;39b9UXe7xX##QUMr4!OT`a_j};k5@Oh92%v$Y_tCvx#Kv4x8=v%|fXaSmY*fdYX=l0cKPyms
O4b>9ZHXxBe9cL1e(~Apfu@o!C{TT%u2Sh%XKm?f{gAGr&{Z6DTHq<V`pp`nmqDRca8f`2p%-tyKQ2x*CARC{VtINtUd!bDn5Ivf
nXJ>?qE4qL<kpVPV1=Fbm|1u_zL`%trL;c%FyCB?c{#u0fS&+pPc#KAM|_wdor1=XYZd?6m0!Sm)>JnHu@;`qr_!tW=A*HMj&W!G
+>`6)dg~|auHxqb&H+&<T|A9<1YH$Pr6;<Vb?y|fxmZR;TUJn3Md4}zb+N1g=B!34$(k~Rk~(1WpwIrvKKmV-OKN#C`882Cc|>xP
$H;$6iVrM>qu!f^bJjA~rz!XCl!9ovxcYeNz1Ml4bfS;XQ8ZaD^F74UgN&^=+bkXdjrXI+HNNR;93Q{eeHg>Lkp;<_bi7`!L^2NV
UrZ8uP!aI3nZ?bE#T45Sy7p4PUTl^~DHx5Od`!cI7qeCOm?oM&)lrr9U8TQjN8gVQ?Hv}+u^!*2j{fa&D?{xHmGWpi^4(_G$Trd9
p7XrAT>v>5U7VgyXJ@w;nx6G@_LIuZ?A5FGd_KFH>IR65i}qr+R4)D~QuU|N(Q4H`nY4K{xojWhIKUIuS2+Xqfh^D4hx;$Ili1Aw
Wte!iefHzq*Wdp5>Z{XlUcdd})qj5d_Vl%@PXF_(uRoQtAN}c{+%wB$Zohf;oz$_b6y{~&>Gz+%%HS9~Q}@^K+4x!Z>`eZj$p2IM
e<uH*>*r?tYy_`a=TrMBGu5)5-=CVx?Xy(o<LUW)wceaw%M3{$zRc2GwHJa5A5K%dq6#|goMD$)njPVaj8lWZG9g^dX={th`LR5=
#q#`WIo_<vEq#H%LnWwWSnLTR+=&d{ch0`Uu66aR3o3j>e4x8bNpSSAmEDKC3mc4Cl*4!H<>JNk_WGu~lPQ0mzMp+uBdt19*|E?>
jR!j&jyB`f#Y~oayty1cyIo+@(CMvzp-ny`ziFbj)Vf2=;n~^k{A&8_kk7sNuo9*^J^QG1CtcBb?s-?Nl7P^u)e)0Lt)(t={Ou24
eE0hF``3SZ{q{5w=kI^~LH_^r_301a{rLLykFWmx#UG_qDfO#YKm72;?_Zz3di&Yw*Z=kQ^p9Wv@&9kzN>&?&f#}^|;hsXEg(PiK
O6ft7<yfFvL6S*tLnwiSk~D`N8tBLOjjU{LZ$_SZnnk0<egcATS?B!|YH1rs(payG$V&J0G`J_Gf)mrk>Ebe)Ct(adOornD1Z;pt
a7z7wOe}PYoNx%u3rh6%(PTV$d<6d7dd)0%deyac9!^OMI|~(*LzDQ&Q106U3Z+*zc&?P5RS+v7-o_!iqU%DTVhgUlsqlDJIw4#0
JBU{SEi}U8A;w_VMayC=BkJ55;Yhd`m#$$la3*S-`fH%y)NlkY1!qmnKvPfASRfi$h^RDTMnP!P#R5n(q=gQ(@}40Vl{E@ZNez#X
P4y;C!)C_*7?NZq>X|x&q=B?sZddVt9}l(L4)KZGu1VBK3#3(LsijVH7leE5<iNzZE|&#6yXT~LOm<9YSM!pp51lOAL~=5J0V9+N
(RR7n5%t>TH{M)Jb=1Fk8RdM4JJ;2TbePHubLo2Z{?Wr)wA|nn>Ej+vee>1I{o!l<xy$dS`9-<z4|&x5NqSkkE@i(oj2ff
"""
def main():
    if len(sys.argv)!=2:
        raise SystemExit('Usage: python -B -S recover_unequal_u2.py fresh')
    source=zlib.decompress(base64.b85decode(''.join(DATA.split())))
    assert len(source)==62196
    assert hashlib.sha256(source).hexdigest()=='c469ec9b127addd02fd2f1e5059b9ce63b8afb7d35f80b828f140bfe572fe7be'
    folder=Path(sys.argv[1]);folder.mkdir(parents=True,exist_ok=True)
    path=folder/'unequal_u2.py'
    if path.exists() and path.read_bytes()!=source:
        raise SystemExit('Refusing to overwrite different source bytes')
    path.write_bytes(source)
    print('UNEQUAL_U2_COMPLETE_SOURCE_RECOVERED',len(source),hashlib.sha256(source).hexdigest())
if __name__=='__main__':main()
```

Optional convenience copies: [decoded source](sandbox:/mnt/data/unequal/unequal_u2.py), [complete exact report](sandbox:/mnt/data/unequal/unequal_u2.json), [source-only recovery capsule](sandbox:/mnt/data/unequal/recover_unequal_u2.py). The embedded capsule is sufficient without these links.
