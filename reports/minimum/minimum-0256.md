# minimum-0256

AI research report · 2026-09-26 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# H5_OPTIMAL_FLOOR_ALLROOT_CENTRAL_REGION_V1

## 1. New actual-shape theorem

Let

```text
B_central = { (x,r,p,q): 1/5 <= x,r,p,q <= 1/2, p+q<1 }.
```

**No genuine homogeneous member of the literal H5 family with basal parameters in B_central and any 0<lambda<1 admits exactly one strict stable and exactly one strict unstable equilibrium under a common physical SPD metric. Additional weak contacts are allowed.** This is a new four-dimensional basal region, not a tube about a fixed shape or another fixed-G control.

The newly computed all-root assertion is more specific and stronger on its metric domain. Put

```text
p0 = 7024915/1000000,
q0 = 6832329/1000000,
D0 = p0*q0+q0+1 = 11165771895407/200000000000,
ell = 1/D0 = 200000000000/11165771895407,
alpha = 1/(D0-3) = 200000000000/10565771895407.
```

For every basal point in B_central, every `1/40<=lambda<=3/5`, and every SPD M satisfying

```text
H = Sigma^(1/2) M Sigma^(1/2) / tr(Sigma M) >= ell I,
```

there are at least **two strict unstable vertices**. Sigma is the same body's actual uniform-volume covariance. All 48,790 rooted true-edge trees are rejected throughout the entire closed shape box, including weak selected arrows.

This includes every metric with the two closed descending adjacent eigenvalue ratios `h1/h2<=p0` and `h2/h3<=q0`. It also includes the complete one-sided spectral window in the supplied floor theorem. It does **not** assert the entire condition-number-48 cone: that cone has metrics below this eigenvalue floor. The previous box's cap73 conclusion remains an independent accepted result on its previous shape region. The strict finite-height bounds apply to joint S1/U1 candidates, not arbitrary U1 metrics.

The all-taper joint conclusion combines the new middle-taper theorem with two accepted premises: the paired-reflection WIDE theorem covers this basal box for `0<lambda<=1/40`, and the all-basal unrestricted-U2 theorem covers `lambda>=3/5`. The first premise is a joint S/U exclusion, not an unrestricted U2 theorem. Thus the all-taper conclusion stated above is **S>=2 or U>=2**, while the new conditional-U2 assertion has the stated middle-taper scope.

The new basal cube is disjoint in this parameter chart from the prior Nlj box and its reflection: those require either p or q at least 3/4. Its four interval widths are 3/10, versus 1/10 for that prior box. It also avoids the named x/r>=15/16 macros and the tiny off-macro tube. It can intersect older lower-dimensional slices and the paired-reflection low-taper regions; no disjoint canonical-catalogue subtraction is inferred. Whole H5 and E17 remain open, and the accepted global bound remains **34<=C_min<=622**.

There is a qualitative separation from the paired-containment mechanism. For every H5 basal shape and `lambda>=1/4`, its exact moments give

```text
D-3Kz = A*(1-lambda)^2/2-lambda/2-3*lambda^2/4,
A=(31-24*x*p-24*r*q)/64 <=31/64,
D-3Kz <=279/2048-352/2048 = -73/2048 <0.
```

Hence `g_z>1/3` throughout this entire upper part of the new interval. The paired-end containment from the companion parent cannot hold there; that parent explicitly identifies the `g_z>=1/3` boundary of its particular mechanism. The new proof does not require a basal U or prescribe a root layer.

## 2. Actual geometry and the certificate inequality

### One homogeneous body throughout

For `s=1-lambda`, use precisely

```text
Z0=(s/4,0,0),              Z1=(s*(1-3*x/4),0,0),
Z2=(s*(1-p),s*p,0),        Z3=(s*q,s*(1-q),0),
Z4=(0,s*(1-3*r/4),0),      Z5=(0,s/4,0),
Z6=(s/16,s/16,0),          Z7=(0,0,1),
Z8=(lambda,0,1),           Z9=(0,lambda,1).
```

The oriented maximal facet cycles are

```text
(6,5,4,3,2,1,0), (8,7,0,1), (7,6,0), (1,2,8),
(9,8,2,3), (9,3,4), (4,5,7,9), (6,7,5), (7,8,9).
```

Only consecutive vertices in these cycles give the seventeen mechanical edges. Boundary triangulation diagonals are used solely for integration. For each boundary triangle `(a,b,c)`, let `d=a dot (b cross c)` and `u=a+b+c`. The exact moments are

```text
D = sum d,
K = sum d*u/4,
J = sum d*(u*u^T+a*a^T+b*b^T+c*c^T)/20,
Vol = D/6,  g=K/D,  Sigma=J/D-g*g^T.
```

The new verifier independently computes a positive nine-tetrahedron apex-7 fan and proves equality of all ten raw moment polynomials with the boundary formula, identically in all five parameters. This retains the within-tetrahedron covariance, not just tetrahedral centroids or vertex averages.

### The optimal floor map is applied to original arrows

For every directed true edge e=(i,j), define

```text
A_e = sym((Z_i-g)(Z_j-Z_i)^T),
D_e(M) = (Z_i-g)^T M (Z_j-Z_i) = tr(M A_e),
Q = -sum_e w_e A_e,    w_e>=0,
t = tr(Sigma^-1 Q),
P = Q+alpha*t*Sigma.
```

This map is linear in the weights. All quantities are recomputed from the moving actual body. Put `P0=Sigma^-1/2 P Sigma^-1/2`. The supplied exact identity, with `tr(Sigma M)=1`, is

```text
tr(MQ) = tr((H-ell I)P0).
```

If P is PD and H>=ell I, the right side is positive because `tr(H-ell I)=1-3ell>0`. In contrast, selected weak original arrows imply `tr(MQ)=-sum w_e D_e(M)<=0`. Hence such a positive weighted P rejects the entire selected packet. This is the given optimal trace-floor identity, not a new claim of scalar-map optimality.

More quantitatively, in any common congruence coordinates, if

```text
P/(sum w) >= delta I,   Sigma <= R I,
```

then the normalized negative-arrow mean is at least

```text
-sum w_e D_e(M)/(sum w) >= delta*(D0-3)/(R*D0).
```

No fixed tangential G, fixed shear, eta contraction, independent polar metric, or frozen centroid is used. A cell's rational covariance preconditioner changes only the computational coordinates. The physical metric continues to range over the full stated cone.

## 3. Exact whole-region verification

### Polynomial moment initialization

To retain cancellations before interval bounding, the implementation first constructs all raw moment polynomials exactly: ten polynomials, 222 nonzero power terms in total, maximum total degree 8. On each cell, it shifts their variables to `theta=mid+rad*xi`, with `xi in [-1,1]^5`, before taking any interval remainder.

Let C be the nonsingular rational midpoint-covariance preconditioner and let g_mid be the actual midpoint centroid. The transformed numerator coefficients are computed exactly as

```text
K' = C*(K-D*g_mid),
J' = C*(J-g_mid*K^T-K*g_mid^T+D*g_mid*g_mid^T)*C^T.
```

Here D remains the **original** six-volume. The common affine Jacobian cancels from the moment ratios, so `K'/D` and `J'/D-(K'/D)(K'/D)^T` are the actual centroid and covariance in the transformed coordinates. This preserves coefficient cancellations before interval bounding; it is not a covariance surrogate.

The midpoint preconditioner uses exact LDL and 24-bit dyadic inverse-square-root approximations. Its invertibility, not approximation accuracy, is the needed mathematical premise. The arithmetic then uses 80-bit outward dyadic intervals and affine Taylor models, with rigorous remainders. Higher monomials with an odd exponent are enclosed by `[-1,1]`; all-even monomials are enclosed by `[0,1]`. Reciprocals use the exact remainder identity

```text
1/(c+z) = 1/c-z/c^2+z^2/(c^2*(c+z)).
```

Every actual volume and covariance-determinant denominator is bounded strictly away from zero before inversion. Each symmetric arrow-map field has an affine lower matrix model after subtracting a rigorous entry-error row-sum bound times I. All 32 corners of that **affine lower model** are checked with integer arithmetic. They are not 32 samples of the nonlinear body.

For each accepted packet, the 32 weighted integer corner matrices are PD by all three leading principal minors. Convex interpolation proves positivity of the lower affine model throughout its box, and hence positivity of the exact moving P. The uniform eigenvalue lower bound is obtained from

```text
lambda_min(R_int) >= 4*det(R_int)/(tr(R_int))^2,
```

with the exact dyadic scale and weight sum restored. The reported R is an outward interval upper bound for the covariance operator norm. The quantitative arrow guard therefore follows from the displayed trace identity without floating acceptance.

### Complete shape and true-tree coverage

The initial p/q square is split at 7/20. Three rectangles are computed directly: low/low, low/high and high/high. The omitted high/low rectangle is obtained by the exact whole-body reflection

```text
(x,r,p,q,lambda) -> (r,x,q,p,lambda),
spatial coordinates (X,Y,Z) -> (Y,X,Z),
vertex permutation pi=(5,4,3,2,1,0,6,7,9,8).
```

This does not reflect a packet while leaving its geometry behind. The executable proves all ten raw moment reflection identities and all ten vector-valued vertex identities. Thus it transports the actual centroid and covariance with the whole body. It also checks the bijection on every one of the 48,790 rooted trees. A reflected packet retains exactly the same normalized physical derivatives and quantitative guard under the pulled-back metric. Reflected positivity is a proved transport, not a second numerical run or an extra direct PD-matrix check.

The other subdivisions are dyadic in all five shape coordinates, not merely taper subdivisions. An optimizer-free verifier reconstructs the complete closed partition independently from the terminal boxes, including the reflected boxes. It checks every leaf against its exact recursively reconstructed box and checks the exact total five-dimensional volume. There is no uncovered shape cell or pruned feasibility assumption in the claimed region.

All rooted trees are enumerated from the seventeen true edges. The independent Kirchhoff cofactor is 4879; orienting every spanning tree to each of ten roots gives 48790. Each direct cell's exact packet supports cover all these trees, checked using literal arrow incidence. The reflection bijection proves the same coverage on every transported cell.

If there were exactly one strict U, every nonroot would have an original true-edge exit with D>=0. The identity

```text
|Z_j-g|_M^2-|Z_i-g|_M^2 = 2D_(i,j)+|Z_j-Z_i|_M^2 >0
```

makes these exits acyclic; selecting one per nonroot gives a rooted tree. The atlas rejects it. This argument includes zero nonroot derivatives. A metric-norm-maximal true vertex is always strict U, so the conclusion is U>=2.

True facet fidelity is additionally certified on the entire requested box: 90 support/convex-turn guards and nine positive fan determinants have 956 positive Bernstein coefficients after removing only powers of `1-p-q`. Every expansion is reconstructed back into its full power coefficients. The factored term is strictly positive on every genuine body. The face `p=q=1/2` is an indexed collapsed limit, not a ten-vertex mechanical claim.

## 4. Executed exact atlas and quantitative conclusion

The reconstructed atlas and optimizer-free verifier both completed. The final verifier was executed from sources decoded by the inline recovery unit below. Its status is **EXACT_PASS**, with terminal marker `H5_OPTIMAL_FLOOR_ALLROOT_CENTRAL_REGION_EXACT_PASS`.

```text
Directly certified closed five-dimensional cells   3215
Additional reflected closed cells                 1047
Full closed shape partition                       4262
Direct distinct positive-integer certificates      4181
Additional distinct reflected certificates         3101
Full distinct certificates                         7282
Direct certificate/cell uses                       1130608
Reflected certificate/cell uses                    369638
Full certificate/cell uses                         1500246
Direct PD Taylor-corner matrices                   36179456
Direct positive leading principal minors          108538368
Rooted trees covered per cell                      48790
Full raw rooted-tree/cell combinations              207942980
Maximum integer weight                            4471
Maximum weight sum                                10000
```

The directly stored support-size histogram is

```text
3:445, 4:1258, 5:1546, 6:840, 7:91, 8:1.
```

The complete independently reconstructed full-partition split counts, in coordinate order `(x,r,p,q,lambda)`, are `(92,45,48,192,3884)`. The generator processed 6427 nodes and 10434 LP calls; 120 enclosure failures and 3092 locator failures produced subdivisions, not feasibility claims. The final generator starts from an empty library and compacts it to 4181 used certificates. Reflected positivity follows by the exact body-and-metric transport; those matrices are **not** counted as additional direct PD checks. The full 207942980 figure is literal tree/cell support coverage, not that many numerical optimizations or new canonical classes.

For every tree throughout the whole new middle-taper box, an original arrow has

```text
D_e(M) <= -2^(-28)      when tr(Sigma M)=1 and H>=ell I.
```

More precisely, a contained packet has a normalized negative-arrow mean at least the exact rational

```text
1538395524956348896976513702052030925578867481824571545014952141888354134458575368275
/380555339018407663012701415047012098971005888936113123860539412638342307469641133733113840979
```

which exceeds `2^(-28)=1/268435456`. The value is obtained by taking the exact minimum of all certified cellwise eigenvalue/trace bounds, not by rounding a floating optimum. The reflected cells inherit the identical lower bound.

## 5. Retained physical control and method boundaries

The new exact nonattaining control is inside the new region:

```text
theta=(2/5,3/10,2/5,1/3,2/5),
Vol=13571/120000,
g=(3491507/21713600,3664091/21713600,24771/54284),
M=Sigma^(-1)/3,  N=3Sigma.
```

Sigma is reconstructed from the same full-body moments, and the source checks `MN=I` and `Sigma M=I/3` exactly. Thus its normalized covariance-weighted spectrum is `(1/3,1/3,1/3)`, strictly inside the necessary spectral bounds. Its complete same-inverse audit is

```text
strict (S,U,H)=(6,8,12),
S=(0,1,3,4,6,8),
U=(1,2,3,4,6,7,8,9),
H=((0,1),(1,2),(1,8),(2,3),(2,8),(3,4),
   (4,5),(4,9),(6,7),(7,8),(7,9),(8,9)),
physical weak points=0,
zero primitives=0 of 68.
```

All rational vertices, covariance entries, poles, M/N entries and 68 true-edge primitives regenerate in `h5_floor_control.json`. This is a calibration body, not a U1 candidate, proper110 construction, or separately optimized polar system. The source does not claim an eta-pencil census for this non-U1 control.

The stronger scalar map and cancellation-preserving actual moment initialization enabled the regional computation. No use of the full upper-and-lower spectral-window dual was needed for this region. This does not prove that a different library using an older scalar map could not cover the same region. A conservative interval or LP failure triggered subdivision only; it supplied neither a feasibility conclusion nor a reason to drop a tree. This work supplies an exclusion, not a positive full-tree construction. Uniform certificates can use more than five rows; this does not contradict the accepted pointwise five-arrow theorem.

The companion parent's distinct capped (4,2,4) control remains an important boundary. Its parameters are `(1/10,9/10,3/25,3/5,2/5)` and its metric is `((149,-455,64),(-455,4030,-340),(64,-340,104))`; it has only the two top unstable vertices 8 and 9, while its covariance-weighted eigenvalues lie in `(9/10,1)`, `(5,6)`, `(33,34)`. Thus an unavoidable basal U is false across the general residual strict-ratio cone. The present atlas does not assume it or choose the root's layer in advance. That supplied control was read as evidence, not recomputed or renamed as the new (6,8,12) control.

## 6. Input authority and complete reading

I read the supplied complete journal through EOF, including the branch memory and both literal parents, and all four newly supplied standalone sources. An initially truncated final line in the journal's first displayed chunk was explicitly fetched in full. No remaining input range is omitted. All five mounted manifests matched:

```text
OPTIMAL_COVARIANCE_TRACE_FLOOR_MAP_AND_CAP73_V1.md
11920 bytes  f4a14462a34718f63cdd82246ec99333fee682fa52ae6296729c8bd1bed262f0
spectral_floor.py.txt
7694 bytes  bdb5fe86802c7d4da89389630a04b17917aca21f890f7b65e7825e9a72388b51
spectral_floor_locator.py.txt
1580 bytes  102a63fc514e4cbb84388299d6196eacebfd1e1509f6d3907c3de6829bf2ca97
FINITE_HEIGHT_RECIPROCAL_DOMAIN_V1(1).md
10171 bytes  e7daf31f7dddffac638b3bb0d7005af5613e4b2473b0979daff4357ebf5894db
research-journal(20260926-212447).md
375280 bytes  6b7e5dc00c94007f6fb694710da764e92f75fa0ad0f1d8f8dc530de28412e9ff
```

The two literal parent envelopes also matched:

```text
minimum-0254
44777 bytes  54910bbef02f3039f114fe487568a3710a65cbf08331a42511807f836c39c2d0
minimum-0253
37319 bytes  0bf1ea8d44110e8f0f712137c4fc3bff5ff4f48962e0e3a5b4c3c79b6b14db45
```

For each parent, take its titled Markdown payload, strip trailing whitespace, append one LF, and serialize `{'version':2,'result_markdown':text}` with `json.dumps({'version':2,'result_markdown':text},ensure_ascii=False,separators=(',',':'))`. This reproduces the stated envelope pins. No semantic/source conflict or missing computational dependency was found. Historical exclusions and the finite-height theorem are supplied accepted mathematical premises, not newly replayed atlases.

The new integer atlas was regenerated in a fresh source-only directory and matched byte-for-byte. Independently of the numerical proposal run, the optimizer-free verifier was executed from the sources decoded by the inline recovery unit; it recomputed every accepted lower matrix, all exact positivity guards, the full reflected partition and every rooted-tree cover. The fresh generator did not need a saved parent library. This is an author-executed exact certificate and source-only reconstruction, not a claim of proof-assistant formalization or independent coordinator replay.

## 7. Complete source-only recovery

Save the complete recovery unit below as `recover_h5_floor.py`, including its final LF. It decodes the complete four source units and checks the decoded map and every source pin before writing the files. The recovered sources include the actual geometry, polynomial-moment constructor, outward Taylor arithmetic, numerical integer-weight generator, exhaustive partition/tree verifier, reflection proof checks, and physical control audit. No parent source, saved certificate, historical library, journal, or old sandbox is a computational input.

```sh
python -B -S recover_h5_floor.py fresh
cd fresh
OPENBLAS_NUM_THREADS=1 python -B h5_floor_search.py build
python -B -S h5_floor_verify.py
```

For checkpointed generation, `python -B h5_floor_search.py step 20` processes at most 20 subdivision nodes; repeat it until `COMPLETE_UNVERIFIED`. The exact verifier, not that status label, establishes the theorem. Fresh reconstruction begins with an empty weight library. The generator has no random seed.

Observed stack: **CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0**, one OpenBLAS thread. The recovery and verifier use only the standard library. The generator and verifier share the exact compiler; independent acceptance means optimizer-free recomputation and separate exhaustive checks, not a second independently implemented interval-arithmetic package. Assertions must remain enabled. Different floating solver stacks can propose different weights or partitions; that does not license accepting an unchecked output. All reported pins below refer to the stated stack and exact sources.

Important nondefault parameters are literal in the recovered source: 80-bit outward dyadic arithmetic, 24-bit rational midpoint preconditioner, the exact five-dimensional domain above, the three initial p/q rectangles and whole-body reflection, adaptive midpoint splitting by largest width with taper weight 2, maximum subdivision depth 32, 70 LP cutting iterations, 2000 proposal calls per cell, the positive-margin thresholds, and the complete integer-rounding denominator list. Numerical comparisons only locate or screen proposals; exact integer/rational checks accept them.

The actual recovery markers are

```text
H5_OPTIMAL_FLOOR_SOURCE_RECOVERY_PASS
CHECKPOINT COMPLETE_UNVERIFIED 3215 4181 5600262
H5_OPTIMAL_FLOOR_ALLROOT_CENTRAL_REGION_EXACT_PASS
```

The checkpoint line additionally prints its hash and elapsed time; elapsed times are not pinned. The generated report stores the exact uniform rational guard, all cellwise bounds, the full partition and certificate statistics, the geometry/control pins, and a digest of the completely recomputed integer Taylor-table stream. The atlas itself contains every integer weight packet, cell, and support assignment.

### Recovery and output pins

```text
recover_h5_floor.py 15557 bytes
9a19097b1abdc4e514a8db09cd2c2acaed03c75bb47bcc419853bacc7eaf158e
Decoded lossless source map 31017 bytes
16ac5721cd689627f961d9bc3dcd6b241f3baca916081cd710726af08ec33b17
h5_floor_core.py 8083 bytes
5cc97f945b963a87d651d41e529c3206a65664b702922564b1862de509a0be6d
h5_floor_search.py 5811 bytes
db22437a69b2eb6cf91f54cc5ff7b8be65897f0119bc419a7a73b1a201e566d6
h5_floor_verify.py 12932 bytes
984725c11b29465e5256229d387ca87a3db3dbf076cf70de8983acef8ac0aa84
poly_moments.py 3098 bytes
70256230321e1cc00fa1d4bcf43db89bcd52c1755dce44a84938471eb467f3a2

h5_floor_atlas.json 5600262 bytes
aba157dc06fde52307bf82866600fa6b969282b820dfe79087d3f4a3dbb78927
h5_floor_report.json 4739343 bytes
340d6ab822d03a1f5cd768b7bf16283c62d7c71f5dd80b9e2f0578d614f07405
h5_floor_geometry.json 40526 bytes
4e62c0a3e9147465a0b7ea2640b9e0f8630c697452080e4e93c0021b717fa6ff
h5_floor_control.json 10528 bytes
99e4d5fed5e2a5c8ece88357372d589b63aba22b77d300012ffe85ef103af7b7

Recomputed integer Taylor-table stream SHA-256
c656b2e60177715de1e53ef06d22b691f750b3123841052ce5bf1ac0dade069d
```

### recover_h5_floor.py


[Encoded source block omitted; the code in this passage is incomplete.]


## 8. Remaining region and continuation

Relative to the supplied exclusion map, remove the whole basal cube B_central at every genuine taper in addition to the earlier Nlj box/reflection, small-taper paired-reflection regions, macro/reflection and tubes. The remaining general taper is still `1/300<lambda<3/5` outside those regions. This result does not decide the rest of H5, nonparallel heptagon–triangle moduli, other E17 incidences, the existence of an unrestricted U1 metric in the new box, or the exact minimum. No canonical count has been changed.

The exact 4181-packet direct library, its whole-body reflected packets, and the cancellation-preserving moment initializer are reusable for adjacent basal regions, especially extension of x or r above 1/2. Where the scalar-floor class stalls, the supplied full one-sided spectral-window dual is a strictly richer next test; such a stall alone is not a physical survivor. A positive alternative must satisfy a complete original-edge rooted tree under one genuine SPD metric and then receive a full actual-inverse facet/edge/weak audit before any joint110 claim.

Convenience copy: complete recovery sources, exact atlas, reports and handoff (`h5_floor_central_capsule.zip`). The inline recovery unit and its literal parameters are sufficient without this archive.
