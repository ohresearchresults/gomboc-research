# minimum-0014

AI research report · 2026-09-07 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# NOVA24_GLOBAL_CAP_41_40_V1

## Result and scope

The new result is a **universal 2.5% pole-coefficient obstruction**, together with a consequence for the **complete** pole-escape graph. It uses no prescribed incidence type, symmetry, bounded metric condition number, or radius ratio.

Let P be a full-dimensional homogeneous convex three-polytope, with its actual volume centroid at 0 and exactly eight maximal facets. Write its true polar as Q=conv{q_0,...,q_7}, where each facet inequality is q_i·x≤1. For a pole a define the **apex-excluded coefficient cap**

```text
γ_a(Q) = min max_(j≠a) λ_j,
subject to λ_j≥0, Σ_(j≠a)λ_j=3,
           Σ_(j≠a)λ_j q_j = −q_a.
```

These are algebraic containment coefficients, not independently assigned physical masses. Actual centering is imposed separately. The physical construction below proves these linear programs are feasible for every actual centered P.

**Theorem.** If P has exactly one strictly stable facet, then

```text
max_a γ_a(Q) > 41/40.
```

There is a substantially stronger localization. Put τ=41/40 and let r be the unique unstable pole in the physical metric. If γ_r≤τ, then the five largest-radius poles have a strict ordering

```text
r=a_0, a_1, a_2, a_3, a_4,
|q_a0| > |q_a1| > |q_a2| > |q_a3| > |q_a4| > every remaining radius.
```

In the **complete weak escape digraph**, whose arrows are i→j for distinct i,j whenever q_i·(q_j−q_i)≥0, the sole incoming arrow at a_k is a_(k+1)→a_k for k=0,1,2,3. Consequently every escape path from one of the other three poles enters the same four-link chain

```text
a_4 → a_3 → a_2 → a_1 → r.
```

Paths starting on this chain follow its suffix to r. Moreover, **γ_a2>41/40**. Thus the excessive cap is forced either at the largest pole or, after a rigid complete-graph alternative, at the third-largest pole. This is not a statement about one conveniently selected tree.

Equivalently, each of the four closed diameter balls with endpoints 0 and q_ak, k=0,1,2,3, contains exactly two of the eight poles: q_ak and q_a(k+1). All other poles are strictly outside that ball. These assertions include weak escape equalities; no additional nondegeneracy assumption is needed.

**Whole-class exclusion.** Every actual centered eight-facet P satisfying γ_a≤41/40 for all a has at least two strictly stable maximal facets under **every invertible affine linear deformation**. More generally, the finite vector theorem below gives the same conclusion about polar instability for every positive-definite metric. The metric on the actual polar partner is its reciprocal, never an independent choice.

This does **not** establish F≥9 or exclude all C30 bodies. It supplies a rigorously delimited, affine-invariant excluded class and a universal necessary mass/escape obstruction outside that class. The threshold 41/40 is certified, not claimed optimal.

## Parent authority and the actual-centering control

The authoritative active parents are:

```text
minimum-0008
210f1968ce162060b752db868a0f9930508f1b487f1a4bd406218f1edddf75bc

minimum-0009
6f905a98d5d84d11e1369aebb34643ad59248a2485b95270c59bb52c48b92326
```

The first parent's own-centered (9,15,8) control is strict222, with q_3 uniquely largest in norm but −q_3 separated from all 56 distinct-triple sums by h=(−347,0,249), with gap>4/5. It is not S1 and does not itself supply an eight-pole escape tree. I preserved that distinction and independently reconstructed the identical vertices, poles and maximal-facet cycles. No incidence or object-identity substitution was made. :contentReference[oaicite:0]{index=0}

The second parent is frontier provenance, not a numerical input to the new proof. Its surviving count is **178131**, across all **74 types**, with 4369 surviving joint root-pair orbits. I have not regenerated or reduced that frontier in this assignment. The inherited bracket remains **30≤C_min≤1374**. The new geometric class is not converted into an unsupported count of closed combinatorial records. :contentReference[oaicite:1]{index=1}

The finite algebra reuses the complete 17 rational tables from NOVA24_V9_DISTINCT_TRIPLE_V1:

```text
minimum-0006
4480a792dec44a82e252175c8263360cd2cac11c705c881fe30da85b47087f08
```

Their exact 5705-byte JSON is embedded in the recovery program, SHA-256 `34f501da2c4cabec97a55ca8311381a78eee0603c9c46c7c375a3f3dbf859af6`. The inherited unit-cap argument and its distinction between root and secondary-apex conditions are recorded in the journal; the larger cap, six replacement rows, complete-digraph consequence and the new all-metric application below are this continuation's results. :contentReference[oaicite:2]{index=2}

## 1. How actual polar-volume centering enters

For facet i of P, let A_i be its physical area, h_i its distance from 0, n_i its outward unit normal, and c_i its uniform-area centroid. Thus q_i=n_i/h_i. Define the **actual cone-volume weights**

```text
ω_i = A_i h_i / (3 Vol(P)).
```

Divergence and integration over the real cones conv(0,F_i) give

```text
Σω_i=1,       Σω_i q_i=0,
Σω_i c_i=0,   Σ3ω_i c_i q_i^T=I.
```

The third identity uses g(P)=0: the centroid of conv(0,F_i) is 3c_i/4. These formulas use maximal facets; triangulation is only an integration device.

Consequently the physical rows

```text
Λ_ai = 3ω_i(1−q_a·c_i)
```

satisfy

```text
Λ_aa=0,  Λ_ai>0 for i≠a,
Σ_i Λ_ai=3,  Σ_i Λ_ai q_i=−q_a.
```

Strict off-diagonal positivity follows because c_i is in the relative interior of the actual facet F_i. This proves feasibility of γ_a and gives γ_a≤max_i Λ_ai. In particular, if γ_r>τ then the largest-pole physical row has an entry exceeding τ. If γ_r≤τ, the forced-chain conclusion applies and the third-largest-pole physical row has an entry exceeding τ.

In purely physical quantities, an excessive entry is

```text
[A_i h_i / Vol(P)] [1−q_a·c_i] > 41/40.
```

The second bracket is the distance of c_i from the plane of F_a, divided by h_a. This is a quantitative actual-volume obstruction, not a claim that arbitrary positive weights locate the centroid.

The orthogonal foot on F_i, in the primal metric M^(−1), is Mq_i/(q_i^T Mq_i). It lies in the relative interior of F_i exactly when q_i^T M(q_j−q_i)<0 for every j≠i. Thus a strictly stable primal facet is exactly a strictly unstable polar vertex. At every other polar vertex, a nonnegative radial derivative exists along a true edge, since the incident edge directions generate the tangent cone. Any largest-radius pole is strictly unstable by Cauchy–Schwarz and distinctness. Consequently S1 supplies the unique largest pole and the complete escape structure used in the theorem, not merely a chosen largest radius.

Nothing here asserts g(Q)=0. The actual Santaló condition is **g(Q°)=g(P)=0**. Under a physical map P↦T^(−T)P and Q↦TQ, the pole metric is M=T^T T and the primal metric is M^(−1). Cone-volume ratios, facet-centroid/pole pairings and all γ_a are unchanged. Thus the proof covers every SPD metric without compactifying the metric cone. The joint110 estimate R/r≤27 is neither assumed nor used.

## 2. Finite vector theorem and complete coverage

For any four through eight distinct nonzero vectors admitting a weak escape tree, define γ_a by the same apex-excluded linear program, with value infinity when infeasible. There cannot be cap-τ rows at every apex. For eight vectors, a cap-τ row at the root alone excludes every rooted tree except the following four arrays, in parent-before-child canonical order:

```text
[-1,0,1,2,3,4,5,6]
[-1,0,1,2,3,4,5,5]
[-1,0,1,2,3,4,5,4]
[-1,0,1,2,3,4,4,4]
```

For these four arrays, a cap-τ row at vertex 2 also excludes the tree. These are exactly four unbranched initial links followed by an arbitrary four-vertex rooted tail.

For 1<τ<3/2, the coefficient polytope on seven non-apex indices,

```text
0≤λ_i≤τ,  Σλ_i=3,
```

has precisely the extreme coefficient patterns

```text
τ q_i + τ q_j + (3−2τ) q_k,
```

where i,j,k are distinct and k is designated. At τ=41/40 the partial coefficient is 19/20. There are 35×3=105 such patterns for each apex. Therefore it suffices to separate every root-plus-weighted-triple extreme point by one common direction for that rooted case.

### 2.1 Elementary projection bounds

Along a weak escape path, squared radius increases strictly:

```text
|parent|²−|child|² = 2 child·(parent−child)+|parent−child|² > 0.
```

Writing the successive ray angles as α_i gives the contraction |child|≤|parent|cos α_i. Append the projection angle to a negative-root support calculation and apply concavity of log cos. A point at depth d has negative root projection bounded by b_d times the root's squared radius, with

```text
b_0=b_1=0,
b_2=1/8, b_3=1/4,
b_4=(11+5√5)/64 < 89/256,
b_5=27/64.
```

If at most four vertices have depth at least two, the sum of the negative parts of any at most three selected projections is strictly less than 15/16 times the root's squared radius. The only three-mark cases not settled directly by the depth bounds are a chain marked at depths (3,4,5) and a fork marked at (3,4,4). For those, set M_00=75; put respectively

```text
parent = [-1,0,1,2,3,4], diagonal = [128,208,352,336,192],
parent = [-1,0,1,2,3,3], diagonal = [128,208,368,176,176].
```

For i=1,...,5 put M_ii=diagonal_i and add −diagonal_i/2 at each symmetric parent off-diagonal. Add 40 at both entries (0,i),(i,0) for i=3,4,5. Then

```text
x^T M x /80
 = (15/16)x_0² + x_0(x_3+x_4+x_5)
   − Σ_i (diagonal_i/80)(x_i x_parent(i)−x_i²).
```

The exact leading minors are, respectively,

```text
75,5504,333632,15370240,434778112,56623104
75,5504,333632,9116672,817229824,5266866176.
```

They are positive. The remaining depth triples have bounds at most 229/256, 217/256, 210/256 or 3/4. Any two negative projections in this four-deep situation have total bound 197/256; one has bound 27/64. These last observations justify using negative parts rather than accidentally retaining favorable positive projections.

Multiplying the negative-part bound by τ gives a positive root-plus-weighted-triple gap

```text
1−τ(15/16)=5/128.
```

The same argument at the root's sole child works when that child branches; the root term projects at least as positively as the child's squared radius. A sole-child subtree of height at most three gives 1−3τ/4=37/160. Two root branches of height at most four, with fewer than three depth-four nodes, give 1−τ(242/256)=159/5120. The two easy long arrays are

```text
[-1,0,1,2,3,4,1,0], [-1,0,1,2,3,4,0,6].
```

Every marked triple in them has a four-deep ancestor closure or depth bound 229/256. The program checks all such triples.

### 2.2 The remaining elementary broom

For parent array [-1,0,1,2,3,3,3,0], normalize the root e to norm one, let a=q_1, t=|a|, c=e·a/t≥t, and let z=q_7. The subtree at a has height three; z lies in the closed diameter ball B(e/2,1/2).

A weighted triple without z has positive a-projection at least t²/4. If z has coefficient λ_z, its root-plus-triple a-projection, divided by t, is at least

```text
t/4 + λ_z(3t/4−1/2).
```

For 9/16<t≤2/3, its minimum uses λ_z=τ and is greater than (9−5τ)/64=31/512. For t≥2/3 it is positive directly.

For t≤9/16, every tail point has negative-e support at most

```text
f(t)=t[1+√((1−t)/2)]²/4.
```

Indeed its path from a has at most three edges, and appending the final projection gives at most four cosine factors with total angle at least π−arccos t. The displayed half-angle formula follows. The derivative of f has the sign of 2u+4u²−1, where u=√((1−t)/2), so f is increasing on this interval. Since √(7/32)<15/32,

```text
f(t)<19881/65536,
1−3τ(19881/65536)=176077/2621440>0.
```

The other root leaf has nonnegative e-projection. Hence the broom is excluded too.

### 2.3 The secondary-apex inequality at the four exceptional trees

Suppose cap-τ rows exist at both root q_0 and b=q_2. All points except q_0,q_1 belong to the six-vertex subtree rooted at b; also b·q_1≥|b|².

An extreme b-row not containing q_0 has positive b-projection, by the four-deep bound and τ<16/15. Therefore an extreme b-row with nonpositive b-projection must contain q_0. Its other two negative contributions have total less than τ(197/256)|b|². This first forces b·q_0<0, and then, because q_0's coefficient is at most τ, gives

```text
H_τ = −q_0·b − κ|b|² > 0,
κ=1/τ−197/256=2163/10496.
```

This is the needed quantitatively weakened secondary-apex constraint. No centroid identity for Q has been substituted for it.

### 2.4 Exact matrix certificates and tree enumeration

For each of the 17 remaining canonical parent arrays, the embedded table supplies C_i/1000 and coefficient rows A. For each weighted extreme pattern s, put s_0=1 and define d=Σ_i(C_i/1000)q_i. The ordinary shadow multipliers are A times the nonroot coefficient vector, divided by 1000. There are six explicit replacements, all for the terminal triple {5,6,7}, in table cases 0 and 1. Their eight numerators, divided by 10000, are:

```text
case  partial-index   shadow multipliers followed by H multiplier
0     5   52168 115280 144919 171642 202930 156859 82761 33811
0     6   52046 114952 144815 171911 203874 151765 83006 33482
0     7   51998 114771 144690 171943 204282 152271 77190 33308
1     5   51620 114379 144856 172482 204581 79774 79774 33148
1     6   51502 114029 144715 172720 205569 74287 80157 32805
1     7   51502 114029 144715 172721 205569 80157 74287 32805
```

The program reconstructs every quadratic identity

```text
x^T Q_s x
 = (Σ_i C_i x_i/1000)(x_0+Σ_(i>0)s_i x_i)
   − Σ_(i=1)^7 λ_i(x_i x_parent(i)−x_i²)
   − λ_H(−x_0x_2−κx_2²),
```

omitting the H term outside cases 0,1,2,6. **All 1785 matrices Q_s−I/1024 are positive definite.** All multipliers are positive, with minimum 1587/20000. Exact leading minors and a separate LDL reconstruction are checked. Summing over physical coordinates makes the common direction d strictly positive on every root-plus-weighted-triple extreme point, contradicting a cap-τ root row.

The 115 rooted eight-vertex tree types split into 30 four-deep-root cases, 28 four-deep-first-child cases, 7 shallow-first-child cases, 30 shallow-root cases, one broom, two easy long cases and 17 matrix cases. Their parent-before-child labeling counts are 2556,600,52,1638,7,56,131, totaling 5040. Every rooted tree admits such a labeling. Sorted-parenthesis canonicalization checks all 5040 arrays, rather than selecting a sample of geometric trees. The four-through-seven-vertex cases are covered by the elementary four-deep argument; the program additionally checks their 870 arrays and 81 types.

### 2.5 Why the statement concerns the complete graph

Every arrow in the full weak escape digraph strictly increases squared norm. A unique unstable pole gives that digraph a unique sink, and every independent selection of one outgoing arrow at each other pole produces an escape tree to that sink.

If γ_r≤τ, every such selection must be one of the four exceptional trees. Two distinct incoming arrows at r could be selected simultaneously, producing a forbidden branching root. Thus r has exactly one incoming pole a_1. Repeating the same argument at a_1,a_2,a_3 gives the four forced incoming links. Every other pole must eventually enter them, which also proves their strict radius ordering. Any one resulting exceptional tree then shows γ_a2>τ. This is an analytic consequence of the complete tree coverage; the code's prefix marker checks the four exceptional arrays, not an enumeration of continuous geometries.

## 3. An actual-Santaló class beyond the old unit-cap core

For the **unchanged parent (9,15,8) body**, the new exact program finds apex-excluded rows with cap **51/50 at all eight poles**. This includes boundary q_3, even though its unit-cap distinct-triple containment fails. Each row is generated by fixing three coordinates to 0 or 51/50 and solving the remaining four affine equations exactly. The complete deterministic basis witnesses are:

```text
apex   fixed indices   fixed bits, multiplied by 51/50
0      1,2,3           1,0,0
1      2,3,4           0,0,0
2      3,4,6           0,0,1
3      2,4,6           0,0,1
4      2,3,5           0,0,0
5      1,3,4           1,0,0
6      2,3,4           0,0,0
7      2,3,4           0,0,0
```

The source reconstructs the full parent geometry, rechecks actual volume centering and all maximal supports, and emits all eight complete rational rows. No LP optimizer is needed for this recovery.

There is an important distinction from canonical-row capping. For this same body the largest **physical** Λ entry lies strictly between 41/40 and 25/24, so canonical rows alone would fail the new test. Nevertheless the alternative rows above succeed. Blend each alternative row with its physical row in proportions 9/10 and 1/10. Every off-diagonal coefficient becomes strictly positive, while

```text
max blended coefficient < (9/10)(51/50)+(1/10)(25/24)
                        = 6133/6000 < 41/40.
```

The exact observed cap reserve is

```text
5596120435066630801508658394958883792496777679
/1972201329122241085250541932783191437313053997000
> 17/6000.
```

The exact smallest positive off-diagonal blended coefficient is

```text
322874455580472189418388636281
/464876026084710738962294240679230888636281.
```

Therefore **every invertible affine image of this actual homogeneous parent has at least two strictly stable facets**. Its given metric remains strict222; this is not an S1 counterexample.

The excluded regime genuinely extends the old unit-cap core: this very actual-centered body is outside that core but inside the cap-41/40 regime. For each apex the augmented columns (q_j,1) contain an invertible four-column submatrix. Keeping the other coefficients fixed and solving these four equations transports the strictly interior blended row continuously to nearby pole configurations. Thus a neighborhood in pole-configuration space satisfies the criterion; imposing actual polar centering, or restricting to a fixed incidence stratum, gives the corresponding relative neighborhood. This is a finite-rank continuity argument, **not** compactness of all SPD metrics. No explicit coordinate radius, entire incidence-type exclusion, or coverage of all nine-vertex bodies is claimed.

## 4. Why this does not yet give F≥9

Actual Santaló centering alone does not force the new cap at every apex. There is a useful exact check in the parent's **five-pole seed**, whose order is (base,a,b,c,d). At **seed c, index 3**, the apex-excluded representation is unique and has coefficients on indices (0,1,2,4)

```text
1, 25/24, 25/168, 17/21.
```

The four augmented columns are nonsingular, so its exact minimum apex-excluded cap is **25/24>41/40**. The recovery program checks the seed's actual centroid, nonsingularity and this unique row. This is a different statement and a different pole from the parent's **seed b, index 2**, whose closest-root optimum is 51/50. Boundary q_3 is the transported b; it must not be confused with seed index 3.

Thus I have not proved that actual centering supplies both critical caps, and I have not produced an actual-Santaló S1 body refuting that possibility. The result is the universal strict overload law and the larger, fully scoped excluded class, not a global F9 theorem. Nor is 41/40 asserted to be the optimal threshold for the vector relaxation.

The most useful continuation is now specific: combine actual physical moment/flux compatibility with the four forced sparse diameter balls to bound, or realize a violation of, the root/third-largest cap pair at 41/40. A successful bound on those two rows would suffice; re-establishing unit caps at all eight apices is unnecessary. The seed shows why actual centering without the complete mechanical condition cannot supply such a blanket assertion.

## 5. What was tried and what was executed

I reconstructed the authoritative actual-centering barrier rather than assuming its unique largest pole was unique unstable. I then replaced the unit hypersimplex in the eight-vector proof by the cap-τ coefficient polytope and derived the weakened secondary-apex constant κ=1/τ−197/256. Numerical eigenvalue inspection identified six terminal weighted triples requiring new multipliers at τ=41/40. A six-instance SLSQP locator found rationalizable replacements; **all proof decisions thereafter used exact rational arithmetic**.

The optional locator is included in the recovered source, with NumPy 2.3.5, SciPy 1.17.0, SLSQP, ftol=1e−11, maxiter=400, multiplier bounds [0,100], margin bounds [−100,100], the inherited multipliers as starts with a 0.01 floor, and fixed τ, κ and C. It is not needed to recover any exact object. The literal rational replacements are authoritative; optimizer behavior is not an impossibility argument.

The exact program and a second clean-directory decoder replay both passed. Their proof report, full control report and determinant ledger were byte-identical under direct `cmp`. The new control's vertex, pole and facet-cycle arrays compared exactly equal to the separately replayed parent object. Proof status is a mathematical argument with executable rational certificates, not proof-assistant formalization or a claim of external peer review.

## 6. Complete self-contained recovery capsule

The decoder below contains **all source bytes**, including all 17 inherited tables, all six new multiplier rows, the complete parent geometry reconstruction, exact coefficient-row generation, and both positivity reconstructions. No journal, sandbox file, download or floating-point package is a runtime input.

Save it as `recover_nova_global_cap.py`, UTF-8/LF with a final LF, and run:

```text
python -S recover_nova_global_cap.py
```

It reconstructs and executes `nova_global_cap_41_40.py`. The default execution uses CPython 3.13.5 and its standard library only, with assertions enabled. Optional discovery replay, not required for verification:

```text
OPENBLAS_NUM_THREADS=1 python nova_global_cap_41_40.py --locate
```

Expected exact identities:

```text
recover_nova_global_cap.py
12747 bytes
e21a668e7f1b1b39bc6ff7cc8e4365d16aed00501443b08ccfca2b3e2bd8cca3

nova_global_cap_41_40.py
18936 bytes
d4b02113fe0e7edd5978b9f37d911546c9cd33e732f44efea0fa7e2ed1061110

nova_cap_pd_ledger.json
505016 bytes
88624a03930c5d377809bb7d20630bc06d1889702618b3b18d784553b1a044a1

nova_global_cap_proof.json
1993 bytes
c4efbd6cbea851596456b6d5dc94d5725cc0b31c513df495ecb6db8ca6c30559

nova_global_cap_control.json
22396 bytes
5edeb204c99c56c1fde1410696fd80801e46ccf5dbd10e52aa6526fab3287730
```

Observed terminal markers:


[Encoded source block omitted; the code in this passage is incomplete.]


```python
"""Self-contained exact recovery; CPython 3.13.5, standard library only."""
from pathlib import Path
import base64,zlib,hashlib,subprocess,sys
assert __debug__
B = b"""c-p0WX<On<v+#F*1wL*G1Sc!YNK^zA6qMEVU<^rsuuB30>iqV%syjhYXU_9p=e|ctx~r<ItGa9J#{c~1KUdc`DN)wW3)iQqf|gE|
G+EGOUb_(vg6Y!2?Tm&&=|GSU6fWqv`q0!TX0UHJC;DU&Y%YSP)zYVZ_aHE)u#swTIGX8NyFY5`ea+Cvl;FX55x5?^_Gqa0gQo2m
qnQO1Cf2yGFMbEFOWCW_LaM4=)r(p!SIMR_RaFRjME^!H7>V>phVEK{TE_~GeDaiNaOzl2@M=0JErQ|!Odtr{2djn+@4|r)JKzt4
wi~n^AnyjplhLRZw1?v<%;i7-`A?uV84ZH1iEbcKCuk4Gqlp_l^BRJ>6Fj3Zwrfq?(Wt+IF-C)?J=6&vhlI_k;Zj&*)bCrH6w{;W
5Gc_8vF>(2xPD&=UTMbwp8VFnF$j2%P2I7gG8bF|5*O^~PKP{nozW1~wQvHu;{bO-O*5_Lw5@4@QmT@@s#Sw(@GTJB*PXUDcNf>$
RH?7G-N}t!ocD9%S68m_`@i>PInL{`glJlZEbDR65*1O1DMnn3N>Y?JOwrH{K`>%Gw8e#%CGn;nSDJE+kH=bke4q2iDBLa=W9_ms
I9tkB_oLfHsce<Z>k^D13VcgQMB|1fL`6QzH)D!uHsjH_&bJZ?iC6e|OK8eKPtfJ2Df3ZLfELR%%~nil8mlqJPFEad3Zs5Jt`9Cc
FV~Syg70+uFh;bM;1xX)Hx)B3n}T2oQZ%7k&88$rWl1-cgeb>#_)(e(MU3%=l4v#+(U9ZKgeZy8{f|H`by~=3r*Q=&2g}2VjIY`2
%bCzr)OhPkj+!?wT5>VFtCgKYNz9#D`SMG%xOFjqyJ7CPUTf;zq;SMm%S=zbDOF`P!JfY>+U)AcYAV8g`1wy_vGvBJ9@62d`^um9
cG8tV@^-#kc6#T=^yth;i#zg*B6rNOaFRPd-;=_Lr_;&yak;kLZ&uE#TJ>;CzKb3g&LWo?et4xiuk+Ex<?HcNXx7uujmmv{C)5g^
UK)ujdpEZzl`C7v`I~@xW}l2Jck-<Bw%oFodue4kb~6Ls7(Sf*8C6{;Qq0fp3P-hBZklw{?UO@89_&>`=XU%j5~+{2!p+^()}$O=
R=V1D+TF9oZrnaP-&zVvuk&&fk94*IPUhz0RGYlKy<h0J?PB=wA}JZi&a1Usjab6?ekc1e*RqjWsCx8%=3Fj9(&+fDx|^+?F}u;5
aq%{}H?JDY<ZM_!g#F%fcBfUX#I&P{UgFQ&_+cWNv4A$5O(R>&*Yj$+b05uAbCuBPEc|4?%ZsB+N4Gltx7)Y3v?5O{5iM>$Y~P*F
w?Ce0mDAm~=uv(*efu&jNX7J^`;>co{n&fkt!JXmvt+*2moKjVjK@{e3~Uw3^>FC$VVu9KMa7J``~3W88QQj<9^PNBDv9oSTkbiD
d|0&Ad^8u2y!5kIW@x%lrTgYfX3K7xg<)yIpA8D{-AZ2IbM@}o&35gsz8wuumH6@UPB#OgOqHFt#o=K}zpEVWC0TpQ>^&KiJ9FoG
>sB5cg<SEEef};CZnf%`%ikB(N%hs$ciPw1oaZN#?LzjpUVU$trLYnkO?sp2(&@b&>%Gt3w;g#HQjeX$_$b=lb@J2O{CzlIk<!-A
1uHEoC-PW4N!FXK%)+@m9=`3#rCBRy7n#=EeLnSCNrtS4lZ1IxDJpwOiK(OxYfrPC!(vS7Z=LjxdW*R*KVP<^YOT_`3pnMIvD2Dv
?d@F}$)`@bmcC6!-Ez1yfyob<#d|ATyX_pqzO`CLe=lh%t<j?UTzR_Q(gqLdz1P>H_Dw6j{a{p?!TD}$cP}@7D)j4xSTyPyulDe6
-~=u%<;z%qzEx%}-xACG<h-mroe!V&{_JJEXpWTa$m~2BnKny@WBa|mS7u(L+OVG;b*EdYv+#>_eqYbtns)rE^rx4N*jn$o6R#$n
>ss=-_Iw{5?Pcu4K-=l|y2h&!yR^1<ufxgbW_0Lw6GvO6p%Af*&^tfTx8-U3*(g8Ha+!90nM+k~oJjgKbds!&gxa7LjvUobo?A^l
uS`##!@MB#XPM=#aX%SW<XLU{6nMzol%6{;mAyseKDvktgKqRzR5Qi)V(Yo6wm#;``r+xRl{>lBj^_5o#XzpH?88>{c*`zcjrqZ%
nvwTT`sdT#Grr53jJ`BewM6dxa+WAPZ5>vg-%Tg5?CrGowA}q&^!asHIjjlU=WOvPIj?NFwVmAI@cg}UUTlq}iSt}aWW&QmO_q6G
OzP6|O0IR&r_U{AQmZhp;is#9FDvgoXP?=;(0|pUnY-5gd9P9)2FCZ#@9z&M{9d^JbaOwut=^r~na*YEGNxu;@>*pud9Y4en#{(Y
B2Sab=+9y2*?37mv*}v6lWd9kH(_!6Du%MRVOa}Zy~{h|;5Jt=nbGX|_I|h8W;=txZe^!lIWzRd>5JqRUJ^HvYHI$PuD{k3`SORc
-5E&r@X<?dp6Dj;@6|tgCn@BVc`8v(xI(&JYt4G<A3GDv^sC0@<vb?kO3A}q;p*Cbx;m~WLXpGfZD2MP%iZ!@F{Brj=@#2g%pX2Z
k7gP3w$r*itL2Wx(sgL(sR|b4#c`Ete)(`0zPPd6Xg#+xYfsbiojHgp`gPdIM=R6ABvWHVv7M>pa?y*ZG_Sode**5-AotMBZzqh0
h|`Q5-U!B?v3GQrJP*n2juPsnw_D5dJdtTFZ%4297fxFp-VTym_4nn8vM6j%1XGWNrB3ZCUDcN1d#$)^S*Ogh`iE@}Y(+CV+x<YZ
oWILV?n`IYWcPV8WNs9rSg*cS2Wm9?)L!y8>dZYa%g@^#tLY@iZ2P>t73s~6UoQCEWjs4pF1AMx#k-yK&e?@NZ-=iQvc=G8Jjs;Y
3r$nfa?;TQd!0C&Z}Wxj$DXNQ9KF0wa?<%;vzXd(mTsz@Y|b*(xRN+3p1dl#;c@4FoViZrA9kIhxOkb*#iO00%vM3YY#LFuzk7Xg
{Pup8i#!yv<wfSi&7Uxdyc>w@jOxxbc6OUm?sn78yLfU|FTVF)ohMtKAKOQ_d&<piul$_2Q!3ksmxJNib+ud5b`Q7rw$8#Q+fuXI
>`nJBpCcd4Zh8<KD3^bF)yZjcanUm0%i+rDSPHxrqy51m>ekQo=E8o7b=u+Qc`7U3-pL=S<=*b-D3+C*dVGsHte+;g`Q^RLA7*;S
+n-$eyyDiy=Il87Bwi$n7w4t(r80K6&(h3A^G`l<n@o;(@;BG7fo)4|UWdnWYQ9`tn(R(4omWz^i%R}-cY58n^M}vN^3~b3GRPlw
Yl~3|=BF=&YCL3&s%O>AxKis^9-KscTdmYyMP?^aEEnzug%Z<DjUSG8wXIUW9T=Ckq(U{H>m3`D>Y?+RyHILw%oX=`uK3sXGMBTn
Mr`&Zrbd;@Al<(_*_rN*l-ur3*&W@a^0$SD-eu@=(wfP&`O=7=NnK_6exB~%A5D(x+s$(Q<xe-DT+VLOCpU&|-Q*G{#a^-aW)C}x
E{krcK6^_H_ue8?@$S#A+k0jc%~tNsx$7m)lBJ5t?p<DP7f<-z%cHtc*kfmBXC?OGVUoTB9iAEGhu$A~mfa~91M*FEJ64MyCNkAo
`BYxUD)SOswuc`RQ%u|#^Si4HFlu|PTKZ4>^eTD!;huNRVl8ZhgpY?xH0|#2p;0`4ce1?XyVjsHI(q*I>wMl_*vm!aVN!SsO#-Qp
zA0~o`9-vw9dAdSrN}zQ-SISk)MSdnu)KS{%iq=5-2CFMztuZ?Ef4bP%HYpKE-~4$kC!ja&_}qah8**r8OH{#Uf<cdokeS<ox{6p
_1b)EpJd#?F5_<H>h*C~-%eNRSGQVQe=Q!V)`RpsH`GbyG_`$Iie4>Vo<_53;kEdDXlvrlGE=&&4RRm3nPpyG6ziw<*4DIgQv9Qp
LW7HY?Pbw@*Kf1@QS)YUxfjTXwXwt=J?$)Sl-<L@C=;>`gZYRhj}p5|Ss72a5>o3S7Ygm3)XsL|3*$9)p01UP+u^xXOuSC(;&E|w
@)ilVTcd|kb8owxJGz`Qr%9GAk8}0QS?@d-*wQ|p?X<F|30H+~eMhN3y_fIuH`$3>y&1lBlfA;FT4{asj>}53fT>lW8CTTi{{BIC
WDl8DWPM-_jge_F?13}x+b+Yhe)`h4h791asw&21n#Xy$&Vkd>MI}ml4?5P|wA+>gsH(az>!z&mW=v`cEm@B8d{i<dqbW37kY>b1
Q85xqEY2G(!!#8=4iGV2XzGbpEH1|-!`KhFdb4k-m|Gn{1~eLsCzj(dH0L^i5wQ{Y#j!V7C3wJs0(sF-%+mfZ>`HP=;lYYS)?w&P
%Sgm@MKScaBnVPm&|`7SvLHQ@jD#UajhG>UOOaZV*=&I|)mzd1Ksr^;R#nXX4*DbAbi8pM_YL6K*>4;M*LWnrFs=}T)TXYUF|xqP
JbM^C&DK(?6cIzvd>Fh;l}ag9_ysSKGe$_nIG6xHRde~X8ej>Wz>6{)xW36&D)|hI4{0UCa|-+W5pu<7oD&2^jPslz%LyUD2{9om
i=4=dklJyA5(VbDxEPBHoCMPp8XQ575_DdU0=f(-8KTDp1<@0N0O(RYCIh+<iz-}P0^I_-92Y(G7@`Y_1dcApVgjN^6FfneB|w+O
IM7r?5&EDXx+F>B;{;ux%wsl+=u#{}MpuBB7^H~EysX3lFA)PC=x<39WFMRGE-1W+*f3ATjuGC)7?2csMTsW37_boI;=G{5I0*!#
c-XOjVGBMs#iKMR_D3LKTCJctav7a#vcH29%biY!L1#K(=AlKfHJSwH+#+ZXgG+l%U|52oo8~5lJ015eW*+_rjx%lkh!go2j-dmH
%jsXS+|Zn2A&yRgjmZdh+Qtx!{wOp;%}22j(cu?7!D8{Acx>ZoFXuf8*e1|kj{|FB>wRX<{tg7~R?v3rAy%{uV4OQ!lbAaJnC~E_
ZMdIMZwS_7e|tn{ESW=(o8c_x2exYs9ESb)PKN2*j?0m$v!CQ1H|bC+jey@hr`m1yM@{5^B@?pQ&FNt5Fss>d&S>IlJ!|2pwaL`t
9BZskbaymyRA!%p|9|hZY<T~FhWqTw;u7lC0F3TXA6Og_QB(DXJ0x`|(!(CSPGD+UbKzQG2|-HZi9PhNh?Qo!ua<ek(6Os2J^nY~
4La|!$&`^La31-gYqhNj*f8C+hwb3N9>UCsmDPjZRIQ*j*9|vV$P{2SV+6vVOi9)40Nqb;sN&dVn3$>djR6y4=3wB5qXAa!K>DbG
$><ezQ2tz+(1Pq2)yGGivKgAQ8=Z{}JkVVVAkUb8K^4I!V|@?}DR4vQqCNsHSxf{)AGR%Kh_erl?b*mxQ;)p{{99Rb(t5;WKadKk
<o&Z3+SVrr7T+J}Kp&5-p~>KE5DaHW2DU#3?u7-84j!Dq$Tp7ri;RFx2;BV!93*hvMns*22(w+7P=N@;R@E;16>Z2iz77jbpqx)p
biazi?1IdSKpFnA5j1iIeCahpAu(h+@bFcHU6x%5#q1vONZ*%$+5KVaU2ir8IvW*+qtl|J5mAKvQU5k1`^)SG{9*NepIJvHNIr@0
DhKcE4f$O>-=*@ovrLZa*YgP0*zGvX7{%66(Kh1ZAG3k4L<Np^z?40H`J_4q29ow+umhi}5biu;!>3*9&@sT+Fk^0_@}H(@pV<%l
5gr;O%Va2&&Hi;@w3SF-RVQen*nR2?^x<e|gZDsl3kC-k#UUO=7`@f<FpyXe*9A~8AedtIe+S3Db_wibL}*|yc?nv5#|lPp&yjZ@
lJWuVKnX!sl0cg5KCv<c!N(hq#$Y^sC_G0X?JN0=1A$W&);-U1-Y<cR(+?Rx;t3K@!IK!{qNGWnzZxW*E2c{78+DV$<NkQR!Tz?X
_&73WYd9TPXz{#w?t@CK4-DC@g|GD05+L4ad|=>_1F&<XN+>grdt90Bkt!1UE>iEXNmT{_U!|?lbfTG-HP$Ahk-Pte8dw%0AiqTb
`r>!`(tkt0WltPeGdgzPq{9sKIYYobC2tJ-x#+-&^!uaNFZe54xP~NBIvuY`W|Kq~J}8cd44*#Y%3s@nHM)Fj_`H75!}x0%)GM*T
DX0_!UC=Huo?jUB1i0c%Rbhd05O8uLCz1d8#+qb0mfh~S8WB(va0gT>bY+ZLWQJkZ2taJi!E)Pd!myec&;McqR2D-+ed9kiEPaji
1Ybe4RuIhSZ-hF)AhHX)sS5@Jt^J15JJ95>D?$S>P?bS=_hsDmWK74P;u90T_<S)~y0g&wqhZ^ZpEt_79K3C_+JgH7-JRHTZI>6#
{avs3(Z}!tj2Q$^t%c@xtkJ|8FgSgWG)afhKLay7OBOiIiI77fDnb4uC!(|ilB6U+LZYB}=5-8FBWKOWmH`G3xqD>R^(;5IM?s7O
<v1rnmLo}kn}8VhF{W^e!ee3~MI}sCq!{E`JSR(#&p@6ea!NERN-%f>)V#5F)@fq?6~n|O`kf{uQqgEk<l>N8h>5r;bBY*^#-mY$
W*eyIB5~S0+XzL;bhJ;S9Yqga1a|`eKol`$<w3dSrey*N2;dipE3+G6b$Ljii6@Bw?vfK(Y$FZu<F~E5WCj<oLdfuxjLds<c=CcV
0s1{hg<!F`=IVX3MEX=;7oYltlp%cjDB~}sp{}hvR3+qHQFaX$z{Jq$qeKCP*k1q<hENneK>lA8{ek`LdesYJh3w8lg9nIh$W+dl
1UiclB<(S;o#MwKEsZLQgfs^Fq>WR4`!uWjzl8{_(U8vuw`q=6y}seXlT{yr+S1?Xnj&YY4HgRo+&-~JS|0|pG-G77TDD<ZLm<W^
A_{`AzoIe{qJYi-$gPHxLLNJ7oC8xBvYVPdw&vPcw<l|CdlLFsi3qgHcr!hi>HR5WB`k}<aNjZ^O(3xXvG6J^7rb&Xu}z4E@eNS>
`T*s|^SrlTdmPqEe)6m&{#LP<_~FA~8vVM#5#-MxgaR1*4S+~_;5vd^b9bVXydwqPC;n;rX@|;?(2t?J80<7rv=1H&6DaDk$m1$9
89)BU)w5;+8Z;S#Skw1+Hu240qAqzA?*BKg;H&+2R2t3m-=euVOYHxe$NU|1FsMUIO0r?d0cZdQN+qCczQTDFem8(!iSAkS!d{CH
Z1wx<BZ8hWkVQS(5Z6&9gm9E^j@rw#Qj{qez6P>ZxF{E+B4&DAm-vlU1&dCQj&sJ$2yuQbEnfjX0xIhHb6JH|VSPflIDrg%^tsx|
dL@sX-%H|yU>Qs;lYZ12FpXv-?BG)xp4ea1aW*$3Oq%q62>nxo-gL^o`Gp~g&<<&nXNCRNUm~`DTH?=kUw(A?`9#GA+E10Z#1I0<
2w|Q!(*{aYq?X!mA_UO&P9QR!`&=$nEMTR%IUB+U2Odbe<+A~qI<OU*du)@JkjVZtZz|Tc4YQ1RgNGPE<dKTlh)~Y)5eZQoFLGF}
M7kkqkJY)i1N5JEz{>s5*{Nz7^a=kc>KA?L;Wa%4=b&`29`G}ba2X(Qjff%A(uC1GB%b|g6##8t{SlQEZmIBB?h-2@)L#0D5G-vh
Q!zD`>v9yZ!FraIEOI|DBBoUpVsTpNUbC=j6pXN;de@s6z$PUr$8s6Z*t)viM=re^QcTFRJND1|BogYWm_=eT7bXlM4c4PgqR<}B
#dut$K<n8f+aSD;KDqiC>@yWdvY-AK%`s_#84Gm6xH$X9r|VHwh_Lt-#^cD?NbQ-gITZJoq=)-4mHFbZxgYWZ?rV_DqIZxW0Eu%D
ED#^j*r-SVi<>brCg9)Pg%HCXMcnr)?H;aq6K@6gRvP~QR`JkNF=qIi`aRstVgI*`^=pzVQg8G3{1dpQYX=Jy#Bh*#u2%(m4*R(d
s1(#knZu-jlj9%{d)OMOq=LFnZY$z7#j&Y*+Y0Nn`y72)6;1b3g@T4#M+4tRZ(WkznayaWj0PU&s+O<ivsJB>s#f<m(QuV%+5CB~
rqwE0fPn?6)$U91l)B1j@fgr5A|UOJ3ts0JQfJroik7`gXG^vG^;N2%k%mJ4>QXCJvS<0bH59+PWE-fKDLQ1XX}LOa>|76orBgq^
IUT#@QcJ^;m1S6tO7y{b1_It!Zj|#3pZ6cw8VDx`O;cArM~No~`b6^sTJMv?)oqy?q3fuGt&zcU`edRnHd_18>V<=-r7z=IbHnm3
j%x120?r;u#D@kGBfYg8#1GCIEX^97QGaGJDLkd{i^@&RWPYsshM{f2uFAikM<j^<w~B999fJ2_nC`byD{L2B=S5mPWVx%+&|+zT
*u^`o_`a%(;0va60LdYSiodubsUk1cqF+$P2la9OYx&7JHZ=mlpNp_$ur0MmUDs0em^ma|0inq9`@z#{WcIU)_&6ceIU*Ta7Wd>k
9pf!m8%!A(6^FUOQAbmE-HF)Xpn87^U{N7AtRKS;ReGv~hgUbq#SN&K<>+hAd-X(!l{|g8z<C1UA+Rt-0WQ@?3`>RtY35;kMus;H
ij9%o5)2QI6%LGHmtbi4-^e<#Gqm`i)6jyOZ>Aed)@NY8R?`JkDieKbf{nT1S~_ehuDn*M_%1EguN`^?*p|mE-g6ET0+2}I#(*sG
gNn1oF~-8+Uf3^8f#&=Xi7-JDLIh>;!p*))V9mEINi~-zVLwsQ!l1?&JC69TPQX(bvA}kFNbCQen410yLjK?f(}FO5{uUZ^HG&g%
sDfU&byYV}xB5!eUGJ4$E21M`WapsVajWZeQ*MOvNFQQ(U#a9Z386h<)pr(afW%c1@g9Ieyo>V8hDPZ5D9b%ISf4<P{S+a}1J^nk
0fP&HYRTeS4p9&x?wvLMUdL)-kV2~kNPy_>vE@M6+hF%LT7(8>SJ-52Mmjfa1V6|aY?z*yk-Dk3BuNKdlmkR_{8fqCAZIraFw&2~
XkbB{$dDR18<M=L{lZu+L{cYKZyr&he1jbROa~;Q1^KQcezlYI@Bq-TY)_U!lQTR*V7fT(DJ&48s@`-MdPYuH2mrI|2Sel>jSL=E
O&l8ctHaU5Ym=jg<@lQ-qOR7CkpK;&<W&Pj6MivLi1cv|j^#-MsnACbW6X?-0gCB-?)l8GD7T^@hcYZj!C|?WzcNG+q^4*(4bJd1
G1eylp`p#1jQXUIndZ5)z@<elEpaK;t9%ahF>?ml)tZxH7=g#T5nLoeO2-L>6NJ^9EN~G;^xkAHB8am0!gCN@#&{O@i|btp!HgND
hi}*i3k#JfbFxg%H)NR;MP5OH90r@%6_Gh1reI$L3z4KN5Hv_v+((Nj^vNMdw+yYd@-f;c2;MUy;w2q#*?7Mq0tf733~O0{yCD_i
wWTtigO|vp$O#RyPd-Vt7Ct4Itc*%@UQ}`uh=U!>8JvkzB&He3b54tMUJz==Ic-kkG}YT8Uhn6Mb7ruoWH}+rJl(BrRV5-tq1mvF
Jf>t^IJyg=h4Zp@U`VVNfPFhYlpxu`FhpP*A-O?k4Pl2$V-}!96Fj=UKsK<NF+!0rxLNV$;i!+^v6QHAqU=2gQF@RS<3v2I+Bi6&
cr2-X5|krSy&<N;o-+^*d>#~%4Mtaa#O3h%f_G75fy$b4GwzjJs)&aA0#*8tqW1_Y6h0p%K&l8_MdT_H!J2VX+6#pIhZJry{gteO
Dbgpafb;P%v_PZet%xWjPQL!}T_Nit%EieO_9<8?BWpw<YeXiWc;bSeh)?PfmP$7t6AS5Bi%~*Nj39n7f*69?M?>x}h5eQpiJ%!U
LCBPkFH+2~AcqV}K}sM62`C8Czer?MQHeywkQ<J{uaJ8f%t1?7l0$Ap6r$J^780Z@<OU$!_C}NxXdq0(*r+Mi<30EDSfR|X97m;G
UTqW$wn_^(3x`=c-7Wy&#WDyA7_(8I+t@NIh|h%yFsogI+;|0PU>P291H)rT#vYgnO8yj78A*Tz<03J%X1I+b38GJtBUT{~5NFsS
5^E9TqSR_gs5*|>Ji--eli&fbuxOoPBfCatlLtxB8$Zk`y$|tyx1x8)l<f0{guUMVH2{}zm>W+!^f!)#i3N>K+w4aDGrtz3fj|Md
yn&3q2klDe6pf4B_+dO)re4I?W`E$2HobTQpeAW#`88lYMD0Ob$r%=wU^sATZJoSKEJytkNqiQX2=K}@5>rX(s49H^62#A<ix)<6
pV13PqZjh=HB2rO(K887fL+WbV8}EWSt&&LLW!)V?eT~=PQK~GugSjnmw&!o`B+gaqkPTAcYGG(<dsif)AAQeYn**Dgw<j~x%o3?
Tv@uRHrcP`OmAg1e;yMLG|`}Av;d!6n#IE?YSO_u>titR3K&Fm_OQ@su=i@aLkqRIsuO)HpV~u=54+!4^)gBw$h07XH&rilC8>!$
r)Q`enI4i_9a2F0zCji{H{yCigT(dJmwwX*l4yKa!=^9wD!8`mtk<^CH?Z8q8e2fx<0yzV|F`aM5LJj~)m?f#N)jq$hC?zeIb#pH
c!~yWMMz!Oq&JObn@fgXFa)xG*w6mRtweAUY*m`1#b@yUYcT*Fk@ai)(BXd{76tF0n?knIC+Y0!Oa|VQDon~NTH`p=vAN0=L5Li}
u)Z1}5dubHy2Ob7w0$V0)#6!IqDh!SM8(pOg$N9*(anja_q;L$8D^dL->YtKEq{ZcOLmoZVK)YjU?WUYzyXWEvmt~*ZFC!98rrg<
G=2Y@3HW*}gKf7Yz)o{WjUz*>E@J4MXQDr|?OS&JDhi%*=_HHx3(hpQlGb2+<AAXLi;?jc*S~BH>YQ-7Hq(u1{e9<>!&fj$)?{X3
i7>KmKj_TYPBtjq5eXxs^cWV)da87YcR5w?ta1#~3pv4(o046c-$NgkC^igk8>~?TK^~DpBjVrSAx+(l+a>=z^`!TAR-yp1N0_)M
o6<op%5)^o`(!;g;W5_bUN*H__GN_7>=6wg=$xzSqkpaIM<jp57vkJsxQV}mxXE9}ut5(Xl=>&(*(T)82H}|(HN36}zy1XNN!Sxb
6><Z?KXR_ai^4@4pM~mlt&V?GAbVBIR<No~zI(1EG(pkgTJ{e53-?+jo4&rP)++ThseFI0b;q?-DSL-y>OwsOAn8;|5j2I@D%ZEP
++Dh^=4<(ztae(+UVWqC4O_Xsu1Q+8mIsp8^;$Kb$!b7eiE5cVv|gpLl%6jYzE{bsSr`?0kSNnyF@KdW){7e~iHau5KNibpASqG;
r%?@L=L@3`uQVbWkMOz7dC|;Ta5Nd&rn(*_sWevdh<Ff=>V*MV*IpfCX~Z3;IrP!+gP&u|q^;Bl>5lDapT2ta1PnR0YtJkSOtvf~
J=Xkv?S108pyq?C{}-cy1CWi6zdmoQtGLm<H`t;Y?s53x9P-T;jR?X~tK4+xwX8&4M~aw-l4~TA2F%%m=|H0~i<if)^^e?+HPIkm
AlM+)_0H+gewh+^sD5fot1a}8Pmn5$_XinZ!;BaB$03Geu>AO!8yv$PFAnf;Qw;2-<--wv;C;2muIj~XC7*`vQn*g1YS$I*`l@ih
&ke^18cxf>`D<ilIn%zoD%h^BjS!!K7fw`qe1UcNFBevT7C9YZR<~5xUs$U-z`H76I`viOdiCGCIYHc$gD6XDGIBtZV6X8an1G+k
?|4IP^+&qP;Qb$L>iP|MRz$*$GOsd#Kbqn(Y?^b}@aoOMI1?`oR6j>x;t-sBhx$KVatK!OegJ24c0-K-7yc``C!o?de8&C*1*udY
iD$u1OyPm~$boVgq;Jq1p$wA~Eix=EbmBSb`d2W@d<2-Z>>>J^eHg#niyU=(``rBTH(pJtvXMESZiEnOfs5X!W!Y^=N7hIIL?4_{
zYXNtSVQhGtMOJ?UENq+m(aMGx`Ff+VU4nZc4erM>&cJ{ukqZqxn8#qu~p>A2EJ!pm7B2~LO_s&x}~&W!MZrwM0<qa;9YS)F{u-B
KZiTuA@+?N2o3s80e^Wj^dv7h|4pU9Ar%hhpsqSrB>kntMTCO}J*1;w-Oz13%6p^-kBhOT?%PA_WuI$Jhbj>wAqYQggKJ_K2f(-^
c)Yk64?i*yc%-kC?7(t6BU9b47OLgaK1cs<jCWYrav?w#EUYHt95LyXd7kwy@#5Bd#BctPYeQ^<;y6<StOnT1(WuW%4!l>EqbHT#
%AXt%39#Pr;{+MCAkxI$PhOaLh!#%Q4-OCLGHR@x(b_kDC_7)i?!&VGFezu?x2ietS6A0sz6f5knm^4K^0j*{e{}{f`YN3T=M?~}
tZDd_9!*o#eN7vH1~hG-er?LZix!ji4Al+}f8YNTJo}B`D|;BAx97hcWO#`57=!-79rf$Q+ryw&x>mndvhhm(=kfa59|IzUyc2fc
-=eitVaF31j_Uo<8;*`iezSik=neTVlIp+zstxB)!uzBrS`$MhU!>BsmJPm2V-FxhF}?3nk@%KI8`t#;=z$h1CdRjKNMYNTuT-rx
{+B=Igdx^VwsP->C;t!3a*SL"""
b=b''.join(B.split())
assert len(b)==12024 and hashlib.sha256(b).hexdigest()=="5ccad097b375be6b5a0cc2b4de428acfad268cbb5b36ba13e16eaed182f53be3"
s=zlib.decompress(base64.b85decode(b))
assert len(s)==18936 and hashlib.sha256(s).hexdigest()=="d4b02113fe0e7edd5978b9f37d911546c9cd33e732f44efea0fa7e2ed1061110"
Path("nova_global_cap_41_40.py").write_bytes(s)
subprocess.run([sys.executable,"-S","nova_global_cap_41_40.py"],check=True)
```

Convenience copies supplement, but do not replace, the complete inline capsule: [recovery decoder](sandbox:/mnt/data/nova_global/recover_nova_global_cap.py), [uncompressed complete source](sandbox:/mnt/data/nova_global/nova_global_cap_41_40.py), [proof report](sandbox:/mnt/data/nova_global/nova_global_cap_proof.json), and [complete exact control and coefficient rows](sandbox:/mnt/data/nova_global/nova_global_cap_control.json).
