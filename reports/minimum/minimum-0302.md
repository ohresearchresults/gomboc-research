# minimum-0302

AI research report · 2026-09-28 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# H5_THIRD_BAND_AND_EXPANSION_10_OVER3_U2_V1

## 1. Two new actual-domain theorems

Two substantial regions are now excluded from U1, with the original uniformly filled body supplying every centroid and with all physical affine metrics allowed.

| New theorem | Six basal cut depths | Origin corner | Taper |
|---|---|---|---|
| THIRD_BAND | Each of b,C,p,q,a,E independently in [1/4,1/3] | Entire admissible triangle u,v>0, u/b+v/a<1 | Every rho>0 |
| EXPANSION_10_OVER3 | Entire admissible six-depth domain; no small-cut restriction | Entire admissible triangle | Every rho>=10/3 |

Here C=1-c and E=1-d. THIRD_BAND excludes all 48,790 labelled true-edge weak rooted systems even for nonzero PSD matrices. EXPANSION_10_OVER3 is stronger combinatorially: it excludes a rooted spanning tree in the **complete** weak-arrow graph, again for every nonzero PSD matrix. Consequently every genuine body in either region has at least two strict unstable vertices under every SPD metric, including when incidental physical weak contacts occur elsewhere. All nonsingular affine images are included.

This is **not** the entire corner-third theorem. Depths below 1/4 mixed with depths above 1/4 remain outside THIRD_BAND unless another accepted region applies. It is not a central-half theorem, an all-shape polar S>=2 theorem, or a whole-incidence exclusion.

The extension relative to the supplied parent is explicit. QUARTER allowed six independent depths up to 1/4; WIDE allowed depths [1/10,3/10] but restricted u,v to [1/50,1/25]. THIRD_BAND permits all six depths to reach 1/3 and retains the entire origin-corner triangle, for every positive taper. Its intersection with QUARTER is only the six-depth boundary where all depths equal 1/4. EXPANSION_10_OVER3 replaces the former unrestricted-basal expansion threshold 7 by 10/3, newly covering the entire admissible basal chart for 10/3<=rho<7. The existing regions remain a union, not a newly asserted nesting. fileciteturn0file2L1016-L1034 fileciteturn0file2L950-L952

Four exact actual controls below attain U=2, with full same-inverse strict222weak000 censuses along unbounded metric rays. None is U1 or 110. The working global bracket remains 34<=C_min<=622; no canonical registry count is subtracted. fileciteturn0file2L9-L11

## 2. Input authority, complete reading, and a repaired literal-source discrepancy

The three native files were read through EOF, including all 2,028 journal lines and both literal parent payloads. All six decoded parent program units were also read. The native bytes matched:

```text
NINE_VERTEX_NONZERO_PSD_REFINEMENT_COLLAR_V1.md
9577 bytes
3052074db1f19530ac423145576607e4c86366b7e45a96cf9f17f880f0aee65b

HEPTAGON_TRIANGLE_UNIFORM_GAUGE_AND_ALL_WALL_GAP_V1.md
12200 bytes
a78ff4287c53f66c405271a3c0f63170a77c72763d2f81dd2a9b33ec724aa6f6

research-journal.md
368848 bytes
ebc4bb3f94e5d3ce61c1372a52e6176a7ca400afac6ab0bd20c65201e6dcd1ab
```

The parent authority labels are unchanged:

```text
minimum-0280
2e8a9d98288afbdc7ce98ed8ec9a1fc4ef8f95371f37c170f46471bf32381c8a

minimum-0284
2a38ebda52611fc6f5cb7914fb408a20fe7afba5c0b25d7cef0a61e7b3ce10d1
```

**Observed transport discrepancy.** Extracting the first parent's literal recovery fence, with its terminal newline, produced 24,318 bytes rather than the recorded 24,316. Its observed SHA was `92e701a936840760b6e044af882ece6d0d9f7d41cb28d22fbe3c83cc19fb6f36`; Base85 decoding failed. The fourth payload line had a duplicated two-character fragment. The exact single replacement is:

```text
T5sYbYhz}  ->  T5sYhz}
```

After that replacement, the entire wrapper is **exactly** the parent's recorded 24,316-byte object, SHA `fbc19ff24d8909f2bb6cb6fd8799150051a8105894aa6df11c7bf7f767a604ac`. The decoded 53,488-byte source map also matches its recorded SHA `35cfc6df1cb25cfbaef66cd4e9409d4c216300a3274c674da4d2908ab355e8a8`, and all six decoded source pins match. The recorded wrapper/source pins and the literal affected payload line are in the supplied parent. This was a hash-verified repair, not an invented substitute program. fileciteturn1file0L105-L131 fileciteturn1file0L149-L155

The new capsule below includes the complete, unchanged `h5_nine_exact.py` core directly, so continuing this result does not depend on repeating that repair or having an old sandbox. No settled QUARTER certificate was rechecked as the research target.

The later parent's generic equality hexagon is centrally symmetric only at delta=1/3, as already corrected in the supplied journal. Neither new theorem uses that adjective, the sharp-volume equality collar, or an unevaluated nine-vertex gap. fileciteturn0file2L1038-L1044

## 3. Literal moving body and physical conventions

Use the full strict chart

```text
b,C,p,q,a,E > 0,
b+C<1, a+E<1, p+q<1,
u,v>0, u/b+v/a<1, rho>0.

B0=(b,0),       B1=(1-C,0), B2=(1-p,p),
B3=(q,1-q),     B4=(0,1-E), B5=(0,a), B6=(u,v).

Y_i=(B_i,0), i=0,...,6;
Y7=(0,0,1), Y8=(rho,0,1), Y9=(0,rho,1).
```

The true outward maximal facet cycles and the true edge set are:

```text
FACES = (
 (6,5,4,3,2,1,0), (8,7,0,1), (7,6,0), (1,2,8),
 (9,8,2,3), (9,3,4), (4,5,7,9), (6,7,5), (7,8,9)
)
EDGES = 01,06,07,12,18,23,28,34,39,45,49,56,57,67,78,79,89.
```

These are the supplied full-chart labels, not integration diagonals or a lower-feature alias. The new computations keep these coordinates and their actual moments coupled. fileciteturn0file2L1136-L1174

At the actual volume centroid g, write X_i=Y_i-g and

```text
d_ij(M)=X_i^T M(X_j-X_i).
```

For SPD M, every vertex that is not strictly unstable has a genuine incident edge with d_ij>=0. Every such edge strictly increases the squared M-radius:

```text
X_j^T M X_j-X_i^T M X_i
 =2d_ij(M)+(X_j-X_i)^T M(X_j-X_i)>0.
```

Thus U1 supplies a true-edge rooted spanning tree. The corresponding identity is nondecreasing for PSD M. The certificates exclude a given weak rooted tree for all nonzero PSD M; the physical equilibrium-count conclusion is stated only for SPD M.

## 4. EXPANSION_10_OVER3: a new maximum-basal-source quotient mechanism

### 4.1 Actual area and volume moments

Use the genuine affine normalization diag(1/rho,1/rho,1), and set epsilon=1/rho. Its basal points are epsilon B_i; the three top vertices are

```text
T1=(0,0,1), T2=(1,0,1), T3=(0,1,1).
```

Define the actual basal moments

```text
A = 2 Area(B) = 1-bv-au-Cp-Eq,
Lx = 6 integral_B x
   = 1-bv(b+u)-au^2-Cp(3-C-p)-Eq^2,
Ly = 6 integral_B y
   = 1-bv^2-au(a+v)-Cp^2-Eq(3-E-q),
Mx=1-Cp,  My=1-Eq.
```

The same actual three-dimensional body has

```text
W = 6 Vol = 1+epsilon+A epsilon^2,
J24_x = 1+epsilon+Mx epsilon^2+Lx epsilon^3,
J24_y = 1+epsilon+My epsilon^2+Ly epsilon^3,
J24_z = 3+2epsilon+A epsilon^2,
g = J24/(4W).
```

The new verifier checks the three basal shoelace identities and the four three-dimensional identities against all sixteen oriented boundary triangles. No assigned vertex masses enter.

Because B is contained in Delta=conv(0,e1,e2),

```text
0<A<=1,
0<=Lx,Ly<=min(1,3A),
0<=Mx-A,My-A<=1-A.
```

The bound Lx<=1 follows by integrating x over Delta; Lx<=3A follows from x<=1 on B. The y bounds are identical. The M bounds follow from

```text
Mx-A=bv+au+Eq,  My-A=bv+au+Cp,  Mx,My<=1.
```

Consequently the actual centroid belongs to the rectangle

```text
1/4 <= gx,gy <= 1/4 + epsilon^2[1-A+epsilon min(1,3A)]/(4W),
gz = (3+2epsilon+A epsilon^2)/(4W).
```

This rectangle overcovers the **one actual centroid**. Its corners are not declared realizable bodies. After multiplication by W, its four centroid descriptions are affine in A separately on [0,1/3] and [1/3,1]. It therefore suffices to test A=0,1/3,1 and the four horizontal rectangle corners, provided the same centroid corner is used throughout an aggregated stress.

### 4.2 Quotient lemma covering every rooted alternative

Contract the seven basal labels to one group 0 and retain top groups 1,2,3.

If the actual root is basal, retain the actual parent of each top vertex, replacing a basal target by group 0. The top-only arrows cannot cycle, and this gives a group tree rooted at 0.

If the actual root is top, start at a basal vertex of maximum M-radius and follow its given rooted-tree path. Let x be the **last basal vertex on that path**. Norm monotonicity and maximality imply that x is also a basal radius maximum. After x, the path uses only top vertices. Select x's outgoing top arrow as the outgoing arrow of group 0. Every other nonroot top retains its actual parent, with basal targets replaced by group 0.

There is no top-only cycle because the original tree has none. There is no cycle through group 0 because the selected outgoing arrow of 0 is followed only by top vertices until the actual root. Thus this is a rooted tree on four groups. Moreover, for every incoming top-to-basal target y,

```text
(y-g)^T M(y-g) <= (x-g)^T M(x-g).
```

All selected group arrows are actual arrows from the original tree. Incoming basal targets remain independent points; they are not identified with x. The argument uses nondecreasing, not strictly increasing, PSD norms, so ties and projected coincidences are included.

There are sixteen unrooted K4 trees and four roots: **64 alternatives**, all generated by the source. This analytical reduction covers every original rooted tree, including trees in the complete ten-label arrow graph. It does not infer coverage merely from counting PD matrices.

### 4.3 Retaining source energy while adding valid norm comparisons

For one of these quotient trees define

```text
Q_ij = -[(x_i-g)(x_j-x_i)^T+(x_j-x_i)(x_i-g)^T],
tr(M Q_ij)=-2d_ij(M).
```

When group 0 is nonroot, x is its maximum-basal source. For each incoming basal target y use

```text
N_y=(y-g)(y-g)^T-(x-g)(x-g)^T,
tr(M N_y)<=0.
```

For a basal-root quotient there is no outgoing basal source and no norm augmentation; all three arrow tensors are already affine in their basal targets. In the nonroot case, choose independent nonnegative arrow weights w and norm weights mu with

```text
sum(mu)<=2 w_out,
```

where w_out is the weight of the outgoing arrow from x. Put c=(epsilon/3,epsilon/3,0), merely a tangent reference. Replace the outgoing source tensor and the norm tensors by

```text
Q_out_lin = Q_out-2(x-c)(x-c)^T,
N_y_lin = (c-g)(y-x)^T+(y-x)(c-g)^T.
```

The exact identity is

```text
sum(w Q)+sum(mu N)
 = sum(w Q_lin)+sum(mu N_lin)
   +(2 w_out-sum(mu))(x-c)(x-c)^T
   +sum(mu (y-c)(y-c)^T).
```

Every omitted term is PSD. The remaining matrix is separately affine in each selected basal point and in g. Therefore each basal point can be tested independently at 0,epsilon e1,epsilon e2; the same x is retained in its outgoing arrow and all its norm comparisons. The code checks the nine entries of this identity symbolically and checks the required multi-affinity.

This is not the centroid-balanced flow hierarchy: the original arrow weights remain independently selectable, the original source square is retained through an exact lower identity, and each additional norm inequality follows from the same original weak rooted tree.

### 4.4 Exact closed-continuum certificate

Multiply the lower matrix by 108W. At each of the twelve centroid/area descriptions, all entries become integer polynomials in epsilon of degree at most four. The complete source constructs 396 tensor types and **5,184 endpoint/centroid configurations** across the 64 quotient trees.

For the single closed interval

```text
0<=epsilon<=3/10,
```

the embedded 64 integer rows make every degree-four Bernstein coefficient strictly PD after subtracting

```text
(sum of the three arrow weights) * 2^-20 I.
```

All **25,920 shifted matrices and 77,760 leading minors** were checked exactly. The source independently reconstructs all five monomial basis polynomials from the Bernstein transform. Affinity after denominator clearing covers both closed A intervals; Bernstein nonnegativity covers the entire closed epsilon interval. No sampled-value feasibility claim is used.

For 0<=epsilon<=3/10, W<=139/100 and 216W<512. Restoring the PSD remainder and contracting with any nonzero PSD M gives, under the selected tree's valid maximality inequalities,

```text
sum(w d_ij)/sum(w) < -2^-29 tr(M).
```

A tree of weak arrows is impossible. This proves EXPANSION_10_OVER3 for the entire admissible basal chart, including the finite wall rho=10/3 and the unbounded expansion tail. The numerical margin refers to the displayed top-normalized affine coordinates; the exclusion itself is affine invariant.

### 4.5 Preserved simpler EXPANSION5 certificate

Earlier in this execution, a norm-comparison-free quotient proof was obtained for rho>=5. It uses any rooted quotient, the same independent basal endpoints, only the source-square tangent, and the larger centroid box

```text
1/4<=gx,gy<=1/4+epsilon^2/4,
3/4-epsilon(1+2epsilon)/(4(1+epsilon+epsilon^2))
 <=gz<=3/4-epsilon/(4(1+epsilon)).
```

With d=(1+epsilon)(1+epsilon+epsilon^2), clearing by 36d yields degree-six polynomials. Its 64 embedded integer rows check 3,456 configurations and 24,192 shifted PD Bernstein matrices on [0,1/5], with 72,576 positive minors and physical mean-arrow margin 2^-15. Its coverage is subsumed by EXPANSION_10_OVER3, but the simpler norm-free certificate and stronger quantitative margin on its smaller domain are preserved in full.

## 5. THIRD_BAND: full origin-corner freedom and all positive taper

### 5.1 Actual model and new geometry audit

Set lambda=rho/(1+rho), s=1-lambda and apply diag(s,s,1):

```text
Z_i=(s B_i,0), i=0,...,6,
Z7=(0,0,1), Z8=(lambda,0,1), Z9=(0,lambda,1).

u=b t h, v=a t(1-h), 0<t,h<1.
```

This parameterizes the entire admissible origin triangle, with inverse t=u/b+v/a, h=(u/b)/t and Jacobian abt>0. The six cut depths, h,t and lambda are nine independent shape parameters.

Use the actual identities

```text
A2=1-bv-au-Cp-Eq,
D=6 Vol=lambda+A2 s^2,
J24_x=s^3[1-bv(b+u)-au^2-Cp(3-C-p)-Eq^2]
      +s^2 lambda(1-Cp)+lambda^2,
J24_y=s^3[1-bv^2-au(a+v)-Cp^2-Eq(3-E-q)]
      +s^2 lambda(1-Eq)+lambda^2,
J24_z=A2 s^2+2lambda+lambda^2,
g=J24/(4D).
```

The new geometry audit verifies these against the sixteen true-boundary integration triangles. It also verifies all 56 nonincident support guards and all 19 nontriangular corner-turn guards, retaining all 64 simultaneous upper-depth strata, and checks the closed oriented facet-edge sphere.

That **geometry audit** is valid on the containing corner-third class (0,1/3]^6 with interior h,t. The **mechanical certificate** is only on [1/4,1/3]^6. These are not interchangeable scopes.

Throughout the band and its indexed compiler closure,

```text
A2>=2/3,  5/8<=D<=1.
```

The D bound follows from

```text
D=1-1/(4A2)+A2[lambda-1+1/(2A2)]^2.
```

Closed endpoints may merge labels or facets but retain positive volume. They are not described as genuine ten-vertex bodies.

### 5.2 Exact all-tree continuum proof

For every directed true edge set

```text
R_i=4D Z_i-J24,
Q_ij=-(R_i (Z_j-Z_i)^T+(Z_j-Z_i)R_i^T),
tr(M Q_ij)=-8D d_ij(M).
```

The unchanged, hash-pinned parent core is used on the **new** basal box. It enumerates the 4,879 connected nine-edge subsets of the true seventeen-edge graph and roots each at all ten vertices; the Laplacian cofactor gives the same unrooted count.

The actual polynomial compiler has 684 basal monomials and degree four in lambda. Its inverse-Bernstein reconstruction checks 697,680 scalar entries. The native direct domain is

```text
(b,C,p,q,a,E,h,t)
 in [1/4,1/3]^6 x [0,1/2] x [0,1],
lambda in [0,1].
```

Each row has independent positive integer multipliers on true original arrows. The source aggregates the row before bounding the complete multivariate Taylor remainder. For each of the five lambda coefficients it uses an invertible integer congruence H. At all 256 affine sign corners, it checks the full lower matrix obtained by subtracting the entrywise higher-order remainder row sums and

```text
(sum weights) * 2^-45 H H^T.
```

Three exact integer Sylvester minors certify each lower matrix. The resulting common-coordinate inequality is

```text
sum(w Q_ij) > (sum w) 2^-45 I,
```

so the weighted mean original arrow is less than -2^-48 tr(M), since D<=1. Congruence frames prove matrix positivity; they are not independent physical metrics. The moving actual J24 remains present in every tensor.

Every residual rooted tree is sent to **both closed children** at subdivision. A leaf is accepted only after all its inherited trees contain a certified forbidden support. Missing children, orphan nodes, wrong residual counts, singular frames and failed minors are rejected. Coverage is this complete recursion, not the leaf-volume sum or the number of PD tests.

The physical reflection

```text
(b,C,p,q,a,E,u,v) -> (a,E,q,p,b,C,v,u),
vertex permutation (5,4,3,2,1,0,6,7,9,8),
h -> 1-h
```

preserves the new six equal depth intervals. The source checks the actual moment transformation and the bijection of all 48,790 rooted systems. Thus the direct h<=1/2 domain plus its reflection covers the whole origin corner, including the shared wall.

### 5.3 Observed complete counts

```text
Closed binary nodes:                     349
Direct closed leaves:                    175
Maximum subdivision depth:                13
Independent integer rows:               4999
Positive arrow-weight terms:           27836
Maximum integer weight:                10000
Row/cell applications:                 18721
Shifted PD lower matrices:          23962880
Positive leading minors:            71888640
Numerical locator calls:                9216
Missing rooted alternatives:               0
Exact relative parameter-volume sum:       1
Initial polynomial denominator:    254803968
```

These are local proof counts, not canonical classes or a count of disjoint reflected incidence domains.

The complete numerical discovery and exact check passed. The final frozen driver was then run from an empty output directory: it rediscovered the entire certificate byte-for-byte and completed every exact check, reproducing the report byte-for-byte. A further complete check from the recovered source-only capsule also passed and reproduced the report. The earlier parent QUARTER/WIDE author-execution distinctions are not altered.

## 6. Four durable actual nonwinners and their literal inverse

All four records use the compact lambda gauge of section 5 and the same true facets and edges. Inputs are ordered

```text
(b,C,p,q,a,E,u,v,lambda).
```

Let

```text
r0=(1,3,-2), r1=(3,-1,0), r2=(-1,-3,-5),
M_L=L^2 r0 r0^T + L r1 r1^T + r2 r2^T,
M_L^-1=r0 r0^T/(196 L^2)+r1 r1^T/(100 L)+r2 r2^T/1225.
```

The inverse identity is checked exactly. The vectors are orthogonal, and on all stated rays the displayed-frame condition number is 2L^2/5, hence unbounded.

```text
THIRD_FULL_ORIGIN
input=(1/3,1/3,1/3,1/3,1/3,1/3,1/9,1/9,1/3)
L>=128
Vol=157/1458
g=(2921/16956,2921/16956,265/628)
S={2,4}, U={3,7}, H={18,49}

THIRD_ASYMMETRIC
input=(3/10,1/3,2/7,5/16,4/13,1/4,6/125,64/325,1/7)
L>=64
Vol=1241257/10701600
g=(50125422397/243286372000,
   135844489343/632544567200,
   1532457/4965028)
S={2,4}, U={3,7}, H={18,49}

EXPANSION5_LARGER_CUT
input=(2/5,1/5,1/3,1/4,1/5,3/10,1/10,1/20,5/6)
L>=256
Vol=18491/129600
g=(5596973/26627040,5594869/26627040,4681/6724)
S={1,8}, U={7,9}, H={28,79}

EXPANSION_10_OVER3_BOUNDARY
input=(2/5,1/5,1/3,1/4,1/5,3/10,1/10,1/20,10/13)
L>=256
Vol=27473/202800
g=(5622919/28571920,5618107/28571920,73473/109892)
S={1,8}, U={3,7}, H={28,79}
```

S labels are facet indices in the displayed FACES list; U labels are vertex indices; H entries are true edges. Each entire ray has strict(S,U,H)=(2,2,2), physicalweak000, and no zero primitive.

The generator independently recovers each hull from all vertex triples, recovers the true edges from maximal-facet intersections, checks every support, and verifies actual zeroth, first and second moments by both the sixteen signed boundary triangles and a nine-positive-tetrahedron fan at vertex 7. The within-tetrahedron second-moment terms are retained. Every primal and same-inverse polar primitive is a quadratic polynomial after multiplication of the polar rows by the common positive L^2. Substitution L=L_min+z gives a strictly signed constant and remaining coefficients of that same sign or zero. This certifies all **272 primitive records on the entire rays**, rather than a census at sampled L values. All vertices, poles, actual covariances, nine fan weights and all primitive coefficients regenerate from the included 4,556-byte unit.

## 7. Uncompleted experiments and the remaining target

Two broader locators were stopped with incomplete trees and were **not accepted as exclusions**. One used [1/4,1/2]^6, full t, h<=1/2, all lambda; the other restricted lambda to [1/2,1]. The first retained 164 completed locator nodes, 2,708 proposed rows and 5,649 LP calls; the second retained 299 nodes, 2,048 proposed rows and 4,769 LP calls. Both have nonempty frontiers and `complete=false`. Their proposal rows did not receive an all-root exact acceptance. The two complete locator units are preserved in the source capsule; the corresponding bounded recovery commands use budgets 164 and 299 and terminate as non-proofs. A second cold replay of those stopped numerical prefixes is not claimed. Their saved checkpoints are only supplemental unverified search material, not successors to the accepted THIRD_BAND certificate. The observed incomplete files have these pins:

```text
central_half: 2687417 bytes
51946cc389890bab3a25fc7ed1788ffe80a96aeaa8de571ab02f7b5c8acef377
half_upper: 2512471 bytes
0c83546f2b3cb8f2da669ab4e70a76d47912c0366f6d3fa2c1bf7d16c4453e26
```

No full corner-third or central-half survivor was found. Failure to find weights or stopping a locator does not establish geometric feasibility, impossibility, or optimality of the threshold 10/3.

The useful remaining parallel target is now rho<10/3 outside the union of the accepted domains. For corner-third, the missing mixed-depth portions have some depth below 1/4 and some above 1/4; merely widening the already closed band does not cover these portions. In the broader central-half domain, both those mixtures and depths above 1/3 remain. General nonparallel moduli are separate.

The new reusable mechanism is the maximum-basal-source quotient together with area-conditioned actual-centroid bounds and independent original-arrow weights. A continuation can sharpen the joint horizontal centroid region or combine that norm augmentation with the genuine multivariate compiler. Such sharpening must retain the one actual body and certify every inherited tree; it must not replace them with independently assigned basal masses or the already blind centroid-balanced hierarchy.

## 8. Reconstruction, exact inputs, and observed pins

The source-only capsule in section 9 contains seven complete readable programs. The proof dependencies are `h5_nine_exact.py`, `third_band_certificate.py`, `expansion5_certificate.py`, `maxbase_expansion_certificate.py`, and `new_controls.py`. The two remaining units are the explicitly uncompleted central-half locators. There are no hidden certificate seeds or saved coefficient arrays. The expansion verifiers carry all 64 weight rows literally; the large band certificate is regenerated from an empty state by the included deterministic locator.

Observed environment: CPython 3.13.5, SymPy 1.14.0, NumPy 2.3.5, SciPy 1.17.0 for discovery, OpenBLAS 0.3.30 on Linux x86_64. Each driver sets OPENBLAS_NUM_THREADS=1 before importing NumPy. Keep assertions enabled. The code records all nondefault tolerances, rounding levels, integer frame rules and subdivision rules. Numerical linear programming only proposes rows; exact polynomial/rational/integer arithmetic accepts them.

Save section 9 as `recover_h5_third_expansion.py`, then:

```sh
python -B -S recover_h5_third_expansion.py fresh_h5
cd fresh_h5

# Exact reconstruction/check from the embedded expansion rows:
OPENBLAS_NUM_THREADS=1 python -B maxbase_expansion_certificate.py check expansion10over3.json
OPENBLAS_NUM_THREADS=1 python -B expansion5_certificate.py check expansion5.json
OPENBLAS_NUM_THREADS=1 python -B new_controls.py controls.json

# Empty-state complete THIRD_BAND rediscovery followed by exact acceptance:
OPENBLAS_NUM_THREADS=1 python -B third_band_certificate.py build third_band 2000

# Independent recheck of that reconstructed certificate:
OPENBLAS_NUM_THREADS=1 python -B third_band_certificate.py check third_band

# Optional independent numerical rediscovery of the small expansion certificate:
OPENBLAS_NUM_THREADS=1 python -B maxbase_expansion_certificate.py build expansion10over3_rediscovered.json
```

Use new output directories. The observed expansion rediscovery reproduced the embedded row bytes, but exact checking, not cross-platform floating bit identity, is the acceptance criterion. The complete band cold rediscovery in the stated environment reproduced both pins below. All final expansion and control checks were also executed from the recovered source-only capsule.

Expected terminal markers:


[Encoded source block omitted; the code in this passage is incomplete.]


Exact final source pins:

```text
h5_nine_exact.py                30665
ca132f45c0d1a6323a0eafa4bf82bd9f196065571a42f9449215351b3a50dcc2
third_band_certificate.py        5419
84744e32dce419dfc5a84c5581dd51129136c5ea84cbe932c1d407284a7e7483
expansion5_certificate.py        8479
fd1b7e0e6682f2213d4baf955b44ec347b81a6cb05da1fa7c86c2bcfa0c16bc7
maxbase_expansion_certificate.py 9886
dc449203e50a93d5ef8d2e36d2444e18459016febd12147d638960b975ed7873
new_controls.py                  4556
b3ce1aef8e8c7a0852be4109eaefe08430d142eed659bd0efcc5c2a2a47ebe6d
central_half.py                  1050
2c29736788de62f4fe84a4c6287f8b005d44b93c7dc9639d0dd0f25d60a35f6b
half_upper.py                    1139
bda59b64cdd6e6ff44286332d3c6da6b6cb1a4be1cfebf98da942b58a42ae640
```

Exact accepted output pins, independent of the chosen output directory:

```text
third_band/certificate.json  4070068
aa618e0ca3c54f2a62a647a33e7ac374e7f400ccf9375a590d67addffa24fe7d
third_band/report.json          6371
26912c545f42230ed3be64014643c363a17313f32d720f9e390743e13995c2de

expansion10over3.json            894
66397bdcb4deec1c073e09d32175f64e70b12a00ea67d6517744ebf0b0898a32
expansion10over3.json.report.json 1082
7e978cd957aafbbd48bb1f96bf35115845a5813058e1571b0fa13e678bd21cf8

expansion5.json                 823
d240ea3b0fe47174bad06c6337deb8a147964bc72f0886c410990cd9b5556410
expansion5.json.report.json      769
6cabb14e2fb1388b12e0c0f13882a6825f7090b0a54d8ffefe4549a16c4f3831

controls.json                 39510
22b60e0030023de4f1981e846404fb34ed0eb95e3642aa9c9b6a790391970eb8
```

The decoded seven-source map is 62,702 bytes, SHA `953f660806ff45b3925595b4ef960e78a2a0d232d78765eabb6c9e6c62a474de`. The recovery wrapper is 27,964 bytes, SHA `4ecf7a1bf2de307187f74d2b46e06746a48c6fe5d1d2276292253a5175d1c18d`.

These are observed author computations and exact mathematical certificates, not a proof-assistant formalization or a claimed independent coordinator replay. The two new actual-domain exclusions, the simpler nonwinning expansion proof and all four actual controls are reconstructible successors. The uncompleted central-half experiments remain explicitly outside that acceptance.

## 9. Complete autonomous recovery capsule

The following is the entire recovery source, not an abbreviated payload. A convenience archive contains the same readable sources, accepted certificates, reports, logs and unverified-search checkpoints, but reconstruction does not require that archive: [source, certificates and evidence bundle](sandbox:/mnt/data/H5_THIRD_BAND_AND_EXPANSION_10_OVER3_U2_V1.zip).


[Encoded source block omitted; the code in this passage is incomplete.]
