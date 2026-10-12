# minimum-0021

AI research report · 2026-09-08 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# NOVA24_WEIGHTED_CAP_7_6_AND_PHYSICAL_FLUX_V1

## Determination

**The universal eight-pole obstruction now reaches the coefficient cap 7/6.** The entire former branch “all optimized caps at most 20/19, with three consecutive unit-bad poles and sparse diameter balls” is excluded, not merely narrowed. The new result holds for every physical positive-definite metric and does not assume that Q has its own centroid at zero.

More precisely, let P be a three-dimensional polytope with eight maximal facets, ordinary uniform-volume centroid zero, and poles q_a. Define

```text
gamma_a = min max_(i != a) lambda_i,
subject to lambda_a=0, lambda_i>=0, sum lambda_i=3,
           sum lambda_i q_i = -q_a.
```

Then

```text
max_a gamma_a <= 7/6  ==>  P has at least two strictly stable facets
                          under every invertible linear deformation.
```

A stronger root statement is proved: in an eight-vector weak escape system, a root cap at most 7/6 forces three initial unbranched links, and the caps at **both the second- and third-largest vectors exceed 7/6**. The proof closes the previously surviving pure-chain case by retaining a secondary-row disjunction instead of replacing it by one lossy scalar inequality.

The actual-mass contribution is a coupled identity for the physical coefficient matrix,

```text
Lambda^2 + Lambda = 12 * 1 * omega^T,
omega^T Lambda = 3 omega^T,
```

together with incidence-sensitive overload bounds and a 7/6 version of the lead's complete moving-plane filter. Two new exact actual-Santaló controls have sharp over-unit caps; their complete affine orbits are now excluded.

**This is not a proof of F>=9 or a closure of an entire C30 combinatorial type.** The remaining geometric/mass problem is the strict 7/6 cap exterior. No physical member of that exterior satisfying the complete necessary escape conditions was established here. The inherited bracket 30<=C_min<=1374 and canonical remainder 178115 records / 4366 joint root orbits / 74 types remain unchanged; these are preserved journal figures, not a new enumeration. :contentReference[oaicite:0]{index=0}

## 1. Authority and scope

The literal parent identities used are


[Encoded source block omitted; the code in this passage is incomplete.]


The later durable `NOVA24_THREE_BAD_POLES_AND_UNBOUNDED_STRIP_V1` supplies the immediate comparison point: it left a connected three-unit-bad-pole alternative under the common cap 20/19. The present theorem eliminates that entire alternative. :contentReference[oaicite:1]{index=1} No mathematical alias, facet-order, or incidence conflict was found. The supplied immutable hashes are retained as authority identities; normalized local extractions of displayed Markdown are not represented as reproducing those envelope hashes.

The inherited 17 C,A tables are embedded literally in the new source through a checksummed compressed representation: decoded table JSON 5705 bytes, SHA-256 `34f501da2c4cabec97a55ca8311381a78eee0603c9c46c7c375a3f3dbf859af6`. They are reused as exact input, not as an unexecuted certificate. Every new matrix is reconstructed and checked. The already excluded beta in [1/2,1], T>=12 strip was not rerun.

## 2. Genuine physical rows: additional compatibility and overload localization

Let F_i have area A_i, distance h_i from the actual centroid, area centroid c_i, and pole q_i. With V=Vol(P), set

```text
omega_i = A_i h_i/(3V).
```

Divergence and integration over the facet cones give

```text
sum omega_i = 1,
sum omega_i q_i = 0,
sum omega_i c_i = 0,
3 sum omega_i c_i q_i^T = I.
```

The third identity uses the uniform-volume centroid of P; the centroid of conv(0,F_i) is 3c_i/4. Thus the physical rows

```text
Lambda_ai = 3 omega_i (1-q_a.c_i)
```

have zero diagonal, strictly positive off-diagonal entries, row sum three, and vector sum -q_a. These are the parent's physical rows, not optimized LP coefficients. :contentReference[oaicite:2]{index=2}

### 2.1 The matrix-square identity

Write Q and C for the matrices whose rows are q_i^T and c_i^T, Omega=diag(omega), Pi=1 omega^T, and R=Q C^T Omega. The displayed physical identities imply

```text
Pi^2=Pi, Pi R=R Pi=0, R^2=R/3,
Lambda=3Pi-3R.
```

Consequently

```text
Lambda^2+Lambda=12Pi,             omega^T Lambda=3omega^T.
```

In particular,

```text
sum_i Lambda_ai Lambda_ia = 12 omega_a.
```

The matrix has rank four and eigenvalues 3, -1,-1,-1, and four zeros. Its stationary flux balances across every subset S:

```text
sum_(a in S,i outside S) omega_a Lambda_ai
 = sum_(a outside S,i in S) omega_a Lambda_ai.
```

These identities are necessary for the one physical matrix. Independently optimized rows need not satisfy them. Conversely, satisfying these matrix identities alone is not asserted to imply geometric realizability.

### 2.2 Actual concentration and incidence bounds

For poles in an affine k-flat, actual cone weights satisfy sum omega_i <= (k+1)/4; in particular omega_i<=1/4. This is the affine subspace concentration theorem of Freyer–Henk–Kipp, not a new claim of this handoff. The normalization q_i.x<=1 is essential. :contentReference[oaicite:3]{index=3}

The singleton bound also has a direct slicing proof. Measure inward distance t from a facet, let U(t) be the volume beyond distance t, and let A be the facet area. Brunn–Minkowski makes U(t)^(1/3) concave. Its tangent at zero gives U(t)<=V(1-At/(3V))^3 up to its zero. Integrating the tail gives the centroid distance h<=3V/(4A), hence A h/(3V)<=1/4.

For any facet a, the affine slack f_a(x)=1-q_a.x lies between zero and four on P. To see the upper bound, cone a triangulated boundary from a vertex minimizing q_a.x=m. Every positive tetrahedron has mean q_a-coordinate at most (m+3)/4. Since the actual mean is zero, m>=-3.

Therefore

```text
Lambda_ai <= 12 omega_i.
```

If F_a intersects F_i, triangulate the polygon F_i from a vertex where f_a=0. Each triangle's mean slack is at most 8/3, so

```text
Lambda_ai <= 8 omega_i.
```

If F_i is triangular and shares an edge with F_a, two of its three vertex slacks vanish, giving the stronger

```text
Lambda_ai <= 4 omega_i <= 1.
```

The new 7/6 obstruction therefore has a concrete physical consequence. Some physical entry must exceed 7/6, and its column must have omega_i>7/72. An intersecting-facet overload requires omega_i>7/48. A triangular facet sharing an edge with the offending apex facet cannot carry that overload. If the unique root's optimized cap is at most 7/6, **both** of the next two poles require overloads in this same physical matrix, subject simultaneously to its square identity, stationary flux, and every affine-flat mass bound.

## 3. Proof of the universal 7/6 theorem

### 3.1 Escape trees and the exact coefficient polytope

Apply a square root of the physical pole metric. A weak arrow i->j means

```text
q_i.(q_j-q_i)>=0.
```

Distinctness gives strictly increasing squared radius along every arrow. If the polar has exactly one strictly unstable vertex, every other vertex has a weak escape along a true edge; selecting one escape per vertex gives a rooted tree. A maximum-radius pole is always strictly unstable. Thus ties at the maximum already give the desired second stable primal facet.

Put

```text
tau=7/6, delta=3-2tau=2/3.
```

The vertices of the coefficient polytope 0<=lambda_i<=tau, sum lambda_i=3, on seven indices are exactly the 105 rows with two coefficients tau, one coefficient delta, and four zeros. The smaller coefficient must be retained. Replacing it by a third tau loses the main gain.

### 3.2 Negative-projection lemmas

For a descendant at depth d, repeated weak shadows and log-cosine concavity bound its negative root projection by b_d times the root's squared norm, where

```text
b_0=b_1=0, b_2=1/8, b_3=1/4,
b_4=(11+5 sqrt(5))/64 < 89/256, b_5=27/64.
```

Indeed, to obtain a negative projection, append the angle to the opposite root direction to the d path angles; their sum is at least pi. Maximizing the product of their nonnegative cosines gives cos(pi/(d+1))^(d+1). For fewer links, adding zero-angle links only relaxes this bound.

For a rooted tree with at most four vertices at depth at least two, the negative parts of any three root projections sum to less than 15/16 times the root norm squared. The only triples not settled by the individual depth bounds are the six-node chain marked at depths 3,4,5 and the six-node fork marked at depths 3,4,4. Their exact matrices have M_00=75, remaining diagonals respectively

```text
(128,208,352,336,192), parents (-1,0,1,2,3,4),
(128,208,368,176,176), parents (-1,0,1,2,3,3).
```

Set each parent off-diagonal to minus half its child diagonal, and add 40 to the symmetric root entries for marked nodes 3,4,5. Division by 80 gives 15x_0^2/16+x_0(x_3+x_4+x_5) minus positive weighted shadows. The leading minors are

```text
75,5504,333632,15370240,434778112,56623104;
75,5504,333632,9116672,817229824,5266866176.
```

The new two-negative bound is

```text
K=373/500.
```

It applies both to a tree with at most six nodes and to any tree with at most four deep nodes. Every pair is settled by 2b_4<K or b_3+b_5<K except the depth-4/depth-5 pair in the six-node chain. For that pair, use

```text
ell=(1081814,1568749,2274907,3298981,2102980)/1000000.
```

The quadratic form

```text
K x_0^2 + x_0(x_4+x_5)
 - sum_(i=1..5) ell_i (x_i x_(i-1)-x_i^2)
```

is positive definite. At common denominator 2000000 its leading minors are

```text
1492000
2057811445404
2784606944230667192
2019854042353942830803092
2564678406430668704815146192
578053859419041267994547507520
```

Summing each scalar identity over physical coordinates proves the projection bounds. The programs also exhaustively check the finite depth reductions: 86251 one-/two-element checks, 102706 elementary triple checks, and 56 exceptional triple checks.

Combining the two-negative and three-negative bounds retains the exact cap weights:

```text
delta*(15/16) + (tau-delta)*K = 499/500 < 1.          (W)
```

This replaces the former lossy multiplication of all three negative terms by one cap.

### 3.3 Complete rooted-tree reduction

All 5040 parent-before-child arrays on eight nodes reduce to 115 rooted tree types. The elementary classes are

| Class | Rooted types | Increasing arrays |
|---|---:|---:|
| Four-deep at root | 30 | 2556 |
| Four-deep at first child | 28 | 600 |
| Shallow first child | 7 | 52 |
| Shallow root | 30 | 1638 |
| Height-four broom | 1 | 7 |
| Two easy long trees | 2 | 56 |
| Exact matrix cases | 17 | 131 |

The first two classes are excluded by (W), using the root direction or its first child's direction. In the latter case the root projection is at least the child's norm squared. The shallow-child bound has margin 1/4. In the shallow-root class there are at most two depth-four vertices, giving weighted negative bound 3/4+25tau/128 and margin 17/768.

For the broom (-1,0,1,2,3,3,3,0), normalize the root to e, write a=q_1, t=|a|, and z=q_7. Then e.a>=t^2 and z belongs to the closed diameter ball of 0,e. If t>9/16, the a-projection of a root extreme row, divided by t, is at least

```text
t/4 + lambda_z*(3t/4-1/2).
```

For t<=2/3 this is greater than (9-5tau)/64=19/384; for t>=2/3 positivity is immediate. If t<=9/16, the tail negative-e support is at most

```text
f(t)=t*(1+sqrt((1-t)/2))^2/4 < 19881/65536.
```

This function is increasing on the stated interval, and sqrt(7/32)<15/32 gives the displayed rational bound. Here use the **total coefficient mass three**, not 3tau: the margin is 1-3f(t)>5893/65536.

The two easy long arrays are (-1,0,1,2,3,4,1,0) and (-1,0,1,2,3,4,0,6). Each marked triple either has a four-deep ancestor closure, or its exact weighted depth bound is at most 1507/1536; the latter margin is 29/1536. The source enumerates every triple and every placement of the partial coefficient. All six elementary margins are strictly positive.

### 3.4 The secondary row: the chain disjunction that was missing

Root-only exclusions leave these five canonical arrays:

```text
(-1,0,1,2,3,4,5,6)
(-1,0,1,2,3,4,5,5)
(-1,0,1,2,3,4,5,4)
(-1,0,1,2,3,4,5,3)
(-1,0,1,2,3,4,4,4).
```

They all start q_0<-q_1<-q_2<-q_3 without branching. Put b=q_2. Suppose the cap at either q_1 or q_2 is at most tau. Averaging the extreme rows gives an extreme apex-plus-triple with nonpositive b-projection. A triple omitting q_0 cannot do this, by (W) and b.q_1>=|b|^2.

When q_0 has coefficient tau, its other two coefficients are tau,delta. The two-negative bound K and single-negative bound b_5 give

```text
-q_0.b > (14003/56000) |b|^2 > |b|^2/4.
```

When q_0 has coefficient delta, the universal two-negative bound gives the weaker but useful

```text
H_0 = -q_0.b - (389/2000)|b|^2 > 0.
```

In the four non-chain arrays, the b-subtree has height at most four. Its improved secondary constants are 145/512 and 557/1792, both above 1/4. Thus they always give

```text
H = -q_0.b - |b|^2/4 > 0.
```

In the pure chain, every partial-root triple except the one using q_6,q_7 has two-negative bound at most b_3+b_5=43/64 and secondary constant 83/256>1/4. The only remaining possibility therefore supplies, without relaxation,

```text
J = -(2/3)q_0.q_2 - |q_2|^2 - (7/6)q_2.(q_6+q_7) >= 0.
```

This is also valid when the apex is q_1 because b.q_1>=|b|^2. The complete secondary alternative is therefore

```text
non-chain: H>0;
pure chain: H>0 OR (H_0>0 AND J>=0).                 (D)
```

No assertion that an extreme coefficient row is a physical cone-volume row is used here.

### 3.5 Exact common-direction certificates

For each of the 17 remaining tree types, the embedded C,A table fixes one direction d=sum C_i q_i/1000. For every root extreme row s, the source constructs a quadratic identity

```text
x^T Q_s x
 = (sum C_i x_i/1000)(x_0+sum_(i>0)s_i x_i)
   - sum lambda_i(x_i x_parent(i)-x_i^2)
   - lambda_H H(x),
```

omitting H in root-only cases. Twenty-two literal rational multiplier overrides, all with denominator 1000000, extend the tables to tau=7/6 with H's coefficient 1/4. There are 17*105=1785 identities.

For the remaining chain branch in (D), the same common C direction is used in another 105 identities, subtracting nonnegative multiples of both H_0 and J. Nine additional complete rational multiplier rows are embedded. Every ordinary shadow multiplier is positive; their global minimum is 29/500. H and J multipliers are nonnegative.

**All 1890 matrices satisfy Q_s-I/4096 positive definite.** The main checker proves polynomial coefficient equality and checks positive integer Bareiss leading minors plus a separate Fraction LDL factorization. An independent program parses only literal inputs, never imports or executes the builder, reconstructs the quadratic polynomials by monomial accumulation, and checks positive rational Schur pivots and the same exact leading minors.

Summing each identity over coordinates shows d.(q_0+sum s_i q_i)>0 for every root extreme row under its branch hypotheses. Since d is common to all 105 rows, a feasible capped root representation would average these strictly positive quantities to zero. This is impossible. Together with the elementary cases, this proves that root cap<=7/6 excludes secondary cap<=7/6 at either q_1 or q_2.

Finally, the prefix belongs to the complete weak escape graph, not just a selected tree. Two incoming arrows at the root would permit a forbidden branching-root selection. Repeating at its unique predecessor gives the same conclusion at q_1 and q_2. All other paths must pass through this prefix, so q_0,q_1,q_2,q_3 are the strictly ordered four largest poles. Their three prefix edges are true polar edges because a true-edge escape selection exists. The first three closed diameter balls contain exactly the defining pole and its next predecessor. The older sharper four-ball statement under the smaller root cap may still be retained; it is not needed for the new common-cap exclusion.

## 4. Whole-C30 actual-mass filter at 7/6

The lead's simultaneous capped-row criterion and complete moving-plane reduction can now be used at tau=7/6, rather than 41/40. Its incidence counts are inherited, not newly enumerated. :contentReference[oaicite:4]{index=4} Here is the full argument needed for the new corollary.

Because 0=sum omega_i q_i and omega_i<=1/4, zero lies in the convex hull of sums of four distinct poles. Thus for ordered projections x_1<=...<=x_8, the four largest sum to a nonnegative number.

Let H(tau) be the image of 0<=eta_i<=tau, sum eta_i=3, and H_a(tau) the same set with eta_a=0. Then, simultaneously over all a,

```text
-Q subset H(tau)  <==>  -q_a in H_a(tau) for every a.   (C)
```

For a proof, the full inclusion tests F_1=x_1+tau(x_8+x_7)+delta x_6>=0. Apex ranks at most five only increase this expression. For rank six the difference is (1-delta)x_6+delta x_5-x_1>=0. For the last ranks,

```text
F_8=(x_5+x_6+x_7+x_8)+(tau-1)(x_7+x_6-2x_5)>=0,
F_7-F_8=(tau-1)(x_8-x_7)>=0.
```

The reverse implication is immediate. All projection ties are included.

A facet normal of H(tau) has one active tie block containing at least three poles, with k=0,1,2 poles strictly above it. Two distinct active two-point tie blocks cannot occur because the two coefficient breaks occupy adjacent ranks 2/3 and 3/4. Supporting planes of Q are harmless: the upper orientation follows from -Q/3 subset Q. For a lower supporting orientation, write its height as h<0 and its normalized primal vertex as x=n/h. The slacks f_i=1-x.q_i satisfy sum omega_i f_i=1 and hence sum f_i>=4. This gives 4h+tau sum c_i>=0; no false symmetric reflection argument is needed.

Only internal planes remain. For n.q_i=h+c_i, with B={i:c_i>0} of size one or two, the complete test is

```text
4h + min_i c_i + (7/6) sum_(i in B)c_i >= 0.           (I)
```

If every such test holds, (C) and the new theorem give S(P)>=2 for every physical metric. Hence any actual centered C30 candidate with S=1 must **strictly violate (I)**.

The three C30 dual facet-size profiles require at most 38,35,28 useful oriented internal planes, respectively; retaining every below-plane apex instead of selecting the minimum gives at most 152,140,112 scalar tests. These counts include accidental internal coplanarity and both useful orientations of larger tie blocks.

In the raw actual-centering gauge r_i=X_i-mean(X), g=centroid(conv(r)^polar), alpha_i=1-r_i.g>0, q_i=r_i/alpha_i, take a raw plane n_0.r_i=h+c_i. The transformed normal is n_0-hg. For a below-plane apex a, multiplying (I) by positive denominators gives

```text
G_a = 4h alpha_a product_B alpha + c_a product_B alpha
    + (7/6) sum_(j in B) c_j alpha_a product_(l in B,l!=j) alpha_l.
```

Its degree in the **actual** g is at most three. The minimum apex is selected by c_i/alpha_i, not by raw c_i. Substitution of g's rational shape formula can increase total degree. No condition-number cutoff, fixed direction pool, or independent polar metric has entered this reduction.

## 5. Two exact actual-Santaló controls

These are new finite rational bodies, not samples from the excluded strip. For either raw array X below: subtract its arithmetic vertex mean; reconstruct every actual polar vertex Y from the supporting planes; integrate its exact ordinary centroid g; set p=Y-g and q_i=(X_i-mean(X))/(1-(X_i-mean(X)).g). All denominators are checked positive. This gives g(P)=0 and s(Q)=0. The ordinary centroid of Q is separately computed and is nonzero.

### 5.1 C30 control with a complete unit-bad triangle

Use the literal raw coordinates

```text
0 (0,0,0)
1 (1,0,0)
2 (1/100,1,0)
3 (0,1,0)
4 (0,0,1)
5 (0,-10,109/10)
6 (-261/20,-11/100,1/100)
7 (-261/4,-1333/100,1/20).
```

For the asserted local nine-parameter shape family use the full chart

```text
X0=(0,0,0), X1=(1,0,0), X2=(a,b,0), X3=(0,1,0), X4=(0,0,1),
X5=(u,v,1-u-(1-a)*v/b), X6=(r,s,t), X7=(r*z/t,y,z),
(a,b,u,v,r,s,t,y,z)=(1/100,1,0,-10,-261/20,-11/100,1/100,-1333/100,1/20).
```

It preserves the three quadrilateral coplanarities identically near this point, where b,t are positive. All other support inequalities are strictly separated.

The ordered Q facets, also fixing P-vertex numbering, are

```text
(0123,0367,071,1542,175,243,346,456,576).
```

Thus this is exactly mask 6216436, with P f-vector (9,15,8). Its volume is

```text
45017047555848914398883357061091873229724800000000
/1118894922099656599273254379037565748714112169951471.
```

Write bar_gamma=max(1,gamma). Its eight values are approximately

```text
(1,1,1.0714426004127078,1.0713536151747345,
 1.0118349022515727,1,1,1).
```

Entries above one are exact optima; entries displayed as one certify gamma<=1, not equality. The bad set {2,3,4} is an actual triangular Q facet, so it contains every required three-vertex path combinatorially. Both gamma_2 and gamma_3 exceed 20/19. Nevertheless all caps are strictly below 7/6, and the entire physical affine orbit is excluded by the new theorem.

For all three over-unit caps, the oriented plane through q_1,q_5,q_6 has only q_7 above it and supplies the exact lower bound

```text
gamma_a = -(n.q_a+3h)/(n.q_7-h),  a=2,3,4.
```

The source finds matching exact rows. At apex 2, for example, set coefficients 0,3,4 to zero and solve the augmented columns 1,5,6,7; coefficient 7 equals the displayed optimum. Thus these are sharp LP values, not merely physical-row upper estimates.

In the identity metric the exact class is (3,2,3): stable facets 1,5,7; unstable P vertices 4,7; saddles (3,4),(1,6),(4,8). The maximum physical Lambda entry is approximately 1.0714599553192234, distinct from the optimized maximum. Strict cap feasibility below 7/6 and strict geometry persist in a relatively open neighborhood of this raw nine-parameter shape; no uniform neighborhood radius is claimed.

### 5.2 Eight-facet stress control with an exposed candidate root

Use

```text
(1,0,0), (5,5,-2), (511,-200,-138), (3,-3,4),
(5,-5,-8), (36,-95,32), (203,-79,-95), (0,-1,-3).
```

The actual P has f-vector (12,18,8), exact zero centroid, and volume

```text
386699819509711716744962303381054628484901505824
/8259194338770728736664282124799477358306124801130705.
```

Its truncated caps are approximately

```text
(1,1.0242065123053927,1,1,1.0962471825336900,
 1,1,1.0222911596121140).
```

The cap at pole 4 exceeds even 12/11 but is below 7/6. The sharp separator for gamma_4 is the plane through q_3,q_5,q_6, with only q_2 above it; an exact attaining row is reconstructed. The maximum physical Lambda entry is approximately 1.0984933017991383.

The identity-metric class is (2,3,3). The source additionally constructs a rational invertible T making pole 4 uniquely largest, using a strict supporting functional of conv(+/-Q) and a deterministic dyadic transverse scale. It audits TQ and T^(-T)P exactly; that image has class (2,2,2) and pole-radius order (4,2,5,7,1,6,0,3). Thus a correct actual center and a uniquely largest intended root still do not supply a unique unstable pole. The new theorem excludes every metric, not only these two audited metrics.

For both controls the source rebuilds supporting triples and both polar face lattices, integrates mass from two distinct interior apices, audits every true edge's four directed components, verifies all physical row identities, and checks all 255 affine-subset mass bounds. Neither control is an asserted attainer in the still-open 7/6 exterior.

## 6. What was tried and the exact remaining gap

The successful change was to preserve the partial coefficient in every capped extreme row, improve the two-descendant projection bound, and retain the one exceptional pure-chain secondary row as J>=0. Numerical multiplier location was followed by literal rational reconstruction, coefficient checks, positive-definiteness proofs and an independent polynomial/Schur replay. Exact reconstruction of the controls then tied the cap theorem to ordinary volume, facet centroids, reciprocal metrics and affine concentration. The supplied recovery needs no optimizer or numerical search history.

Exploratory shape/metric searches did not establish an actual 7/6-exterior attainer or a universal physical upper bound. No finite failure or apparent solver boundary is used in any exclusion. The constants 373/500 and 7/6 are certified sufficient constants, not asserted optimal constants.

The central remaining implication is now sharply stated:

```text
For every actual-centered eight-facet P,
max_a gamma_a <= 7/6 ?
```

A proof of that statement, even restricted to a complete C30 type, would combine with this handoff to close that domain. A counterexample must use actual volume and be rebuilt at its own centroid; a freely prescribed coefficient matrix or point-mass center is insufficient. A cap-exterior body would still need the full root/true-edge/reciprocal-metric mechanics, not just a negative moving-plane test.

The practical continuation should therefore target the strict cubic mass-cut exterior at 7/6 while retaining the single physical Lambda matrix, its square and flux identities, the cone-weight concentration bounds, and the incidence-sensitive overload restrictions. The former all-cap-20/19 three-bad-pole branch is no longer an open escape route. The external concentration results justify the mass bounds, but do not by themselves supply the missing optimized-cap upper bound.

## 7. Complete deterministic recovery capsule

Executed dependencies: **CPython 3.13.5, standard library only**. Assertions must be enabled. The capsule contains all three complete runnable source units, the unchanged literal parent tables, all 31 new multiplier overrides, the small exact matrices, both complete raw input arrays, hull/centroid/cap/mechanics routines, and the independent checker. No journal, previous sandbox, source download, floating-point optimizer, or unstated endpoint parameter is required.

Save the complete code below as `recover_nova_cap7.py`, with UTF-8/LF and its final LF. In an empty directory run

```sh
python -S recover_nova_cap7.py
```

The following additional complete rational check was executed after recovery:

```python
import json
from fractions import Fraction as F
r=json.load(open('mass_controls_7.json'))
assert all(F(z['physical']['max_Lambda'])<F(7,6) for z in r.values())
print('BOTH_PHYSICAL_CONTROL_ROWS_STRICTLY_BELOW_7_6_PASS')
```

Together with continuity of actual facet areas and centroids inside the incidence stratum, this also proves the asserted relative open control neighborhoods.

Two separate clean-directory executions were completed; every generated JSON and the complete transcript were byte-identical. Observed terminal markers include


[Encoded source block omitted; the code in this passage is incomplete.]


Expected identities are

```text
recover_nova_cap7.py  17857 bytes
5c82f81fbf4a4e895903385b765ab354610f2fe1a6dcbc01402e860517f167c9

cap7_6.py  16484 bytes
7bd3464dd5e8ba0aa3e7737a879820a921010749fc5ead3cbce90e0b432fb55c
mass_controls_7.py  11501 bytes
117e447ebba27fe1768fafcd6021220cefc5663178dfc4fb820931cb18282dcd
independent_7.py  2656 bytes
514c9e63094c74c0b168a12d64f5a044809a14d9b16e3c481061127d901dbd0b

cap7_pd_ledger.json  535760 bytes
0231bb8d5d044cbf48dd9635003c40a08bf62389698dc4ee3848e677d718aa79
cap7_proof.json  4584 bytes
7f5c2625d6d2745806122db0c3fb3d88bb04d24d2cb9823c931da619f1250238
mass_controls_7.json  282842 bytes
68f192172c835809f02da321371744778d75e7fc82dc66e912048ae3dced102d

Decoded source-bundle JSON  31298 bytes
27cd5988a34bdb1acb392d1347ae3963bcc74ebbaf6d7fc7dc3e0805ecab96ac
Whitespace-free base85(XZ/LZMA preset9)  15965 bytes
499425beb26f6d1f8bc4b75a357a1aa18df7d1612b503846f4ae61f0990f763d
```

The exact checks are software-independent arithmetic replays within this work, not external peer review or proof-assistant formalization. Convenience copies are [the decoder](sandbox:/mnt/data/nova_mass/recover_nova_cap7.py), [the finite proof ledger](sandbox:/mnt/data/nova_mass/cap7_pd_ledger.json), and [the exact physical controls](sandbox:/mnt/data/nova_mass/mass_controls_7.json). The embedded capsule, rather than those links, is the durable recovery source.

```python
"""NOVA24_WEIGHTED_CAP_7_6_AND_PHYSICAL_FLUX_V1.
CPython 3.13.5; standard library only; assertions required.
Save as recover_nova_cap7.py and run: python -S recover_nova_cap7.py
"""
from pathlib import Path
import base64,hashlib,json,lzma,subprocess,sys
assert __debug__
B = r"""
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;CewZp<Mtyh=^uXP~}q`MmN;rF2NM6)|{c94(n^!{(r34d4ee~M(PO}?IWy9j-yfksloos
{`j_LMk)=(G>gDL7?Pe%rB)<VbsvZoGs;cp*q7YGVSt+1SJ-%0{P{`<HJ2xa1Vxg^bI8<MJ0qySI_jSVJ*6iu^w=pr)kK!ax)ero
;{*Ai4mr=ks7tEG`hl>*kX<jh9uE{*q=75xP1MTx#Ll))rKN=7r=zx}cB!~Nq@aT?-p{(-I;orx4~L)dW(hE`)lg`{-Z+PN@DvI*
xu>OkV%c+`T+`|stvm@k^`YHo0Hm(-h_H8gT)5+AIbO5QPr8b#I&Nr~QS>&iJn<KW^z5JsY+VTBn^_F8X19I8xLyc)XE8qqvm-oV
JF(%`0wgd@y*(*1tv;24D@{v^5iXdMu;F;s!mi@d{)h7m?`o?Xzk(^P<lVfzTJ_Fm{Ls8W4c(Ocuj|;jKKPfSx@o_q9smNV8&Jn_
+^_r@ymH_I3ObbjTE%9-f32+fCrH>>=rUob8?@7=3p*t&XL$S+*Ew^iCo^*EuXDh{ScJ@K4rJl0$|nt9BB9;qBrm0TW-*XxFj&SK
OaMTiXl~4cOJMT|Z+`)>KAYPkZL;kqX|w7X3-?=KAREU6sSk6BJ{*U!8yeM@0FO*gXIJ)v=A>r?-n&!l>a@xpsOT^$j|iE^%e*`6
y<~N(ysVF9UB~w<iCg0VSW1}UYyYNOb1Xk$!7o8%<*kUIMAz=M4>~ds1+}skRwr{X9mKV)QcSt%kZGdoG~!Wr+UiOq+_d(;IF>mT
5zd~kMz|OxPr)3$yytrrk=KQWG2SWeFV&UHjSOrkR()yXK=bM~$ro#Y%s{}StXwshxv;vJu92EM8{oE5M^&QljJLF}O~aaG%`TTm
aY11kMURW>a8*MRD>XFPEk{Yr9as#Su63%KaclK_=8xuD(xubol3ANJs?H+6Wh^^t!TiUm5let)$ffyYy87ThG$y2PK21@KdmAeD
Tx#lXW%y@Hg1(cn70rMb{eExI&(wEp1Du{B&lJ`UhXHlqpEr3Xa+Xth{wvm}?58QWZPo@#VMt9R30LawA@AauW`)1-;m6!dT6>A1
NuU1eSN;scFxe`U`bRib>R}xIMq{_Ks2=3m@y!>1yhAGhYCWdPu?NvAUXESo7v!@wLID?M3iu}S+F+$pK{`i4YXn6ziojB!z$~*s
6HvvPJhN=Ga^)I=<vTj69<Stg%UUR06LO>7m%!<y5@~Zz9BIwll}ncC%DPs2*nRE6H~IGP<Z5R3WNs><2C^@i>Lz!e1x8oo1iRd2
)nGPPi!e~<)2M7Fqui%Em~uTcsk46U{5mrI*uXIpY8Iz+r|r99^al!YHPm2od<GrMYVr(o5pBJ}b{7%5VUxkeSlUg9lF43FJ3|Sc
I3d$!8Cta&+)gnAtlIQ1vEQ6PN;@Mmp)OAQTG{nWfv*eOpU|S|s1Qakw#ldEn6TXC%xXU-IT*WEV5O_~E~lNwkym$-sS4_1PDFhr
!`8|PMcx0>hKr`!l#cz7_M<A}bHIKU=!z&V`^mGpXQG-XXPU|UT7Vq{Z7IOhmqDKtFPdyxBYLrl5_sHW@joPjv~Dx1D=FX(bd-jM
H~n*ND;&K9WT9GS`?DJG)(_e^g>ey-p%8@3^#ReLEN{hulvM8dfRtYenYwYMj3Lj_HKMI(+xbB0$eWw30ND{F?(rWWf{~5Hm1X;e
kqB!Q0c0RIiJ#oO)1{%kYBPtt^m7^(kGNHUYi`~M|H6%)OI5pVn3O`z)}KLr>cH-eL9_bz>1>U^<9+cn?v9;UPHXUbskDIK-TRb|
qoRZ&9|O6*lw3bW8ht)A!Z5<?3SX9Rw?dE})m&IQp|+M7z^CSx?Vm@Ins}fRRzLpv!)=z{Ka8EKQNw*DgQ){md=nM-`>z|+^a!@6
CWvKO>5YdM%;B7CAwq5li3JTCLSoaM&Hii2DR*qQCGB>c;48r1sNL`o*rumUyxv|w29aJ-gSS^DKh=~r?Ox=Yc4m^b%68)|0W}_b
_$24#xbGZ~m308Mh`hII5z{D&vxbq7xIx&erU+Xw7HSe%YQ>-R7~W^}+Ps6(sO*n)?dc(DvOR`uyblgfhZ}P&5a|&fWXC~0Gf?r)
&&;Vz@_U(KNJ6~x^+j8M#x`PeMCt3j?+o0Ht!&B1XZz!@m;!~Z@gv&WH};jr3BA6KHL{kcoIUsGy9kW9JrFao%Obn$rM?q_!e4L}
C#^4}x*K;&FlhstCIJGp)rO$gg~h?iat3p{x6=Gc<5#nZX|p+I#$_Pce>7h&mLv)dYzF0(Ldp~E@7WAQGV!C#XX9T9P*saE=yo8r
c38Qt*9=+s^giFPb<a2wnA?DtRSW<<g~+Z|4tKdh=EolOh?C4HLPOBujgn>`RVhQa^`zP+p${hUH(Vn%(%8gQ_>%7{W_aqpVyx;J
BJ#4C*m~Ek(w4>bMi{~Ndqx0I1<3^aQABf)Ld`CLbKQ7Mu>LO08ByP8#*s&RO#4%=0OQ;+;dt8c$-|jdYt3Ja{Q3SaR8q}Rn>H>(
=jNQcuH9LE=O%`9#_NpJF*VwJc7eN-jT;D>B9#d`q_KL-9-ldKlO<a>E$6P%8z7EKOk^SczT_oGxZ@NdAeJ{Oif1d!bFxV^_}<~}
Rxjf#hGad@`_G(kC419X1|a_5as!39ZeCd2K8p*=?{o5Omr-x2a0~eXpHw!xB=wIj6=`JL^-Nl79!t4$qKWAadzfDYsVVsBL->bq
@tKDQ6Q?tj>_=0rSDxxhLC;5-Ieu-#_@z;LIK7T|mWqkw0@4{jdx6zMR6%-oQ|UAjdUc5SI}EB~&rE7dleW0ky<qk#M3?pvCHPu6
3Th7vC{IP;7&V?z3rt&()?|Vm$>o-}dDQ&i$NG)dr3!oK44%B&uoC@Q9w5g(;iUlRjWz9J%x5ibT{42kx0`Nucx&%e)-x>POjRT&
G@0oS4s=J!MmjEirOCf)xd6YR`VEwb7#WJX9A`v!XQEC8@I%|AzT+0{=?vqOvg12V?*mNyWckPvs;?hps=V+}!u+dfFaJ!vA3&fH
RKd}*E!mu*b=_3Hy<mx0;hBxZRraCHQF;;Pp5u6m|I@`2kHasdcVvGn-cmgU3d2^`3Ox)UFY|5p);d-mBH!OS0j^HqJ~ibWf!T2(
?;?EW6h_hM+0gg1X{Nhkia{hE?<y3KRH*PnR(&}3)OoZ1Z*`nfxDhf}y5C4j<SYNREWk;-Y;r7?#a>m(_x}TJlbnqm2`FW;`U7kU
&SIaxJ(ooRhV+%qas}f9ODB|~a^>zwW{-XzdI&v0*p$Fp>#4@8Fr&#L2Mj~=8vTyz8i;@%Y0ylbL@b`nAn5{HA=t;luvchMJ!DG&
W(*I|#cs|F8gQZoeYv#CiH^6kZIVa$f97xAY_)OkJ+;W(SW20|a%>-1f+TfekdJ!8WBFtII@~LNi{%F@#_WS#<O+FTEs|_6q)C%x
LU6yCSLY2;PBzjc35cO-WGF=DYl~<)3q8b-Nyk^sf^9M+zBvN8X{&$q6L5J5q9x6*-g>jTDvE%Qvi(fhU~o>Q`r7fj<Qb7*zdkuz
?_7NW8+u8+JKbwzqqRnW7wi+-_2P8a>5>JlflSg5(9C#j<Qa&ShxE3cp~IwM`mFE@aUY-^=QO;r^+trt_I6jNks>EGSw280pHK}j
O556vZEv*_WSUYf^}|Kq1ts_FkSp4m@JP_6ydPt{bQ?+CNH{`7E6>nD&_&a^edsjt3glamLV0x-FErba*n68f9++GKs%&bj-Hf4@
W@d&yKaNtbUKxxQ7VL~07V{)<5=3j$zddCb3D(K0pcgHK;u|A2Y)Lt!7f#LrR_!;AZ)U+N(}QDwnAEe34`N8zL)nCFuCfvCasF&y
X_ulkG2!bqqgw^g;OEC$LyIo`d1JSzd{e!`f4_kYwKB;Nt7rQ+69WNX^lXgr<Q5-N!MNh;h6ulnpEFc**@1!T7NS>7ibv>*3DQYX
@k^UW@aKO$kw=<0maiaWl~n(n(D=fnQyVg#_;3`eKpYJ-%`q>|F0=v&VPHLb0M$%b^OvQF6m*Vn$W4Nis7E(OIa7fg^q;24pCMIL
#?u8*=iz1N6*V9#SNhwr&<m-1lLjYqtmMCzd~KOh-$Wu7VXn-YX};&{x12S`DK2}1v$Vx0_@K2jCBwUml$T$GSO8>FxF;SoBgs!%
9?U$9`GJ?@RlH(aoT>j`z^gAW==HEJn;8QOTvAY>Y`zPxIrkeI@3MP=NFuMq9UFgqi*22t(CYk7iY51r!aK{j@Dr)oys?&tbcI@%
3y}lSccvr>A)pi9s;M05XwAfn-yD>rCcvwF_Mk?p+;HSthrnSZyX>XoH5|IWWAaH7GOP5&Wee!W<S>L1Ur0JrzgYhGDXyXmHvAx)
HHP<zQ{JW_S@}?*4nIyat?{N^dvGf~pvH^IrM*G56PqTu`g<u)TNC*I%T3yxzs`Yn_yUp-=`(WM2b2kXAbE--_*=r!{`4ZM)F`$v
249*=(r_2x2T@D37e$Rc7<%~o#6a`pF%4^<H)y0PZ}`cWb0DZ2-&Q@U!|j-L<E+YltajK*-axE!hDWmP|80f;Ehi)+?SPNy2EisI
blv9&QG*<gGPqw-3b#ztm|gbSf=3#&<kOX1pMr}8&=bl;O5)r-(Vdcnfeyz~WAADkmGo!VyIeI10Uz7bB-d}NhyxHguMZ-V{9z}8
w<j32ie!TmK||MR8ee^D_Enj6mOrue6`Z1Xl&e?f;9}1DtH<AH@8AFFHJkpm0-&eviGY{x*CF!<-Du6Rg1ftB7qk6-k&V|N;?qhP
KX5kv#YAyk`A!@w6!teQob!P$FMa<mLiCQ;m>1zRRt^h{Pt+QI@+*M)X1`m+mzHG;BY2PQWVY(uT!C8ojrYIW{DB&w2hUd$L`R64
sIV)w$How@Nl*=ZugVHIW)1-JHEK-Vm*T?x<sp#OMCJzz6u?k;{~EOphIH&Krz@GZ94EVjrzfVkdcW)zlqm%+-i%rvOO1tlGbtl`
-|Q*m!(=1IBb?4jr3_R^3ifu`?y76%roEa%^pK$NUn<1Pd<qU82EN_Re{j8nVy1^<EYwk`3g*afmM14EU8=P;;ye>JUp=deDk5JL
xW$<YJ8IJzyjaC1M?K@RJCI|eU-r-@>L2ZWQ5z|z<`_UHPi2Iu8E`?nw*Z#~F$Y|ux##l7GDKf7zRm7DOy}w?a2|A$Rmcmf{uPgk
G_cHmaPNZ3hgn*{sB4JdtNh_f%sm!SR*BDt#7?Jr+d^8~(_i@WhjT{p<qt-p{}bi8uSjOuK+jnPW?zg3iUURO@~^PMJSdLjnw*Yz
+2|pgFO^ygGRm+~<+g+fVi}(rvRez^L@@4a;H7$ZD_4P%#h6p!{!9SiHf%=Y600j=`j}f3fkQB|!;k?c30y4cA<Yl@<bFZguU~{3
QJl11!M`+z3oc93@XBvNy>U(AB3RAba_HLSLeT`#@d5#ZZ26K$8kBSL`j!%=<wa0RYAAiKuIyucLG=m=MtCO8LLwF;0MAIa9isx!
w--b|9(Xe*^O9JhJQ-R+52K3~!{$EFkM%**UPc$54`iqw-F)%$)ewV!Q@Tkc#^v|qh?PAmyD0bSTr(_&c;pB3YH#-?6|j|hWU|Uo
X18MbG>vM+U5%Vc2xV=GpOzkt?ytsbsY~D0aw7Bw%Hvyqg@p$O9=>48uOVU{wER^3zO^l*cu)=76ues8(^-JRJoIhbwb49^cBEKf
J)RbHBb0W;)sI(CqsyOTfneMwMN)z?k3d-Rs!bX%#x$I~s1=xyCW-x)6lFan#W-hk*1fa(Gr#>ES@<F$oL2{K1BAjsgto&v<yjuh
qGK(latg5!ssHkdyy=X(ni9EAj2IYlBeypJIAX8TtcYA+eEGr_P_iSYtNA6#a#1m^R$%rzk1%ByIXCY6h^%#8mex)`Jt?tAsV+2?
(oV52W$a!iminfDC^f(`F)ZB6ouF<pjog<W61B|4xusMqGNrUeqX^J<m!8VCoqK?2X&yM@U<xxFOnXo!YC#0{b&{u*eFDlF(4Pq<
fY<w?Ey|!qk(jqBAToiAUq2h^t-M_{BKrOMo?P70OaxVhKtrO;>wZ05QtHJoKAUwX#hlP`QP2{S^J=vgYE9hQ!VQMZ%q_brUn9zD
_aB)wO3x1_Hl!p&sBYQ}i*Xsf_7Py6hfr8O1_mMrY=Gi^4?u1NNzg(s+cLouQ)alWa-S+jH*GtW7W*JGt0$R4D0?1>%8_B=vJ*k#
i}WYyHxdpfAe4V-)w%%9`Ggo~3_fpZjY6u|tfiB(R_-Ra?IiVA&CxFVQfvtQgTVRso)FN=9R3so$qsg>#@+w!>}1xnt__G*4>MhI
j^pIvcf@%{J#zn<{-Y0O=$S<F#OpGW*D)QsfW7vj`Fsd|QphgiLeVdUsZSFtKe!GWNOE3Sv3I&C24}$tY|^TC=b7mee*048YKC~x
OO5Pg=bHRHg%bM;NpV#FkN}U&iq<v);Ek8rA5T%At7EO1h*<Rl*Nvc`tmWE+HSqcoAm&tvVZT&QF(en$rK;CX)x>rkiZ2;d+xhH&
!Z`~iITT;{=xm7LWJqcek7IrD-h#7mQqvj01&i!n=6=Z)kuWgJ^$_*)&GFQf91rTSf5?|fb0R4j>5Kg9_@Im6FY3!N@Tp7^m4C)u
CpRM4@FRtbp(kki1w|TM-w7e&D~|TAZNVYSonf=)=Mpu7eRtgduJ%DulM<GwV!Ia9VUy0l45{Cw@QQO6KoTqKJbQlfS77k#K4h+3
1VG0z1v;EY7MPOcaWBS54HBhb>GKz<U>zt!(ff+NOep6~*gkD{jlfq?&S?xEVEd^;KpY>l{M^YIdATseUDmH&ZM3Rw8(_$Ra?AAq
`84Wc#PhE_b`EWxlceu?OrJlw%u0=BjjoOL1=)1w(e$+8e9f+Be~x}GM&N?5E(j}kLhWepOSPGTOTtp#>f79hSLp!Mn<CwDyt;mY
r4l2^(J5>RABgcZv_Jb~(vvLHQUVS*FG=uOfB=5k5A#(4hph~yEM}aRQ<<`@=7AQDqW&#aYZ}>CxUKpbP%(3yt?ZQnmD2tm?^U1V
n+4Kgsos{_3>hf|Q)Yq^B+JkE-9!AAO`>Mgnk$Kg4FG96<T6k)kWF&1JAh8=e2c2SB~8kfsRMz}>G3yOGRLl~u*o(-R;14IArsS)
6o_=OKGMA9<_J^}3<WWC7VsbE@iN=Md1KeUP!+?C$XH<-@aS-p@w%Zb)R~kOGp3Z)n<dReE*=3N`>}_fhBOF9pK=*jj6K4@5J8^d
3-=W2JxLvY$QR}&4+vK>YAv1bxqr|hK@XjRYG_UT5V<BeYk{@H1Ugzl2GR=k+UL$M0`6BOHHE{d@8o5{-E%%O{!7?k0Vob!|G<oB
E8jqVN2HjMkAMDGX5?+rKyR0gw7kS2Lz#5XT6d*{=2k$GvJ<091J^|b0qZLbKYShG$PE+ok29<LQw=t!cSBq3fwuj+bc+HA_vrL$
h&gRWyIRl!f5KI$dl{NzB>zF`aX}OuxocO;*im+#ng~Iis)QY>vM!trld$eI(zHC|YL=MjW_@$4$AIFEwIef5Mw#_&7}n7ZS{Hlr
(~PEsuPdK_Qx_IQt)xQ32>YDv_*lw)_N8D{v{7Xq_aa>~PLa4CO_r_NsC%_>$_f3Y<|=Z(%Lzx@WvTIjlp9<@`eezbqxRoPJ*M(K
lT4%^9OA^CFQs%VT7sjl0jS0FdAzCdnQCRiB-*dlMD)y~>s@rU5@DLv68r*-R_M6EvMqbj(&dQZI_pqvWoaYvycto7v1NRQYkDGw
m?&U!lviE-f$7nA?(yJ<oh}aT|G;#`U#Qp_Y9CF5W>Q`&m<F^+BYTmko^DsreJ7VjeeTRnyh0WeO80ES<66e)Y>+5j(MXRBVIIjt
edSm6y)c*`VCM-VBKiJ-{wf%d0?r9LHxNlPOXB*UuJCdT{MnLURAJ`0Sy@Om{#J3p2?_X~FvFw)`U>X^#}11at~jg2RbOX^#+4T}
9f<5cSfgj}lX*MXB5cHjb*aAO_#+R-WbMj55RBt1L>sMU<1u<UhABsS3_vMe_XuSNMQySpcN5=SACk*|4J{Jx&Ti?d4^brZAir!Y
Y2!hc5V3_!@ndLoGLK;`h$PAjZvPGK0;zsFTL;x<dQ#3`#_(qndq;J*!`c!fK`f*~c=%_NaXc0cky{U$>x<b|i234a552;IdL7`O
qLg{s&W6ShRcU|1SXP}Cp|-?TrJgwsurBH%&vE_lEcY}+I>x`_l4%BrUQHa>bo+Ny8DA2P^gi5iguq!o%BJkIN^eGlhO17`f`V(o
Y|Xdd1}N6-solwQjwJF341g{oYt>S5{&C0ZD*KLHJc9=+ES=GhBA3P|PeXbN9L;l7Il~;*JUIdNm&H`pT}K_#h3$KprjEB*2o?I?
h;6s=Xwm{A6{;OyER8xtLN|u3-IWw)Sc8Vob_F#xsk{9&MZ-mPK;1lTXxf>vDj4>L*ydBFZMP2?nY*`*%;TZ6Bu10I^TXtuh3eTP
e9b@df<2(tP!)CIN4qi0Q%2#2Ad=DX;>Y^N<`A!!WIGo}Y=rnbzGJmbC<0jT4C>!kks<Ont{%N?;5v6wS?BiwprOswkd37p>9eaC
<Op%3&>5E_L}<K%Q)V0e2byk~CxVhmz7ZMbkCBnEy2d66v_;eI7z*f=lnN9=`_WDj?p3hoP+OP+no67Qu)-VD@mTFZ2((ZMN?Y@H
4cq!Y*i03ZYxq}vlHsQjq9RwpLc<y9D=?m-;#`T5@T!RA8^HGtWxeCSN|1yor`<Tl5RrAzOzV{?$#%a^aZB-=*!I=mWjZUg=&T^t
b2ni+BqF8Q^-C#ikOVljjU`)o3|^LrPri!+Rq_cLC3a1w)sc-dQ3zfKl=0ZT-@b*1hFZFoNXv=MGaf#QxLwHz%cc{aX8>yRL=N1Q
5$&iaqRlZ|wPviw?CGe*OSH5x(R1Ge)XD*YHCi*!KBb#|0|Ob`+&%3Qj6#y<)n-Yg9;eU{+%qCSUZjrXKj+cQ_Eh^M0aEc5$hk!1
^juNZbFI#Dj`_6Uq<@C`->*ewHNbv{bU2RF<#e;Hx>3e6B)++`A<z0j#cfhk)M8~RZn=O#(xnsUdSEVz8Mcex28l-BsnDj`h8r)p
@*9XHO_ltLRc_Y)$5Nq<38EqVvALuAz};o;ZkS>sb4m{2en*jz`m(oR=185t_)ipB@5N7x#wWG2{$3(USqN<lo)HurmpQ$|^m#is
Vwn_58O`G*kF9!j)=YafNm&Bjt;K%xea>=Juj?o(XN6Q^9K-!pEP3HUB2n?ncG=NYp$QZ~S;(HeRB1~=oQ;D*CW?kGx|Q^-NJLwr
ZF8NtCfgL{C;DN2Y0>Qq@43M}zAt52yqi}5)352aE7pj`fPOwYY<DK)sY(kc>2tAcCY9-|q&?X<7{jA*1WdJB<D0NV_H^F#D~u`A
M(a^5j<OsgEdiL&7Mz!FFUVnz#kQZLvL~-lN8SczgqnoaK$mVLhQPmp&qYmJ+E*2r2yieT;iOfYyZp2{4FCWPYg&|9M?u?*&bP>-
W9NIQ+t6$~?<h4lbb%2d%36`heB0qEgq_+=SDp~69VymnumKruLE!|ksg^N*K%1dy29z^87X#L&U~&8hN_=C_t$?c_SR_{KZQ-OA
n^+9tjbxq)2p-f~9)}tHUMX#-=U4mavMU68uFrgW=T6$QKv$&F9=-_qvxGB-6ukWIRNwjz^7#qd1J<sRkyf}XDLR4S-Ee4z-|9ws
Qhs1LQVuQ>C;k1gyjq|Zf>E%xZY@SPN=`@A$T$cM$cwU8d+5~XnUIn9D8C~48YC#KBY&V}BIE7@v}0rco|cWhdYEB*C^O~UyNg8R
eTQoU|JB8yR$PeX&0AgCg*iQc|Az@m4u;ZfKUtgHoPip;HnImkrU^b!D)ztMAL%NU#$Est-=gf#1OCa8ezxuH&pqzvsdG5X4GrpJ
k!4&E6ZOFVr5nl7uu9)mwz@{v$!3&|G4P@A2ihe%zT`m3wJ+>Di?ReR#90gCnxa1CbG#7wvMbV_wlc}3BkTH1o88vLsE=pml@f44
EinS~MYJQbp%P=kUF=kCerzfY4~QPr0ugp0$NnBV{qz-rMv=xOo<k=$37f4*B$!ND8%BLoorr|KwN9)VaUq<E!usvlvKK?uY+D~^
WSGdMMTNys83$l|g~Q$T2Rz-e?&&oZZ3&6M{sTtGT0U{~glR8lLz{JbB1O&I21uyLt6@^dO4EVmf3s-~yaV3^3dXJ+4%23XFn95J
^eg9NBvs<c?RTCfMET}A_Xlk5R6vIbZ#l9?@5>A}jcHd(>~_-Lb+I9DzQXr<zln;PMK$+=F>+h{JG5|a0S~X5DNvsNb;SFbMXwGO
Jq>vLNtwC!`mM^lo9MKWM-G+yvkoUjwIs?2gwO!agdhL1Z<N@(%i1NG<LL54W>7xSNPd`V3jZ!GB1*bRRdy3R1+*P>YM$e<K}yH~
V}4)ceD{g&Q|Z986;142v)|1SnTTOS#1;9<3cjx9{(Zr<`<bAl3X^$9g5@yU*lXgeCZbV4^dk005bh!v7;mCBv;i^hw8)~Yec8R}
nph#uwLmWug#TGkQEeFou1vVz)8g1f+ZwB7As<<foD@awU(^eRR1tz<W15*CaQiwS5Yk#?i`uq%@4SSXLtS}w_We{!>Rt{WS>l`z
lGxgVCBeGln?OcllN^(UqYl9Xe>k)P^#dJm!!6xTE~q3qrX<z-nuQtB<gk>X$>7`d?2LICK_TMSlt%H0bQP{`Zz$GQO7AP<VzvMN
D~jh>W30%5Dlm4hh*|;hBNS)6fCmbV*hWnS^{;fA*bm=o1<UTQ4X`G@P~;09p(d5dfpEfz){v+of3T~*U8_KTI8!7tyt?BpTywIv
qQslsQ&#06(9s1`>0}tmA3nc>s3TYsl6~+Yo6r&7i>zqODup{sbvlxv!v?^BoK#z_@u){4E<SiA2W6`nG*j|7Aw&TsQmqnyT)Vs=
b-)4ChHScHat&*lphcdyIiS2~uO|HiE9V0+dOU9s*_B~G9(N+Tn1ypelG}__UIWDqYM-gmRd-%Y^=GG=y1<ff-g{9XEaC4BdY~uy
{=o4aF%j+AFryg|k>k-K^>l3}sYr5$Mv~vWIBpx`TfiVr$#S>36t*(c#ytJxR8u}Ptqc9)d@wS9<;TcxK9dHUy6Ljj2djo`Z)Cm6
^6|P{0z*`~)?)5;HE3+x`-pu$m;jT_o8rE%`cdrZ?N+r6+r~l+<oZ*na}VB(bXd}qq^=VLmCTy3GyN6GQs#^GQn(SX*skUhh~x<4
Hc2OYuk=n}Q0RZ}mh?#5CVHCZ(bq#xgR5WMeo1!Nx$S_|<tMU_LUUA?wfeN=zm*>Jz5s(6$Ycj?+a={N0>R<Q!Bw=m-q=nTe)16V
3WKMVmS=_2Dr_f(orx<2_Y)`PcQ2RKAX;c$<qI8N6tj-A6IF9Zm<KUUfCPsYLY3q}XUBmiIj@?J?YbLbg`{3mr-*kyHc9|;*pM!@
zC`t|dO)RWFrD=C^*K~4-52OIUD&9n7*{^X56>J!sYXcxXn2OYDo+?sXQ9GLM=59UUsr}Fcv+pTLDfA=e)Dp^Ulo}D<jah9{ZmpS
R68IGwvTBfg<RBI<+Qy%*ef_u2A*9LHuRkPu7jy5GH^-XHoVhTv%{@ZrcBhR2!;bbB-QsKj~!ra-H&tP6X&7ZBK}3>u?_^4?T=U?
B<v3l@3?VJ)uA8r(+N`?q9%JbPDv;hKL({DM}$#{R&s03@_%Hq11j}ls0xFfSw4#dd7cx_+-^uH41pCuHw&aI(*LxV6+=bA8<>mp
&#^m~4bDHuu6iI1p2IRAPdJS~W(k`E#%c=?Vo3n<@tE+HTA)tb*;ERb=6eS|=UTN(>q$f-?(%>=R1E+ppG&tsoE#cbq(av0dL(o&
a=V{V3m;wp^UbFZAp%o2F=-Vclkco6@tJBU@&wU&DQjDu@{f-mg7X3w2jol{u2s&S#(CuF#>R%#G(x|thiGyOsItsiY?qIWB@k5M
%#M9(rTxko*=FHr<9mb*2wG1)2Sm^@CFRdEq$xDcs;hI!a93JkFwwxL%HgwlgyR)xyHLmB%9{Zgi?X6e)J+ml-&v5us(t*GuDUi^
>)lk9=7m*M6yg4FAt~w~G3Ts>Wfu+$mDJ+}Q<UN@inRJx+%jKUdD8N+B>|GY4HMjI`?KG4ilyh^z7XNvcGW=xpEI(>x6$@4BtcmK
%iCT--}%GPD9~8as-SUgRVzIr^JfE~bvQMek=_OGIssKr<hGQvi3=|Qu(*eLBBM9Nmj3rvROkFtVp}=y2a^tY!W~;)Ok-4A6Sl7`
92lV_CVEhZ@%?bSq@Cfrw)vBkqk!+%A~wL`rm$3+QJ^u%a$Hrcd|H9?rAwRpYhrO)v(3%S=F2fY^ah#KRpJPl?7@|2K<(J?HZ%X>
6WB1epRglpI8Tka+kZ}O#bWwQP#5M7RC0~p%WDKFDsaYnPhNZQJBbB+UA@Tze2{j#?9$zX>+apS|3EnWr;zf>qv>(AHqe>w38-Ib
#o6<Ca1NoIx^-DE%hP@=1Aa3}OJr&`C!reayrBD$6ON>^G`{5(Lg8&7THLQaWC7_Lp?1F}uuHUzZPJh5#7Q$+zwgb5rI%7%0)iE~
<iDSoxDQp8Ssq>#qL!|~kGPMCzf*CmSP0YRZQk<85FDGL^DH|1jXBZ34^;SPsGPFVhE?V&7BJLdadcCUIJWq1<IR@2ENV2uO&*Ic
V(c1wH((jdt-mc?>UZqf6SM$>E)L_;E$0NTPjdhkz2X*Rl{#gHlyKw9du7*Rm~DWM!uUiC*~-)!lOUyOW0wBD@!?GhrQ>T+&dU{{
Bn#OZ_e*BhbghO$%Uw7UKhXm&0-&}ggXv#k#~T`yGq|dJ1r~NZ?3N8;O9W|7&s+KRe<j;UgR1x)-wyGnU}{~$8^0GA#Ho=(FjKON
om2i<31?^^4yhp#@VHf2W7o7!CEpF+iac3)`Pw{^d??jwhy?1FFWk8}&9=ZcxS1in+r8T*dn@-dR~f9(;8v5U37NrOO(&eSZ0mr}
HGY@h3a6Fms&*NgVYz+Dv&uomV=;dZb14-vc;v^S%!5oxush}ryx!rRPx8!`;bHYDBv0MVxpUAX45rW_Za_*M*T)cMaho=JP;W5{
E<Ebg%nPFgpBz^0xRvbqUJJ>gL43vIDeneD^LzIdeN|bW0<83w)dFf8vI1`$@mBAhNt8i8giA}laZQ@Yj7C2Efqz*ZdB=p^LFRl}
-M%cNXd66K?h`L>!zl>E!m!)pVarsmPyY<(oIEK$^yTNt{c_20r0A9MF*=Q=R?Tn*C^cxaTJwltFtd!qvXiN_f(-SKeNp2^dLBoZ
-JdCZ$zZ#HH^wl#U%3r@mN@(;e}Jon^!3sqYMc|2p9-`pAYd1iD`o77Xf|K0pIIpn)gQ8l0T$2Mq8tjr3+caTdOPfg)J6mz0*DO}
!B!OWO8SexQA`7m#<#Bsw0uF2zWg-{Jx{wkb|J3Q42-GUFw^Bb(=i*bGE2SLYdPYi8SJ)349^5W{Og6#Qoq=VWUQxOP!8QqOmF2C
4X@@u;8%r!M-pO{@uX#)jM}~>rB_(H4NrHy4*#ZEu8QWUI#vLU8Wo7Wa`m&XUi}t&8v=|SIw~!}9Z=m?VsMrp8TeD^YS~h)HG=<<
|B&pnssMbKGND9*_e+izl{;p-6GyH+!REy<?2Ra;AKsM!7_d9%mJw;&hjUllYwfG=Qi~1&;B|0)8rP7)S<Svy2(`n(r3n5cu2Eqw
kVk=pvzc1ky`?~ylUX9JER8)>CbM0)aN1a!M@vq8r$~TEt*nJ6X*MBj7yEF_4p|+5MZ&DyN~y?V7)od^M;MqL29*8D_KTYOg?9;I
=#?iXgX*Ee+vc!u861{`(R+K}^3UsxSZxV8K$jSlEVE7cg(HJ-e5lIORpvEU9Q=iU%gA%0;_*WwTi_P$?R5)N*mb-xFJm8UPI1M`
>-bn1ZOYB}AFOZ9s!iNmfkGx#<<}cW#RSR+^qYYp^s<bp`kq3(MGn0K#Jy))MWX+(qGU8U66s$W9KP-P&(}zuXbNt6kymOIl4r7X
FYIfkR<tdPwWR7n%646-6d?Hr4gXd!+V(7O)w}w8qGm=7L_9&55cKQ9rH26924Ozybh&x}d(@7}b-#V;%Jftt+j4YS7oRgN+Zs?<
zR4H|z&Ib2{-<<Le1<0O+NV}gw9%b73o35-P%Uv>MMR|K@{Mrb`8$lYz#5Pcwd;n910xo4!h2mCzyI8@$9m5TRNJFhUB*miafeU8
01DmZ{hOBL4|I+r+R4DJNqjQAK`ql{tvlyEQl#6ru$32fb4?%^dHa9q!EPvNgG<t5xg@OsRIXO^vwlm`Hr>$_R-wQhjvD{LpPwH%
PrKAGL8$nN0nH}jWX?-Nv?9)g7Y-A+SD4XOb2(`4p9j_804-YQ?u(p4T;6h+`j{Y23o9RCDw$pnu}q7rFg4-=x2mhg2XD|juZe6F
a@xDXH|rUK#4V)MeHl)OHlc521%wlXB=xd29kjXJpX-*8mLz;nLL6~41Z6h~QtV1OTC_3s<LVl*DBB?I^^7)yVYy<57SLCVYZ<nI
R9N4#E##YRec>89?$oU`xC^_p&3vquzgg7j1k>PLgXgwC{-sm+nr^KCUyn(kdjmmaA9<#o<q=LW@Re;SxLOTC%QfaE?Y<3#%uu@t
u+dm&AtnBExe{YnBa02vUsdHv^RU_*puPC)@~90Hdfav<LhIiXyN-z`xK(?1m{(T&o7gdGtUiEc*zDf7K_Ogsv}6M)sZ5D=cAn&o
?mo>^4q6y%@Hh=}K|h7CkIDsTdAUUZmU9Q3E63*rgg)bX2mf#YLVw=GzwLfXt-<(H{3te93S3>mVc!5hQkwomZ^!J~qe9uE<9J!@
ohsI&{Ix{eRhQXzq)~p|flVZVTEQ3Q<MyoEEwAZkvTvYonqZ~S*bbDRLCJyK$t(6yp8u+0>{%6z`IWhAMH>zp7#u36@S32;{)ufj
u>1A`Pc%kfY?NgqVeD9zWq=Ca&nQc^jOhc$lU$YahsyP5%tgLM!I$I1xMh25lSV!6e_Qk~B@X{f1|yxfur~T>+bWWhJ)3HtH@ntg
)Ep0M0qqZ@BAEPlh5pbjJs_USb~a6hA96v{i^}dNA3LE`!dL%d?2wA_)Y;O(pqgRjgipAdKUA%HV+hup@12<CC6W(${bodZ@%Vmt
Il~3-h^nDbBJl_|6*Z@*6)B^xiqh-o#il!HkxV-f3iK)_4KwwsTNKUd1a4^njxhDs?{FSrzo^8-I4+uAQ&~+^G7Xh=m(k&qDw;wS
xkr<PS!<2O<G(OBDlz5WdRqQZg@D~^hqy%w{ai*_CRyVjF8@WiR3;xPBA4FFutu4>m!S0_qbQ}6%4Va+wI%DM3jDUWBPoETt{|DT
*CHqSkk8AhhI%?QhJ(uxy`G-dg1kZfN87QRE1Hwo%AX(ia#b@)1W+=ow>h9b-r+092))3~el?$h-}O2_#IcJxdH>WaTT3|RKM89|
9A1>V0+*;3r<=t%0`m-*VITu>#?m3{hBNh+q_2nN!s;-}1MEas{s=F)2?O@y&%IpeuC!sTZf6Tac(&s`<}|igb}%5$BTiTg>+4Am
7YJ;B6nczv)9FZjWrEtMa6CzOUpQ|oc|_fSO$7IGn_W^jJXHF%UN5%;iaP`lkgAe*N(h9-@nIV{w{w!+lQe4h_3VySALyK!=1PZ<
sh^<TbcrM;gWK<2l%o$N6-V@vcoGI+<`H)}><!0XU%B$}@w{gjoL@U`GFJtdK-C`lZpX4gMMQY+6%t;cv1&z#ql{p9`dU*YWZ|!h
pLFRqylQ5(08gzt<{&OdQWU2@>r49z<rPAXV#|6;LwN)KJTMu*J)QCPf?pgegMUoDrMGC}AnsAUmuZ|I#?Naw$vDIvPPxRW5+qk_
{$GnkMU{{It>3p9;9daE?vc8%InHOLM=e`uD7F)bWR*25R1ohCv0Y=}y8my^)R6{6shQh-e;s==u#9|>JWAbl8jx{Lno{5PC3qYC
3tlTcBHYLpHsv_CnGf<QT8FJ;nIToq%5j%U>-nTpdg3}}AE3$s$(lRn|Ho&`RMB-J8DICTVzGGGCOE{`Knpkr+${x*^cO?3tAjL2
?N}^!!mwv)tyP4?Y)P>-P+>Rq+iZOFghBoaEZWYk0c^NL6R^LU)`!RoMOn8gLZn&Jr`tIQc;IZGd{l=;%4N7ITuz-Yk|T46;|f0B
j;NL_;5K7K<}aK#Ri>f_ve0=@;JdGnU*%wZS-c9*H|FyzH}&fNPrfEDW=t2v-Lgwpx&IGb_FW8XMuq<u(kH$UF=8bor@Ty$ohqHb
I(*lHwZCl{J&!h#=8|IA00000W!zT01RVkX00F&Y!t?<ED-{9EvBYQl0ssI200dcD
"""
b=''.join(B.split()).encode('ascii')
assert len(b)==15965 and hashlib.sha256(b).hexdigest()=='499425beb26f6d1f8bc4b75a357a1aa18df7d1612b503846f4ae61f0990f763d'
r=lzma.decompress(base64.b85decode(b))
assert len(r)==31298 and hashlib.sha256(r).hexdigest()=='27cd5988a34bdb1acb392d1347ae3963bcc74ebbaf6d7fc7dc3e0805ecab96ac'
sources=json.loads(r)
MANIFEST={'cap7_6.py': [16484, '7bd3464dd5e8ba0aa3e7737a879820a921010749fc5ead3cbce90e0b432fb55c'], 'mass_controls_7.py': [11501, '117e447ebba27fe1768fafcd6021220cefc5663178dfc4fb820931cb18282dcd'], 'independent_7.py': [2656, '514c9e63094c74c0b168a12d64f5a044809a14d9b16e3c481061127d901dbd0b'], 'cap7_pd_ledger.json': [535760, '0231bb8d5d044cbf48dd9635003c40a08bf62389698dc4ee3848e677d718aa79'], 'cap7_proof.json': [4584, '7f5c2625d6d2745806122db0c3fb3d88bb04d24d2cb9823c931da619f1250238'], 'mass_controls_7.json': [282842, '68f192172c835809f02da321371744778d75e7fc82dc66e912048ae3dced102d']}
assert set(sources)==set(['cap7_6.py', 'mass_controls_7.py', 'independent_7.py'])
for n,t in sources.items():
 d=t.encode('utf-8');assert [len(d),hashlib.sha256(d).hexdigest()]==MANIFEST[n]
 Path(n).write_bytes(d)
for n in ('cap7_6.py','independent_7.py','mass_controls_7.py'):
 subprocess.run([sys.executable,'-S',n],check=True)
for n,expected in MANIFEST.items():
 d=Path(n).read_bytes();assert [len(d),hashlib.sha256(d).hexdigest()]==expected
print('NOVA24_WEIGHTED_CAP_7_6_AND_PHYSICAL_FLUX_RECOVERY_PASS')
```
