# minimum-0016

AI research report · 2026-09-07 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# CR62_GLOBAL_ACTUAL_MASS_INTERNAL_CUT_V1

## Determination

**Universal Santaló-point containment in the distinct-triple core is false even within the requested mask 6216436.** This is established here by an exact, genuinely non-affine family covering every real parameter T ≥ 12, with the actual ordinary-volume centroid imposed, the true polar reconstructed, and the failure certified by positive-coefficient polynomials. It is not an Atlas fixture, a free-mass relaxation, or a numerical counterexample.

The constructive advance is a **globally surjective actual-mass gauge for the entire realization space of this type**: nine shape parameters and five physical-metric parameters, with **no remaining incidence or centroid equations**. Their domains have no arbitrary bounded-chart or condition-number restrictions. A complete strict-110 formula in these fourteen real variables is generated below. It has not been solved.

There is also a global boundary theorem, applicable across all 74 C30 types: at an actual polar mass center, failure of the distinct-triple core can occur only across an **internal plane containing at least three vertices and having exactly one or two vertices strictly above it**. For this mask, at most **38 moving oriented planes**, hence 304 scalar tests at any shape, suffice. Their actual-mass tests are cubic in the true centroid before its rational substitution. Supporting-facet directions are eliminated by strict physical reflection, not sampled or ignored.

**No entire type or additional root orbit is declared excluded.** The inherited bracket remains 30 ≤ C_min ≤ 1374, and the 178131 necessary tree-pair records are unchanged. All 74 types remain globally open in this handoff. The preceding nine-dimensional certified patch remains valid and is not replaced or replayed. Its scope and the inherited frontier are explicit in the journal.

## 1. Authority, identities, and preserved checkpoint

The authoritative parent identities remain:

```text
minimum-0010
06cb5b531ffd247eee4bcdbc2b3c02c741f8d3c79a5fde5713f69be68cc0544c
minimum-0009
6f905a98d5d84d11e1369aebb34643ad59248a2485b95270c59bb52c48b92326
```

The attached current journal has 1703095 bytes, SHA-256 `94ef32edfb7b4218c7f9bc4a8e5c1621b3e958ef4634a93fb8cebec3b7d4a7de`.

There is a **rendered-byte/envelope discrepancy**, not a discovered mathematical alias conflict. Extracting each displayed parent Markdown body from its title, removing trailing whitespace and appending exactly one LF, gives:

```text
parent 1: 42227 bytes
 e58e87e3e44baf7986f8a0b14e6e4cf82e366cf1f18fb349ecff6a11f9b76ea9
parent 2: 43478 bytes
 814ac0d394adee09d378431b62164055ea8ff5d9e608a105abb3d3c4baac243f
```

These do not reproduce the declared immutable envelope hashes or byte counts. I retain the supplied immutable identities and literal mathematical contents; I do not pretend to have regenerated their envelope hashes. No conflicting facet order, mask, or mathematical parent object was used.

The preserved late checkpoint is `CR62_VARIABLE_SHAPE_SANTALO_TRIPLE_CORE_V1`: its 31449-byte decoded source bundle has SHA-256 `97dfde71b4bf78f31082d0a328304050e6709597a804ee4cc94ebb03989cbcc5`. Its coordinate box of radius 1/352, three planarity equations, and independent nine-parameter box of radius 1/1024 remain as previously certified. The present scripts neither require nor overwrite those files.

## 2. A whole-type actual-mass gauge

### 2.1 Literal incidence and global shape chart

Keep the parent's Q-facet order, which defines P-vertex labels 0 through 8:

```text
FS = (0123, 0367, 071, 1542, 175, 243, 346, 456, 576).
```

For clarity, the P-facet cycles indexed by their corresponding Q vertices are:

```text
PF = (012, 0243, 035, 0561, 3765, 3487, 1678, 1842).
```

Every strict realization admits the following single affine chart. The anchor is 0,1,3,4, not a maximum-simplex chart. Vertices 0,1,3 lie in the strict quadrilateral facet 0123, and vertex 4 is strictly off its plane. Thus this anchor cannot become singular anywhere in the strict type. This is the parent's global chart, with its originally unbounded domain retained.

```text
X0 = (0,0,0)
X1 = (1,0,0)
X2 = (a,b,0)
X3 = (0,1,0)
X4 = (0,0,1)
X5 = (u,v,1-u-(1-a)*v/b)
X6 = (r,s,t)
X7 = (r*z/t,y,z)
```

Here a,b,a+b-1,t,z are positive. The remaining shape coordinates are unrestricted real numbers subject to the complete geometric guards below; no finite box is imposed.

For each ordered facet f=(i,j,k,...), set

```text
n_f = -(X_j-X_i) × (X_k-X_i).
```

Impose `n_f·(X_i-X_l)>0` at every nonincident vertex l. For every directed side i→j of f and every other vertex k of that facet, impose

```text
-n_f·((X_j-X_i) × (X_k-X_i)) > 0.
```

There are 42 nonincidence and 42 polygon-side tests. All facet incidences are identities in the displayed chart. These inequalities make every listed polygon a strict maximal supporting facet. Their prescribed, closed sphere incidence leaves no room for an additional facet. Every listed point is a strict polygon corner and therefore an actual extreme vertex.

### 2.2 Rational forward map imposing the actual mass

Set

```text
mu = (X0+...+X7)/8,
q_i = X_i-mu,
h_f = n_f·q_i  for i in f,
Y_f = n_f/h_f.
```

The arithmetic vertex mean is used only as an auxiliary interior point. It is not called a volume centroid. All h_f are strictly positive, and `P0=conv(Y_f)` is the true polar of `conv(q_i)`.

Triangulate each PF cycle by a fan from its first vertex. The fourteen triangles inherit inward orientation in this chart. For each fan triangle τ=(i,j,k), put

```text
w_tau = -det(Y_i,Y_j,Y_k) > 0,
W = sum_tau w_tau,
g = sum_tau w_tau*(Y_i+Y_j+Y_k)/(4W).
```

Thus `Vol(P0)=W/6` and g is its actual ordinary uniform-volume centroid. Define

```text
p_f = Y_f-g,
lambda_i = 1-q_i·g > 0,
v_i = q_i/lambda_i,
P = conv(p_f),
Q = conv(v_i) = P^polar.
```

Then **g(P)=0 and s(Q)=0**, where s denotes the Santaló point. Neither `g(Q)=0` nor `sum_i v_i=0` is assumed. The centroid characterization of the Santaló point is the standard polar-volume identity; it is also explicitly stated in the primary literature.

For completeness, in dimension three, if `Phi(c)=Vol((Q-c)^polar)`, differentiation of the spherical radial integral gives

```text
grad Phi(c) = 4 integral_(Q-c)^polar x dx,
Hess Phi(c) = 20 integral_(Q-c)^polar x*x^T dx > 0.
```

Consequently the actual zero centroid of P, not an arbitrary choice of reference, makes 0 the unique Santaló point of Q.

### 2.3 Why this covers every physical shape, not just a projective subfamily

Let P be any actual centered polytope of this labelled type, with polar vertices v_i. Its logarithmic facet barrier

```text
B(a) = -sum_i log(1-v_i·a)
```

is strictly convex in int(P) and diverges at its boundary. It has a unique analytic center a, satisfying

```text
sum_i v_i/(1-v_i·a) = 0.
```

Therefore the vertices `k_i=v_i/(1-v_i·a)` of `(P-a)^polar` have arithmetic mean zero. Normalize k0,k1,k3,k4 by an affine map `X_i=T*k_i+b`. Then `mu=b`, the forward construction has `q_i=T*k_i`, and

```text
P0 = T^(-T)(P-a),
g(P0) = -T^(-T)a,
P0-g(P0) = T^(-T)P.
```

This proves surjectivity onto the complete physical affine-class space. Conversely, the auxiliary P0 in the forward construction has analytic center 0 because `sum q_i=0`; uniqueness recovers the original raw affine class. The map is rational forward and has an analytic inverse on the strict realization spaces. Hence it preserves their nine-dimensional local shape dimension. The analytic-center/projective-centering connection is established background; no historical priority is claimed for that general connection. The coverage argument above supplies its use in this particular mass/metric reduction.

The construction also works abstractly for other polytope types whenever a complete raw realization parameterization is available. It does not require independent mass weights or a Santaló root solver.

### 2.4 All physical metrics and the generated exact system

Use five further variables A,B,C,d,e, with d,e>0:

```text
U = [[1,A,B],[0,1,C],[0,0,1]],
M = U^T diag(1,d,e) U.
```

Every SPD metric, up to an irrelevant positive scalar, occurs. There is no shear, aspect-ratio, or condition-number cutoff. The polar uses **M^(-1)**, not a second independent metric.

The complete generator uses directed true-edge scores

```text
D_ij = p_i^T M (p_j-p_i),
E_ab = v_a^T M^(-1) (v_b-v_a).
```

For Q scores it multiplies by the positive common factor d*e, avoiding inverse-metric denominators. A unique unstable root requires all outgoing scores at that root to be negative and at least one positive outgoing score at every other vertex. The same condition on Q gives the unique stable P facet. For each true P edge i-j with incident facets a,b, H=0 with no edge degeneracy requires at least one of `D_ij,D_ji,E_ab,E_ba` to be positive. All fifteen edges are checked. Thus no triangulation diagonal is treated as an edge, and full normal cones, not merely edge-foot projections, are used.

The resulting QF_NRA formula has fourteen free real variables, 5160 derived polynomial expressions, 195 distinct positive guards, and seventeen mechanics assertions. There are no free centroid/reference variables and no residual incidence or mass equations. Derived expressions are definitions, not additional free unknowns.

For comparison, the inherited adapted-corner rule gives this mask fifteen variables and one residual incidence equation: the exact graph calculation in the new source verifies `max s(c)=2`, while the parent rule is `17-s(c)` variables and `3-s(c)` incidence equations.

**The SMT file is an unsolved complete formulation, not an infeasibility certificate.** Its arithmetic directed acyclic graph was evaluated exactly against the independently reconstructed rational snapshot below. No SMT-solver SAT or UNSAT verdict was obtained or is implied.

## 3. Global internal-cut theorem for the distinct-triple core

Define

```text
S3(Q) = conv{v_i+v_j+v_k : i,j,k distinct},
Cdist(V) = {c : 4c-v_i belongs to S3(V) for every i}.
```

The inherited eight-vector theorem gives

```text
0 in Cdist(V)  =>  S(P,M) >= 2 for EVERY SPD M.
```

It excludes a weak escape tree when `-conv(V) subset S3(V)`. It is a full-core theorem, not an individual-root membership test. Its exact inherited identity is `minimum-0006`, SHA-256 `4480a792dec44a82e252175c8263360cd2cac11c705c881fe30da85b47087f08`. I use that previously certified lemma, rather than claiming to have rerun its finite matrix proof in the present new scripts. The old patch states both the lemma and the all-metric implication explicitly.

### 3.1 Complete moving-normal reduction

Expose a facet of S3(Q) with a nonzero normal n. In the ordering of the eight projections n·v_i, let m be the size of the tied threshold block and k the number strictly above it. A two-dimensional exposed face requires m≥3 and `k<3<k+m`. Thus k is 0,1,or2.

If k=0, the tied plane supports Q. For a facet of S3 in this case, m≥4, and its support value is `3 h_Q(n)`. But P is a nonpyramid at its actual centroid, so both P and Q satisfy strict factor-1/3 reflection. Consequently

```text
3 h_Q(n)+n·v_i > 0  for every i.
```

These supporting directions cannot cause core failure.

Here strictness follows directly from the physical cone formula. For a P facet of height h, take a minimizing vertex a with height l and cone the other facets from a. Actual positive tetrahedral weights give `4 n·g(P) <= l+3h`. Equality forces all positive-volume base triangles into the opposite facet, so P is a pyramid. A nine-vertex pyramid has sixteen edges, whereas this problem has fifteen. Polarity transfers the strict reflection to Q.

The only remaining directions are therefore **internal planes**, with m≥3 tied vertices and k=1 or2 strictly above. Every such plane is generated by a triple of actual vertices. The directions move with the shape; no fixed vector pool is introduced. S3 is full-dimensional because differences between its generating sums include all differences v_i-v_j. Duplicate sums and changes of its face lattice do not invalidate this argument.

For an eight-vertex Q, the number of nonfacial triples is

```text
56 - sum_(Q maximal facets f) binomial(|f|,3).
```

No triple of true extreme vertices is collinear, and distinct maximal facets share at most two vertices. For an internal plane with exactly three vertices, precisely one orientation has k=1 or2. A larger tied block has at most two useful orientations and accounts for at least four triples. Thus the displayed number also bounds the **distinct useful oriented planes**, including all nongeneric coplanarity strata.

The three possible degree-surplus patterns at C30 give:

| Q maximal-facet sizes | Internal-plane bound | Scalar core tests |
|---|---:|---:|
| three quadrilaterals and six triangles | 38 | 304 |
| one pentagon, one quadrilateral, seven triangles | 35 | 280 |
| one hexagon and eight triangles | 28 | 224 |

These patterns exhaust the boundary because P has nine vertices, minimum degree three, and total degree thirty. This is a continuous, all-realization statement across the 74 types, not a count obtained from representatives.

### 3.2 Explicit actual-mass cubic tests

In the forward mass gauge, take a nonfacial raw triple J=(a,b,c), either orientation of

```text
n0 = (X_b-X_a) × (X_c-X_a),
h = n0·q_a,
c_j = n0·(X_j-X_a),
Aplus = {j : c_j>0}.
```

Retain an orientation exactly when `k=|Aplus|` is 1 or2. Additional c_j=0 ties are retained. Set

```text
n = n0-h*g.
```

Because every lambda_j is positive,

```text
n·v_j = h+c_j/lambda_j.
```

Thus the projective mass correction preserves the above/below/tied ordering for this moving plane, and

```text
h_S3(n) = 3h + sum_(u in Aplus) c_u/lambda_u.
```

The exact core inequality for apex i is

```text
F_i = 4h + c_i/lambda_i + sum_(u in Aplus) c_u/lambda_u >= 0.
```

Clearing only positive denominators gives

```text
G_i = 4h*lambda_i*product_(u in Aplus)(lambda_u)
    + c_i*product_(u in Aplus)(lambda_u)
    + sum_(u in Aplus) c_u*lambda_i*
        product_(v in Aplus, v!=u)(lambda_v) >= 0.
```

This has degree at most three in the actual centroid g, with the raw shape fixed. After substituting the rational function g(X), its total shape degree can be much larger; no low total-degree claim is made.

Combining the normal classification with strict physical reflection proves the exact equivalence

```text
all useful internal-cut G_i >= 0
    iff 0 belongs to Cdist(V).
```

Combining it with the inherited eight-vector lemma gives the new globally specified exclusion region:

```text
strict shape guards + actual forward mass + all internal-cut G_i>=0
    => S(P,M)>=2 for all SPD M.
```

Equality belongs to the excluded core. A candidate strict homogeneous 110 must satisfy **at least one strict G_i<0** on an actual k=1 or2 internal plane. This is necessary only. It is not a sufficient Gömböc condition and does not replace the coupled metric and full-normal-cone tests.

## 4. An unbounded actual-mass counterfamily in mask 6216436

For every real T≥12 use the exact raw coordinates

```text
X0=(0,0,0)        X1=(1,0,0)
X2=(3/5,1/2,0)    X3=(0,1,0)
X4=(0,0,1)        X5=(0,-1/4,6/5)
X6=(-1,-1/2,3/4)  X7=(-4,-T,3).
```

Use the literal FS and PF above, then the actual-mass forward map in Section 2. This specifies every coordinate of the resulting physical P_T and Santaló-centered Q_T without an external file or numerical root. The anchor is fixed, so different T give distinct labelled raw affine classes; the gauge bijection makes the physical family genuinely non-affine as well.

The symbolic verifier proves all nine positive auxiliary supports, all 42 strict nonincidences, all 42 strict polygon-side conditions, all fourteen positive polar tetrahedral weights, and all facet incidences identically. Thus the actual face lattice stays exactly the requested mask for the **whole unbounded interval**, not merely at sampled T.

Take J=(1,5,6). Its exact raw data are

```text
n0 = (33/80,-33/20,0),
h  = -33*(5*T-18)/800,
(c0,...,c7) = (-33/80,0,-99/100,-33/16,-33/80,0,0,
               33*(4*T-5)/80).
```

Hence Aplus={7}, the tied block is {1,5,6}, and the other four vertices are strictly below, for every T≥12. The verifier proves

```text
F_3(T) = 4h+c3/lambda3+c7/lambda7 < 0  for every T>=12.
```

It does so by reducing `-F_3` to a rational function and substituting T=x+12. Every coefficient of numerator and denominator is nonnegative, and both constant coefficients are strictly positive. The reduced numerator and denominator each have degree 21. The same positive-coefficient test verifies the geometric conditions and the required denominator signs. There are **115 exact positivity records** in the regenerated certificate. No sampling argument enters the interval conclusion.

Thus `s(Q_T)=0` lies outside its distinct-triple core throughout the family, although P_T is genuinely homogeneous and correctly centered. Core failure is invariant under invertible linear maps, so changing the physical metric cannot put this family back inside the core. Strict geometry and a strict core failure also persist in an open nine-dimensional neighborhood of every finite family member. This is an openness conclusion, not another advertised small certified box.

### Complete physical audit at T=12

With physical metric M=I, the exact ordinary-volume audit gives

```text
Vol(P0)=Vol(P)=73839083699649536000/30731258686139807367,

g(P0)_x = -7937326141517415514462881882/
           93213213535905242292092425307,
g(P0)_y = 25552538009378729476663599858022/
          304154715767658805599097583776741,
g(P0)_z = -43246727249783248073279231213822/
           304154715767658805599097583776741.
```

The centered P has g(P)=0 exactly. Independent integrations use both an arithmetic interior apex and the actual origin; their masses agree. The true polar Q is independently rebuilt, and its ordinary volume centroid is explicitly computed and is **not zero**. The full 72-pair reflection audit is strict.

The complete physical census is

```text
P: (V,E,F)=(9,15,8), (S,U,H)=(2,4,4).
Stable facets, indexed by Q vertices: 3,7.
Unstable P vertices: 1,2,4,8.
Saddle P edges: (1,2),(1,8),(2,4),(4,8).
No degenerate equilibrium; none of the 60 directed primitive scores is zero.
```

All fifteen true edges receive the four-component primal/polar normal-cone test. All maximal faces and true edges of both bodies are independently enumerated. The audit contains every exact coordinate, centroid, directed margin and edge test. This is a **physical nonwinner**, not an apparent 110 witness.

At this point the internal-cut algorithm finds 36 distinct useful oriented planes, including both orientations of the accidental four-point plane {0,3,4,5}. Four cut/apex rows are negative, all at apex 3. Their triples and above-sets are

```text
(0,1,5), above {6,7};
(0,5,6), above {1,7};
(1,4,6), above {5,7};
(1,5,6), above {7}.
```

The last has exact positive failure magnitude

```text
-F_3(12) =
12219000078890914241788332604308379253901532371275129/
26693874583022287624925721798017057523312749509114800.
```

## 5. Boundaries and precisely unresolved region

The new mass parameterization covers all strict labelled realizations of mask 6216436 and all SPD metrics. It does not claim coverage of arbitrary nonmass references. The old all-reference affine theorem retains its different scope.

There are no maximum-simplex anchor switches to discard: the fixed facet/off-facet anchor exists throughout the strict type. Maximum-simplex ties from the old seventy-chart covering are therefore included automatically through the surjectivity proof. Values b=0,t=0,z=0, a=0 or a+b=1 violate strict incidence or polygon convexity, rather than describe an omitted strict realization. Every finite valid value, however small or large, is included.

All h_f, W and lambda_i are strictly positive by actual convex geometry and volume integration; their zero limits are not silently divided through. True facet-incidence changes or rank/vertex loss leave the specified strict C30 type and are not declared excluded by this formula. Accidental internal coplanarity, tied sum-hull supports, repeated triple sums, and internal plane-order changes **are** included by the complete tie-block rule. Metric limits d=0 or e=0 are singular, not physical three-dimensional SPD metrics; all arbitrarily ill-conditioned positive metrics remain in the domain. Primitive score zeros away from an equilibrium are allowed; actual degenerate equilibria are excluded by the strict-110 mechanics conditions.

The unresolved homogeneous domain for this mask is the full fourteen-variable physical system, further restricted, without losing a candidate, to the union of strict internal-cut failure cells `G_i<0`. The generated SMT file contains the full physical system before this optional necessary pruning. **No assertion is made that this union is empty.** The unbounded family proves that its geometric/mass part is nonempty, while its audited member shows that this alone says nothing sufficient about 110.

The other 73 types are not newly solved. Their complete internal-plane test counts are covered by Section 3, but I have not generated a new fourteen-variable chart for each of them or changed the combinatorial remainder.

## 6. What was tried and the useful continuation

I pursued global core localization rather than enlarging the old bounded patch. The decisive discovery was to remove Santaló solving from the forward construction using analytic-center duality, then test the actual mass correction itself. An exact unbounded family disproved the hoped-for whole-mask core containment. The remaining effort produced the complete internal-cut classification, the whole-type fourteen-variable formulation, and a clean exact physical audit. Numerical exploration was used only for discovery; all reported conclusions are reproduced from the literal rational inputs and exact programs below.

The most useful continuation is now to couple the **strict internal-cut exterior** to the full reciprocal-metric system, starting with the explicit k=1, apex-3 cell above. A proof that physical 110 cannot occur in every such exterior cell would close the type; another attempt to localize every Santaló point inside the distinct-triple core cannot, because that universal assertion is false. The supplied family and complete formula are reproducible boundary/control objects for that work, not a solved branch.

## 7. Complete recovery capsule

Executed environment: **CPython 3.13.5**; `cr62_global.py` uses only the standard library. `family_fast.py` uses **SymPy 1.14.0**; the installed dependency was **mpmath 1.3.0**. Assertions must remain enabled. No graph library, optimizer, previous filesystem, journal attachment, or network retrieval is needed after recovering these two sources and supplying those dependencies.

The capsule below contains the full source of both programs, not merely hashes or artifact references. Its exact input includes FS/PF, all chart formulas, the unbounded family, threshold T=12, the rational regression point and metric, complete geometry/mass/mechanics routines, the internal-plane evaluator, positive-polynomial verifier and full-type formula generator.

```text
cr62_global.py
13225 bytes
0b13528e0b40629b373d761d2f27ba64f5fea73f518aa5a44aed6f3c7c685cd8
family_fast.py
2613 bytes
cc8d964bbbf2772e2d50ac53a9026304700f0be04e8815a0e7e584e0d058c6c1

Decoded source-bundle JSON:
16193 bytes
cfb7360357323745995109866742e6c5cbc84b7d34f03987a5bc8d37a5444418
Whitespace-free base85(zlib level9) stream:
7949 bytes
138256e17bb8e2e37db843ec1f52a526e6cac386482638a9db635535c033c301
```

Save the following complete source as `recover_cr62_global.py`.

```python
from pathlib import Path
import base64, hashlib, json, zlib
DATA = r"""
c-qxFYjfJjvfuBo(AirlNoK%2{0d}JMQq4sZ{ioW<1FT?1QH+{Bv}#|XKVla?Z@Z=*h#j|`EqwF);xOpG1Jr2-8204+bBAyTa#HZ
v}cv@`M2h8cl7`9B{YBheD<OJ*=iqOUBl-~yVtWmonCb=PoZ{veP!L$D%$b+b21Hltx>5pD*Hl<6KCcPD|i0o!q=X>WUAS5>_&+f
_;FJU8Mxfj*6H5)S5sG;xV{_NiR);+FIRQVi#1yt2hn^nvxRngcBR?Ac757wUuh%6IQB*W45XOlJAWJnb8Q^iBci5x^Du}Kt*aV<
5v{9$yaW&g!7KwB1@ocj+cZ#Up$kNltQG~%Vw9+%p`A=Y!gSy{RPTIMnc6Y-3GF@(eBjIP_M~A{MNQO2!xT_zhy!s*r9)AJZ%yor
JyEC9q1cCS9qI_%fbRi(_W%OF`_O-2ns@$rH^oVKQh3C@PhWs1+zlK-ZHViL=+=<FIHJ-KQ3i~s?Ju34)NO63EwrT;X|a}Q&)Rpb
t$omrHAi#xN*vC-!~o!4`^)*~j+}XMV$AK(=n6w`?C$GAukF_1Zx#NPYrA{&;W9QiR11|ASo*I<|4d}XamSkNIEF2TW>bsYWD)sV
vIu9cu_`^IHfSsHta-ln-3tjy4T=}T7YCJpGzc^cst;R(b{=>T4zU%i6C~>d;>8>we}sM%1#!GS$gumh!OpN>ACztQ1EtzPs8SW%
s@yA7sfKMe?oAnSi4if%u`+K=4m%X&5?Qo2r6a!k_k*H{RKCY@Wcw4>Xrw4yXX3`jI4+0{itakbUkVx5SZYQyMl|D?%Fvw7%UF#2
wdSBS?l)@#^KXSei98@U+n~`m#vm^Yc%VNe7_f!<A?LOxX0C6H&2r5g-1!$B$y|4PW=lIyYv)}c$+k#C@QaQqB^J)HP}>LN;!sD<
5)8qvJ=n+X<4^6+a$V@8C~&t&<pj$`V*+wF%)jsa)NsoFeLmT1fGi7a&4#IYV*v02!p5`*Ys_;SGIx~mol=0-#t|AHQbF4fe6W)<
!;OV+Ht#@L+==X?5_pK+C2m|Q#w?GQ&#aFVstsqs=pmN<zPH_vtOCZqH;~d{opP{W%~1@>3f-oN+@%}EuDpsCE+GwVFN)cWyf6*E
iKeNgbtGZ{&RW{gjT3nq_$~}aGNBzMF_KdD+1N3PcH0=TG^Btmfl2afLFBlR#2GM%e8_+y;X<UQ=;LP7w7DHW5Mb@yJ2nXq!tlhs
Nz>&o=5$;cBnr*M`lcX4Ff)P+_XFG_FtS6)Ngkwt1F?b!9?GY=v)I+<o^N2QKoA_D_6D|Px{xpLMF*_9ln3?N!CvDa1DM+@+VH3#
{lZ$GcaW-0atzFJgLiAbuy0=wXC!PT0Bji=Fxnh|q(&QRMf<A(|LUleqZx3fowPr)DvmYF@_a9`EKrr%SZGUo7V|P;z2XOs3z|1*
adqy_1NqnAss^wN=>5xYE{U8kmZ`O&BTW#p6ne6-BL{IQ!gdnOndpiM0{>p@`Eg?VBRB*^oJ6@vS|P+rdVXT8Kp9hGm_$&;k*oKz
$_u9(W$le)>Titl%2c$7(@kPzdkcazQ>1xQe>F&fE5H}%Cc0DxlF-c*zH5|;t$w3f21`lGm33t-%<TuoK@f@^JDR9z#**ZPrbb0C
2&L3ZI$0Mur0JM|?vy5$;anmm!eSM+KZ4N=sFot8GGkK12zCwC>(Gc<4NFJB;3D+St6aVUSo<|`YA=do&%kG>%wXj~&45$0;>C_P
LFY)rJ+!?}`QFNB9ZyDy?o+<lf_hs;B_I{GOT*%VFiYiOak98=XGn|p;66(O*0{Ku(3T!2**;=Ee0%OnJ$&QnZ_q~Mo6c-ykbM|F
kO<kz`zv-Bx;~f%Y!@j#^T)y!RU5|*<Uf$Epx5iHDGdi({KNfxne7<0nQ?cd^L@!f^J!mIlzk5(bFJBN{a}vA6?CMVYm!nHi9KQJ
D@lWpDKr=b6O_%I{$3YAhQ?%!=*D~PO{`VHfIy$ZAA1u&r4WRf9J&FJ3K*BXK(XSRsj<C$+0;&iFC5fzFmlYDoG3nh>8la};7t03
{q1D<z*SGt4O#3Vi#;JWhGuJ?*3tf`RZ*Dbu;Mh=roS=~a|6_X1@XlYq~Nksv}zl`@OP&$#4%M1j7|reMIeWO5TRv7B!N_tWODiL
M9F1taafQC_rE|Zqo@~|Wke8`6eg&ky`}QnJY@r-S4U*9JTw~tLCil{gVqa^xU)Xvugw)vl8RzRKLL-<@s>Z~LDgWR422#Bv6pyD
*Me~#xEJ~hdh!!Coh>$fvvAt3ubo1jpTYpVyWNQE#%}X);msU_4V3_HNhS=s7GfzP5sO4Ti|?W>K8R!C2v;(w@=VDJpsmHYNVj!}
wn6A2e!<+8YtV)ttS3TG@cUip-|_1R-NCObbQdDxCeSw6r~vL;3jE=J3g7vQOjRlDuc>d9f`4SRR$i2iTG=*tmb*h}BgXN&^L>{D
pc$LHwl6Ufrf~7r6kW^>fI)i1FkuMf5yH&F#oIya8@gnE5Y55CVvmYq8ZlmXj3EMJ9|O3AxO60qTX2W-AOd2+#=vYbc@AHZBEZ@<
>?J6UMp!fjgmx*t)O`A65~dP^Utc`-F=PZ}IAc?xPw_;%H(TFQaCUK)yHg@hjv{N!W=wOWPG~$n(nE7h3&E5q(_jmf1Q^rN0ry89
oC=Bc#<7sBaWA|aH3|Q66wHLOXm-qXI<Qm91`TILC^G~3MBVm>!vSz&+XJ4iTa1{wj=YV6$af=VE9K0_ga<PBB>QE|CF~gA))oc4
US8}Z;%XrrPFLC!tM!$BN>x=)+yp6kNa8C6PfxrkUxoe^Hu?uUdX}VW{Y>fln;d{RPfsZqP)w(9jT!M|QkXVT?(1sT*xUJ9P*fxZ
v{{XpVq)e?{|zOX*>l;i(X6ibKE5g^49O&g^3bs}VJ~Dq)v;BMYPnQ+my8Ofcoc{xr?FhF6S-i;pxlB8!;N5*={HKm_7eJGp(A%Z
b1BQ2t+Xe`nL#|iHkPR|G?uVWO6{E`_`9VK@Tm_3m5<YMeUOg3*c?ZYWgJ{($nr5GGTJ-G<qsxx;OH>SGlb{YB1CiYm^WQqiwkIi
a14Su4B`IHCgYxC#%u;u3dx|jTkzIuI&mM`2ekK5i^8yP576#yB=E#TI_IbY00rBHV9A1l;WjDjSR{S%6Vh&h^y4Fv{UJ>N0h$De
=6%N%u5c7pbvoUONAV5Zu@KclTnHx?aO!+b&!Xu9B90qUiLpI`$-<0C$}}YcUr8mQKYwFlK8YmqWo|fbkg1z~YBp~ABUOci8Vq`F
=$5KESLmB!AhePY^=A7mhI4Wh_=)E)Qdf`i53%_UzyJz!8c>5!xk;i_FxAV`=e@k&V$Q1|o#K?KlmsD3ldV&C^kDI1iLpAdISHa>
P|7rMS4?Y+*VC3rBuyDYtyM_6-I!(kbj%W^8)Hss6m_T5RNz^9ZA=m8Jr|2)3S;x5N39qw*Ua-DcwZF96^^FDfpIU#6%S@%Wq80b
1YhI+eYu9YQ{%o=Gv9D}bkIVa6;L0TFMBb=oH6N=N$UVk+GhW-*l*K`rUb;rr+5(sAqFWGM+n##GWZ0HUDs!gZ9yP5dXRnJT_pxy
z!(T^k{#5Zrryle2!dsLkW{IJL1>t%&<}YK>-tUnL!3P*+!er#M?K<&gRqPMMW%@tVumQ^>eNa1+8iKBeS{slE6O&~YM{D9Lz<y$
Qg3#A-LTK3RuAzmgBe7ZRd8#AxiqjO%$<f>@Xd2|oMvKhFH6{r8>eyWNzy^hR~$&1ckQrH9&y>+Jt)Zg^uF2xPD=8L_`s=xugLf|
aE#!)1UOB1_ljE#2Bwy67s~lA2Nao~Y%d&4d?5Rq={4oKn(3BUy|1FX3$gG<6r2doqVZ{EC$?non=hKk`)<8rA|-<7`@CQRZUy+B
QeJdu{}nneUh4=2xD-;JcYfx~Zo7+$Jo$%@nD70Dxn3!2X1-H7a^3)WSIZBd4QjwlM(w_sW?iFpfvCbFwfjwKIS5l*R>h<$NzuQd
$gO24CLuS3-0&zSkK91Bl~3@pD&;bi^6TyaO&=hV6D~okicPrw_^-5H7>-K!Xv*y#G$*xE#_j~g*@dNE+Y0G?Z(<}rlE&3`*Rh!9
_UOSH{r}c_E*x2o&>Zkhz>!DulDLz|<||{|^md{pQ&+P`$-<s#BXIPiz;h}&7unp2Y^x&?nph-qEw^t@IA4x(D_`bawdiv=F?CDn
k$vpFfZ-^^;J$>xUB}?Klk;C<L%zlbt!ow$T`Qy)zr>k*jkR^8Jw)n87+n62e*k|c4=>k!Lp<jC>7~r}<|*vF`~)7LcY~4wssR|0
KDcxPp_s%km{h*`aii2e{iUNbpf`DpjxI+MLzRZ;F@#tyR5Q;OY?%P3g)TVPJfLdx_sry>KgncfYd%sF1>S;ET849kt4Q*w%0;o#
$*ux>?4n$=!}7awHo}?hlds(x+g>ql{{tr{y*^}LacIY`EC!l?fR~S<<sTGfi?p#`Xv`vBHza2OjzkFCRhpSjOF}E4+ic}=I}dJ+
if-pBN4l1GXlL5C=_roWEez-Bv5ca(%`A?__Y!N~srIM*q3b!yJ<k^9)c;iHVcX0d5|{4%d1lwKv$>EcjZa7JL`=cG4x`|nC1n6O
5OWDH2CXCrDQH&SDT15*a-%s=nRV6$gp!S&X^Ae}z}RgW%QnNae#-tHz!u=txCPf2JZ{0`UND(in!*#^>V|_(1k@_iRV+9@H6~ub
+Qgn6$<(;>qXedQn4cZ&CI+drHJTeRs?3q+AxYMcOS1fzTr|UwX)P5k?PE!zxEZ;S+tqY_l(JhbvO+tl3#VIQq3}#GOEB|UlBQdI
hk=Zj=cM{%2mUZo$3<Is<l1zrrdmDL6TVLQOUE0e8CaG-gbv`|Eb#Rvj?)tlP0F7_w}-(J0NStF8J>H5UZ54?6s7|91fKzDe@J>{
bbx8L;)dSGja$pM@`0)rcV-Q9bN;3ZQyl8eWSR3}K1@slCZ?dYs(nqfl@b^186m;-tk-LAtMK39(b3!L+uB}zuLi|Nqkd4`YgCUK
hi~iqjknd>exu$vtkn<qYxTFHesJ)%adf!1f7Gbf>-D3<gZdu89oB1yZ;z_A!|MLwe!bBE@V&SDfVH-FRIQrttK{I~V=Y(!O4@nJ
v)<Hy@x7Za^eeqts|!85dAIO>UT><4ccEWc6qV}DZcpgvX$5=(=%KJuZ(ek;M^(<Da;rCQg^p=fD-33KgnzN`QRtEVWS#5HZ>nUa
?uXu-01~|!f|iheS{HygO-g~HfS(LRz;lP4syD$G(boot$WPY$h_ym5)FGl8qIQB53qP$~Lpy{KSo~e+aOS8NdvG4&(IoIl!ap52
8XYfkN1zVKejiUyp$^_b@ib3WCN_&hF47_H>qA@`g0pB*7y_Fo5;_MLAOd}bj^144!}Rd3P&<e#d8A6IQrAM2T+lwFU5ygr%^N;R
v?g}Q&1<cklh&KQkDCydNE-O|ui`A`VQjFb2^CID+OyDLfdPo=B@D#Zp-p#;;Fo}M2~b7TEa`W5zHU}re-t<_M9%og(9jD{CRySN
k^;D=2*PP=_?)<y`gx-KTZB&n^v*3PGivhxDE&;8`?zy@b$Ryb#Ohvu{%oC|U4FsFv(t`s4r;Fp_96s(5rVx4(G%C=_X76f=I9j$
Dgz|+)6U2C)u)?|b$Rwx_0hya*GZ@M>Emhps&is}Y@h1_+Y6}M*C(H@cmzr$)XU0BJhkil2h>)Xx+}+nJ(L*5xRpaf4o_3{H0ZeU
M*RNCp2(B-M-^Y1t@wE^`<DhZ3w6ukqn6PN5^zEDfD`})KvgD5njaknb67r?pZINGIoo*UoJKgPYzBB@!_4nngQTZO>|mJb6M@{M
+v=?v-|%l=D-Z)2H*{n0G8xAkCF|(z3Th*9rb_FV5_XOkFBgXJN8yg$OgI)R1;jZM>69xUGYEyBUW?Hr(*8^lU<+Tw`Cy|F4rdsH
d<yaVht0QxY|j0AV-*+f!0Am#N!Rqsec<`nSJF*gfkRlg0S?T(3cc{XM_}SaJ(bIJ3X$}Qvige*)1~~03IyJz?>sofIZ+W#6a>k@
9F+QuVr$s@mxp-+^W~>@-oF$|>c-;QV?Dml8%=FEn!xK*;=n|{HHE6Uu{bjSgCP~YlS@gae$a-rt6Wg>27VfXv7<2aFkb2FE$tVN
=az;CdgRi>J!SDKcthXPy8Mn@3;fx0MLP{}sqsZ3MD%emgOUdSaCcBAn3>SkhQY#jVnToq8OyU^;*GS6u626ZHuXWuVF_3?9Cri<
w_6@Be0-5%nA)Xl&rJP|ziCo7hK-@TF-qfS9VWi&@bPI)rmc7vs-C*xiyJ%LP4prMG3V*lAMZP5tnkr@Z?0ukbKcTKQ~Jil)LKyB
mnQsZ1>)&62g{huHQ^KjkVJnoCvN7HKuom-wuNp`3a%X6i3z8l;jX-dr<TrAItW>GLi@v`alDw#tmHX#EAc$3zkDt#mY`M{!RjW)
aDC}?dhkp7J<Ml7>gg20z<=9=#1nt+f?EQ92ES9($C2w=5iGs6v?C9FE$FN5q5DEt%Olrv9~XSPqc^MID*|g9O{B9H>ntD+d>36x
2r@>%-Sz)offchS>efrU#wUy;4`Ll~VQFbDbaZSY*c1-BpU?Qn3HTw+0<Q@UpG?ur!V8Yn-{Qw(u5ThywZ2yV(+>v7dH@R7h}VYu
=$PkLKIHZ0PY!*dt1S!iot|A;y|d3Zof93epyLE&07qgYU{Xgu1x!)&lB@Rbx@YR=Di9R--Wb?;(M5|2jt==>SKrP%R&CGfUUoXx
P5bgw`@`o>&-$}-c?SA({OP1~dfeeE=~U<98vLrW)1uQ=Se<Mw3Uu%nHUGe$YNhOfXL$X&4P;M0bvwP(C5yH(M4JxT9n1her2<{I
EGcyhCdKnDOGo3QyaTB&5L#QFTF!ZKV_kNR&u%)G-&k${`c3>cw&&jL8GLt`ZTbb1`Y{f;YvD8g=%@E9Kl=HFU-#frrefduSF%?D
5<|deKu~D5B51fIWcKX;%P)U!^DFsY<%<o*VkNfU7)1sVh$x5l;%lR-C}Zy)0wG~&D%ZHJj%~mOwe5-W74S@VJuytH<ZxB{-t1K%
QihENe2manof-5xi5@4>yCl)8e0L*!`2ZBn-J?7IQTA751SqBm?|gcjq~(v3T2oGS7JjOczUF%UK~mWmmTj}b36l{NTT_V)8(=Rm
B}8=17v3ZRwX`xVygoAg-KmL{*)tq7BLi`vd{4;W2U(P@!0CCnsgCiNf9+DdHe7!~v;6}av$bRi%DoESCZ_9MnbO^<`biOhJ*7M^
&DMvKT<+kbwG!^guZ)1-^uV5##s_|Kvn3hsepuQD52%$N`;7rj96oe~j>Ej;FzdMU{i>wQRGCsyYW6WV#SN`#RV_lb!WU^I*T{=T
vR~|2F}%617+oblusp4na1?Nb3D5>t4ykg8j40D{+5T#se{P?4!0h2Z@j>UORe{iAJX^$5{y9qq-#zJk)WuF8XLtffIyk;p1tvhp
)o&4vt~pr8KyDB#D&3w!A2>r{B+!1E%47;~1!MsW$%9ZPCF**Wb2zxsgjV9kFgC8lRjCI1@5*dBPTC77HhcMk+i@x`#;8@is{m|e
-^XEP2h*{^gQWK!?~Cs}d~p51<r)R<cnoo42{07ve7OTa3hnzUHRN<C8>f7%;6d<9^2`vhTo_i;)U3ZZ@2g*4yvEC58)Aby3Ne0k
(MwA(g#ZPwc@`la0ag%s6F9^45+c9PpAK!k9$aGTpEQyU1YjY}yya(#Wqv)FrVRKkM|!6TLuEA!v55_6`|(S|AO6@byGSm+GF*RT
i1`DeRNi11-xwmhc40q0sD{^G81e%{p4;X2J3$hN9tsvGlEFtCcQCNi(gzs#>KX?R#dNMlJX4hCxR>&fk&gg*5Tbifn8Gr&4&7Ps
R3u70XaUm1X#)=OwDB-)JWLzA>v=+?@Uu{W{I!qm>yI7lL;LdbQ|FR{fMgoE@idq@08c-PrKDMwPu$jTFy{(psyDHBTE+Q?30in`
A-OpMyI>6O9=*w5@O+2=VZT@TU&Wtfzu@!^b1Qj$`r+*Q^rUlQb=zM)eg0-0pIvsK{OR-cWikKA9J4z++;TXF>#@K~=J*CDmUiLS
-2*eVdbN7)-cAsrzbtg+w@Q;i?gayH2-z*-0O#}X|N1}tq(i*
"""
b = ''.join(DATA.split()).encode('ascii')
assert len(b) == 7949
assert hashlib.sha256(b).hexdigest() == '138256e17bb8e2e37db843ec1f52a526e6cac386482638a9db635535c033c301'
r = zlib.decompress(base64.b85decode(b))
assert len(r) == 16193
assert hashlib.sha256(r).hexdigest() == 'cfb7360357323745995109866742e6c5cbc84b7d34f03987a5bc8d37a5444418'
files = json.loads(r)
expected = {'cr62_global.py': [13225, '0b13528e0b40629b373d761d2f27ba64f5fea73f518aa5a44aed6f3c7c685cd8'], 'family_fast.py': [2613, 'cc8d964bbbf2772e2d50ac53a9026304700f0be04e8815a0e7e584e0d058c6c1']}
assert set(files) == set(expected)
for name, text in files.items():
    data = text.encode('utf-8')
    size, sha = expected[name]
    assert len(data) == size and hashlib.sha256(data).hexdigest() == sha
    Path(name).write_bytes(data)
print('CR62_TWO_SOURCE_RECOVERY_PASS')
```

The recovery script itself is 8946 bytes, SHA-256 `59dd86fd6648040204d9e85e69dd5fa573688a8f50a9f2b5b30b4fd1327c3ac2`, with LF and final LF as printed.

Reconstruct and verify:

```sh
python -S recover_cr62_global.py
mkdir audit
cd audit
python -S ../cr62_global.py
python ../family_fast.py
```

The following additional complete check was also executed in the output directory:

```python
from pathlib import Path
import json
from fractions import Fraction as F
r = json.loads(Path('cr62_global_audit.json').read_text())
assert len(r['directed_P']) == len(r['directed_Q']) == 30
assert all(F(row[2]) != 0 for k in ('directed_P','directed_Q') for row in r[k])
assert len(r['core_failures']) == 4 and {row[3] for row in r['core_failures']} == {3}
assert sum(k.startswith('reflection_') for k,v in r['guards']) == 72
assert all(F(v) > 0 for k,v in r['guards'] if k.startswith('reflection_'))
print('SIXTY_NONZERO_PRIMITIVES_FOUR_APEX3_FAILURES_72_REFLECTIONS_PASS')
```

Observed terminal markers include:

```text
CR62_TWO_SOURCE_RECOVERY_PASS
SIXTY_NONZERO_PRIMITIVES_FOUR_APEX3_FAILURES_72_REFLECTIONS_PASS
EXACT_MASK6216436_ACTUAL_CENTROID_FULL_NORMAL_CONE_PASS 2 4 4 [3, 7] [1, 2, 4, 8] [(1, 2), (1, 8), (2, 4), (4, 8)]
INTERNAL_CUTS_PASS 36 NEGATIVE_ROWS 4
FULL_TYPE_14_FREE_VARIABLES_ZERO_INCIDENCE_ZERO_MASS_EQUATIONS_PASS 5160 195
CR62_GLOBAL_RECOVERY_PASS
FDEG 21 21
UNBOUNDED_FAMILY_CORE_FAILURE_PASS 115 8666 99db86876e4070a3c68fec9bcde8510d96d6d7dddb43954645d147ded311de0b
```

The actual `INTERNAL_CUTS_PASS` line additionally prints the designated rational gap stated in Section 4. Expected output identities are:

```text
cr62_global_audit.json
67234 bytes
2611b1dbe2b7ffd9e857b1895a4b9d684672a9636b25285765f1145e20ab899e
cr62_full_type.smt2
230374 bytes
9361d765b1ed7bfd56ffaaf69023ce61dae3d3eb61016ff828d5f96c395b79ba
cr62_formula_manifest.json
551 bytes
98f91ed7e9b4bf191434d5c2cf1fbde7418882feccaa463ac4d317c8798eb560
family_certificate.json
8666 bytes
99db86876e4070a3c68fec9bcde8510d96d6d7dddb43954645d147ded311de0b
```

Recovery was executed in a fresh directory. Both recovered sources were byte-compared with the originals; all four regenerated outputs were byte-compared with the first exact execution. The manifest expressly says `NOT_SOLVED`. A generated formula must not be promoted into an UNSAT certificate.

Convenience copies supplement the inline capsule: complete source recovery (`recover_cr62_global.py`), actual-centroid and full-normal-cone audit (`cr62_global_audit.json`), and complete unsolved whole-type formula (`cr62_full_type.smt2`).

**Final scope:** a globally complete actual-mass parameterization and internal-cut boundary theorem, plus a rigorous unbounded obstruction to universal Santaló/core localization in the requested type. The previous certified patch is preserved. No entire type closure, no new numerical lower bound, and no homogeneous 110 attainer is claimed.
