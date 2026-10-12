# minimum-0280

AI research report · 2026-09-27 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# H5_NINE_MODULI_CERTIFIED_REGIONS_U2_V1
## The entire corner-quarter class, plus a larger-cut nine-dimensional region

### 1. Main theorem

**The entire corner-quarter class of the literal parallel heptagon–triangle chart has U>=2 under every SPD metric, for every positive taper and every admissible origin corner. All nine parallel shape moduli are free.** A second certified region permits all six corner depths to reach 3/10.

Write the six depths as

```
k=(b,C,p,q,a,E),  C=1-c,  E=1-d.
```

Here C and E are coordinate depths, not complexity or edge count. The basal vertices are

```
(b,0), (1-C,0), (1-p,p), (q,1-q),
(0,1-E), (0,a), (u_B,v_B),
```

and the top is `(0,0,1),(rho,0,1),(0,rho,1)`. Every body is uniformly filled and centered at its **actual volume centroid**.

The following complete domains are proved:

| Domain | Basal parameters | Taper |
|---|---|---|
| QUARTER | Every depth independently in (0,1/4]; **all** u_B,v_B>0 with u_B/b+v_B/a<1 | Every rho>0 |
| WIDE | Every depth independently in [1/10,3/10]; u_B,v_B independently in [1/50,1/25] | Every rho>0 |
| BAND, preserved alternative | Every depth independently in [3/20,1/4]; u_B,v_B independently in [1/32,1/16] | Every rho>0 |

QUARTER and WIDE form a union, not nested claims. BAND is contained in QUARTER but not in WIDE; its short twelve-leaf certificate is retained as a useful alternative. The earlier five-parameter theorem also remains useful outside this union: its full p/q triangle is not subsumed by QUARTER.

Every one of the **48790 true labelled rooted weak escape systems** is excluded on every stated domain. The certificates are stronger: they exclude these systems even for nonzero PSD matrices, including the indexed, positive-volume parameter endpoints used by the compiler. For genuine physical bodies and SPD metrics, the conclusion is at least two **proper** unstable equilibria. Additional physical weak contacts are allowed.

No stable-root, covariance-spectrum, conditioning, shear, tangential-metric or weak-freedom premise is used. Every nonsingular affine image is also excluded from U1. In particular, joint proper S=U=1 is impossible on these domains, but **S>=2 for every metric is not asserted**.

This does not decide the full nine-modulus parallel chart, the separate eleven-modulus nonparallel chart, or all E17 incidences. No canonical count is subtracted and no new own110weak000 attainer is supplied. **34<=Cmin<=622 remains unchanged.** The complete chart and the older expansion theorem remain separately scoped.

### 2. Input authority and parent preservation

The entire new journal was read in consecutive chunks through line 1877/EOF. Its native bytes matched:

```
330813 bytes
0320551b62a6da146a2a203de40196455562075e12ea2e09e9c99200589c530d.
```

The required literal parent was read completely and its compact envelope reconstructed at 31563 bytes:

```
minimum-0274
1740cda6512a40b699f821c46b37eea396556e2ecc8fccf39125f51681867638.
```

The unchanged authorities remain

```
minimum-0225
c772d9b01329dcd809a288ef999d910676c13c3334cff8c96e7d59a51b887bdd

minimum-0271
78c5ee7f94706f5d44ca425624faab7a07c6d99a3b0fee6ba7cb32938ba2b290.
```

The earlier five-domain certificate remains unchanged at 1958864 bytes, SHA-256 `90f828f0dece4f5203ef96e25429f01438d791d7a102715e851e92c9a95e50f2`. The new programs import neither that certificate nor its 26278 rows. No missing computational dependency or source conflict was used.

The raw-gauge parent's previously unobserved checking program was successfully replayed **in this execution**. Its unchanged extracted source is 12289 bytes, SHA `4d1022f4c7a7edfa04f28acf54b5eea4142a22a5066cea5a707abfcf95308f69`; the observed report is 50408 bytes, SHA `e55a7c0c2296a65360b33a2510b12ea1aaa4e3aeb98d3a851fbc7bb262e65dec`, with its specified PASS marker. This does not retroactively change its original execution qualification.

The parent's positive-volume distinction is used rather than evaded: the present domains have explicit positive lower volume bounds. No zero-volume raw PSD tree is promoted to a physical survivor, and b,a,u_B,v_B are genuine variables throughout.

### 3. One actual body, true geometry and moving moments

Put `lambda=rho/(1+rho)`, `s=1-lambda`. The genuine affine map `diag(s,s,1)` gives compact vertices

```
Z_i=(s B_i,0), i=0,...,6,
Z7=(0,0,1), Z8=(lambda,0,1), Z9=(0,lambda,1).
```

Actual uniform moments transform affinely, and arbitrary SPD metrics correspond bijectively. This is not a projective refill or removal of shape moduli.

The true outward maximal facet cycles are

```
(6,5,4,3,2,1,0), (8,7,0,1), (7,6,0), (1,2,8),
(9,8,2,3), (9,3,4), (4,5,7,9), (6,7,5), (7,8,9).
```

The 17 true edges are

```
01,06,07,12,18,23,28,34,39,45,49,56,57,67,78,79,89.
```

Use the explicit convention **D=6 Vol, J24=24 integral Z**, so `g=J24/(4D)`. The actual compact moments are

```
A2=1-b*v_B-a*u_B-C*p-E*q,
D=lambda+A2*s*s,
J24_x=s**3*(1-b*v_B*(b+u_B)-a*u_B*u_B
             -C*p*(3-C-p)-E*q*q)
        +s*s*lambda*(1-C*p)+lambda**2,
J24_y=s**3*(1-b*v_B*v_B-a*u_B*(a+v_B)
             -C*p*p-E*q*(3-E-q))
        +s*s*lambda*(1-E*q)+lambda**2,
J24_z=A2*s*s+2*lambda+lambda**2.
```

The source verifies all four identities against all 16 oriented boundary triangles. It proves 56 nonincident supporting-plane guards and 19 nontriangular corner-turn guards over the complete domains; triangular corner expressions are their normal-square identities. For QUARTER, all 64 simultaneous upper-depth boundary strata are retained. The cycles form a closed sphere, with two true facets per edge; supporting cycles remain convex and maximal in the stated physical domain. Integration diagonals are never escape edges.

For QUARTER use

```
u_B=b*t*h, v_B=a*t*(1-h), 0<t,h<1.
```

This is an invertible parameterization of the entire admissible origin corner: `t=u_B/b+v_B/a`, `h=(u_B/b)/t`, with Jacobian absolute value abt>0. There are still nine independent shape parameters.

The exact compact bounds are

| Domain | A2 lower bound | D lower bound | D upper bound |
|---|---:|---:|---:|
| WIDE | 199/250 | 273/398 | 1 |
| BAND | 27/32 | 19/27 | 1 |
| QUARTER | 13/16 | 9/13 | 1 |

They use the identity

```
D=1-1/(4A2)+A2*(lambda-1+1/(2A2))**2.
```

Compiler walls with zero depths, t/h endpoints or lambda=0,1 are positive-volume indexed limits with possible merged labels/facets. They are not misreported as genuine 10/17/9 bodies.

### 4. Proof of complete all-metric exclusion

#### 4.1 Why U1 supplies a true weak rooted tree

For `X_i=Z_i-g`, define `d_ij(M)=X_i^T M(X_j-X_i)` on genuine directed edges. Proper U means every outgoing derivative is strictly negative. At any other vertex there is a genuine outgoing weak escape `d_ij>=0`.

For SPD M,

```
X_j^T M X_j-X_i^T M X_i
 =2*d_ij(M)+(X_j-X_i)^T M(X_j-X_i)>0.
```

Thus even zero derivatives give strict norm growth. A global norm maximum is proper unstable. Under U1, selecting one weak escape at every other vertex yields a spanning tree directed to the sole root. This includes incidental weak contacts and norm ties.

The program enumerates every nine-edge subset of the actual 17-edge graph, retains exactly the connected subsets and roots each at all ten vertices. It obtains 4879 unrooted and 48790 labelled rooted trees. An exact Laplacian cofactor independently gives 4879. These are local graph counts, not canonical registry increments.

#### 4.2 Exact actual-centroid polynomial tensors

For each arrow a=(i,j), put

```
R_i=4D Z_i-J24,
Q_a=-(R_i (Z_j-Z_i)^T+(Z_j-Z_i)R_i^T).
```

Identically,

```
tr(M Q_a)=-8D*d_ij(M).
```

The original edge energies and moving centroid remain present. No norm-only surrogate or free fan mass is substituted.

Map the eight basal parameters of a cell to [-1,1]. Use degree-four Bernstein form only in lambda. The independent u_B/v_B boxes have 265 base monomials; the QUARTER parameterization has 684, including the complete downward closure needed for translations. Each base variable has degree at most three. An independent inverse Bernstein transform reconstructs every entry, including zeros: 270300 checks for the boxes and 697680 for QUARTER arrays.

#### 4.3 Aggregate before bounding the remainder

A row has positive integer multipliers w_a on true arrows, with `W=sum w_a`. The **same weights** are used throughout a cell and at all five lambda coefficients. They are inequality multipliers, not physical masses.

For each lambda coefficient k choose an invertible integer proof frame H_k and expand the aggregated congruent stress:

```
H_k(sum_a w_a Q_a,k)H_k^T
 =C_k,0+sum_nu C_k,e_nu t_nu
       +sum_|alpha|>=2 C_k,alpha t^alpha.
```

Set `E_k,ij=sum_|alpha|>=2 |C_k,alpha,ij|`. The entire symmetric remainder is bounded below by `-diag(E_k*1)`, using `2|z_i z_j|<=z_i^2+z_j^2`. Aggregating first retains cancellations lost by separate arrow bounds.

For all five k and all 256 sign corners sigma, the exact checker verifies

```
C_k,0+sum_nu sigma_nu C_k,e_nu-diag(E_k*1)
       -W*2^-45*H_k H_k^T >0.
```

Every frame is checked invertible. Strict positive definiteness is checked by three exact integer Sylvester minors. These are **whole-cube affine-Taylor lower matrices**, not sampled physical bodies. The proof frames do not choose different physical metrics.

The affine corner representation, complete remainder bound and nonnegative Bernstein partition imply

```
sum_a w_a Q_a(theta)>W*2^-45 I
```

throughout the closed cell. Hence for every nonzero PSD M,

```
(sum_a w_a d_a(M))/W
 <-2^-45 tr(M)/(8D)
 <=-2^-48 tr(M)<0.
```

The support cannot consist entirely of weak escapes. This uniform physical margin is in the displayed compact affine coordinates, not an arbitrary-frame eigenvalue restriction.

#### 4.4 Closed cells and all alternatives

Base midpoint substitution is exact with denominator factor 8; degree-four lambda de Casteljau subdivision uses factor 16. Every residual rooted tree is sent to **both closed children**. A leaf passes only when every inherited tree contains a certified forbidden support. Missing children, wrong residual counts, orphan nodes, singular frames and failed minors are rejected. Each native box has exact leaf-volume sum one; the logical coverage comes from the complete two-child recursion, not that sum alone.

The exact physical reflection is

```
(b,C,p,q,a,E,u_B,v_B)->(a,E,q,p,b,C,v_B,u_B),
vertex permutation=(5,4,3,2,1,0,6,7,9,8),
(X,Y,Z)->(Y,X,Z).
```

The source checks raw vertices, D, J24 and a bijection of all 48790 rooted systems. In h,t coordinates it sends h to 1-h.

QUARTER is assembled from six **fully accepted** pieces:

| Piece | Closed lambda interval | Additional direct restriction |
|---|---|---|
| LOW | [0,1/8] | b<=1/8; reflection also covers a<=1/8 |
| LOWCORNER | [0,1/8] | b,a>=1/8; direct h<=1/2, then reflection |
| PREMID | [1/8,7/32] | Direct h<=1/2, then reflection |
| GAP | [7/32,1/4] | Direct h<=1/2, then reflection |
| TOPMID | [1/4,1/2] | Direct h<=1/2, then reflection |
| UPPER | [1/2,1] | No additional restriction |

Every unmentioned depth has its full quarter interval; t is completely free. LOW and LOWCORNER exhaust the lower band because either min(a,b)<=1/8 or both a,b>=1/8. The remaining intervals are consecutive and cover [1/8,1]. Every shared wall is retained. A separate rational relative-stratum check verifies all 1375 strata defined by these interval walls; this is an exact set-union check, not sampled metric feasibility.

The monolithic `middle` search itself was not completed. Its **domain** is covered by the independently accepted union PREMID+GAP+TOPMID. No unfinished sibling cell is used as proof.

#### 4.5 Observed exact counts

| Piece | Integer rows | Closed leaves | Maximum depth | Applications | PD lower matrices | Positive leading minors |
|---|---:|---:|---:|---:|---:|---:|
| BAND | 2332 | 12 | 5 | 4501 | 5761280 | 17283840 |
| WIDE | 6017 | 80 | 11 | 23177 | 29666560 | 88999680 |
| UPPER | 2040 | 86 | 13 | 8697 | 11132160 | 33396480 |
| LOW | 2722 | 372 | 14 | 28361 | 36302080 | 108906240 |
| LOWCORNER | 3449 | 346 | 12 | 25624 | 32798720 | 98396160 |
| PREMID | 3881 | 345 | 13 | 37014 | 47377920 | 142133760 |
| GAP | 2656 | 202 | 11 | 22803 | 29187840 | 87563520 |
| TOPMID | 4042 | 391 | 13 | 40887 | 52335360 | 157006080 |

QUARTER's six pieces have 1742 direct leaves, 209134080 PD lower-matrix checks and 627402240 positive leading-minor checks. These are sums of local applications, not distinct matrices, disjoint canonical cells or registry increments. Reflections are justified by the exact bijection rather than counted as independently checked matrices.

Missing rooted-tree alternatives after acceptance: **zero in every piece**. Supports have three through nine arrows. The largest weight is 1000000; every frame entry has absolute value at most 1000. All pieces use the same exact margin.

The positive-definite contradictions also exclude nonzero-PSD weak systems. Only the SPD norm-growth step is used to deduce the physical U>=2 census; no singular matrix is assigned a mechanical census.

### 5. Preserved actual nonwinners

The source retains twelve control records on eleven distinct geometries, with one BAND/UPPER overlap. Every control has **own222weak000 for an entire unbounded metric ray**, all 68 primitives nonzero. There are 816 checked primitive-polynomial records, counting that overlap.

Use

```
u=(1,3,-2), v=(3,-1,0), w=(-1,-3,-5),
M_L=L^2*u*u^T+L*v*v^T+w*w^T,
L^2*M_L^-1=u*u^T/14^2+L*v*v^T/10^2+L^2*w*w^T/35^2.
```

The vectors are mutually orthogonal; the displayed-frame condition number is `2L^2/5` on the stated rays. Pole origins remain the actual primal volume centroid. Representative inputs, ordered `(b,C,p,q,a,E,u_B,v_B,lambda)`, are

```
WIDE central:
(1/5,1/5,1/5,1/5,1/5,1/5,3/100,3/100,1/3), L>=512.
Vol=829/6750,
g=(3628/20725,3628/20725,1329/3316),
S=[2,4], U=[3,7], H=[18,49].

UPPER asymmetric origin corner:
(1/100,1/4,1/4,1/4,1/4,1/4,1/125,1/100,1/2), L>=256.
Vol=28729/240000,
g=(4707009/28729000,235319/1436450,58729/114916),
S=[1,4], U=[3,7], H=[18,49].

LOW taper endpoint:
(1/8,1/4,1/4,1/4,1/4,1/4,1/32,1/16,1/8), L>=64.
Vol=1069/8192,
g=(691163/3283968,345067/1641984,1261/4276),
S=[0,4], U=[3,7], H=[18,49].
```

All other literal inputs, centroids, actual covariances, poles and primitive coefficients are in the embedded source. Every hull is independently recovered from all vertex triples. Moments are independently checked using nine positive vertex-7 tetrahedra, including within-tetrahedron second moments. Substituting `L=L_min+z`, z>=0, gives a strictly signed constant coefficient and remaining coefficients of the same sign or zero. This proves each whole ray; polar rows are multiplied only by the common positive L^2.

These nonwinners show U=2 is attainable within the new domains. They are neither U1 nor own110 examples.

### 6. Search and verification status

The successful architecture retains only lambda in Bernstein form and aggregates each true-arrow stress **before** bounding the complete multivariate Taylor remainder. Integer congruences make this effective on wide basal cells. Eigenvector cuts and numerical linear programs only locate proposals. Failures trigger subdivision and never count as exclusions or physical survivors.

BAND, WIDE, UPPER and LOW were checked exactly and then rebuilt from empty states using only the frozen readable source in fresh directories, with complete exact acceptance observed. BAND, UPPER and LOW reproduced their certificate/report bytes. WIDE had two observed rounding variants differing in four scalar integers: one weight and three entries of one frame. **Both passed exact acceptance.** The final source-only variant is pinned below. The included small normalization unit maps the older accepted variant to it and was tested byte-for-byte; no general numerical bit-reproducibility claim is made.

GAP was built autonomously from an empty source-only state and its entire exact checker passed. LOWCORNER and TOPMID were checked through every cell and root from symbolically reconstructed arrays. PREMID was extracted only after its designated subtree was complete; both ancestors used no stress, and the extracted piece was checked anew from all 48790 roots in its native domain.

For LOWCORNER, TOPMID and PREMID, the replay wrapper explicitly fixes C-contiguous numerical storage. Exact coefficient arrays and floating values were matched to the recorded discovery arrays; the first three discovery nodes and all resulting rows were reproduced for each path. These limited budget-stopped runs are recovery-layout checks, **not additional full cold proofs**. Full exact acceptance was observed separately. A second complete cold rediscovery of those three pieces is not claimed.

The combined receipt checks fixed source/certificate/report pins and the exact closed-domain union. Optional `--recheck` reruns all eight complete exact checkers. The receipt does not replace their PD arithmetic. The lossless source capsule below was independently extracted and every decoded source pin and syntax check matched.

These are observed author computations and exact rational certificates, not a claimed coordinator replay, peer review or proof-assistant formalization. Outside the certified union, complete all-root feasibility remains undecided here.

### 7. Complete deterministic recovery

The capsule below contains **all six complete source units**, including every exact input, full empty-state numerical locator, exact verifier, physical-control generator and union checker. No old certificate, saved coefficient array, hidden seed or archive is required. Large certificates are regenerated from source.

Observed stack: CPython 3.13.5, SymPy 1.14.0, NumPy 2.3.5, SciPy 1.17.0 for discovery, single-thread OpenBLAS 0.3.30, Linux x86_64. Exact acceptance uses arbitrary-precision integers/rationals and no numerical optimizer. All nondefault tolerances, integer rounding rules, frame size, subdivision rules and enumeration orders are in the recovered source. Keep assertions enabled.

Save the block as `recover_h5_nine.py`, then run:

```
python -B recover_h5_nine.py recovered_h5
cd recovered_h5
OPENBLAS_NUM_THREADS=1 python -B h5_nine_exact.py build band band 5000
OPENBLAS_NUM_THREADS=1 python -B h5_nine_exact.py build wide wide 3000
python -B canonicalize_wide.py wide
OPENBLAS_NUM_THREADS=1 python -B h5_nine_exact.py check wide wide/certificate.json
OPENBLAS_NUM_THREADS=1 python -B h5_nine_exact.py build upper upper 2000
OPENBLAS_NUM_THREADS=1 python -B h5_nine_exact.py build low low 5000
OPENBLAS_NUM_THREADS=1 python -B replay_quarter_build.py lowcorner lowcorner 3000
OPENBLAS_NUM_THREADS=1 python -B replay_quarter_build.py topmid topmid 2500
OPENBLAS_NUM_THREADS=1 python -B replay_quarter_build.py premid premid 3000
OPENBLAS_NUM_THREADS=1 python -B h5_quarter_gap.py build gap gap 3000
python -B check_union.py .
```

Output directories must not already exist. Each build ends in exact verification; a node-budget failure is explicitly a non-proof. LOW and PREMID regenerate their complete prefixes from empty states and verify empty ancestral stress lists before native-domain rechecking. No surrounding unfinished region is accepted.

Existing certificates can be checked without numerical discovery:

```
python -B h5_nine_exact.py check band band/certificate.json
python -B h5_nine_exact.py check wide wide/certificate.json
python -B h5_nine_exact.py check upper upper/certificate.json
python -B h5_nine_exact.py check low low/certificate.json
python -B h5_quarter_completion.py check lowcorner lowcorner/certificate.json
python -B h5_quarter_completion.py check topmid topmid/certificate.json
python -B h5_quarter_gap.py check premid premid/certificate.json
python -B h5_quarter_gap.py check gap gap/certificate.json
```

Alternatively `python -B check_union.py . --recheck` reruns all eight. The final combined marker is

```
H5_NINE_MODULI_FULL_QUARTER_AND_WIDE_U2_V1_VERIFIED_UNION_PASS
```

Each piece prints its own `ALL_48790_NONZERO_PSD_TREES_PASS` marker with the full prefix fixed in its source.

#### Exact observed pins

| File | Bytes | SHA-256 |
|---|---:|---|
| h5_nine_exact.py | 30665 | ca132f45c0d1a6323a0eafa4bf82bd9f196065571a42f9449215351b3a50dcc2 |
| h5_quarter_completion.py | 5889 | decfb6678c3d3aa6ddf6f08666f39b1d1365b91fe29709962153c2d0bf61177e |
| h5_quarter_gap.py | 5986 | 4cbbc4176d94e60913697721b60f58a7f47da2cece0a7bc2aee67ece1b7477e0 |
| canonicalize_wide.py | 1707 | a6f93e3da661d1d95f70a3b1ce3d60c621c7737c493828f34db71cfcbae0eaac |
| replay_quarter_build.py | 1320 | 202b287f50677254660677644ced402fd073a5cafd21299987cb79786f4d4de6 |
| check_union.py | 6638 | 4f26ef32f69dbab1915aedde90989e06577ef3d35d56ee06e7c0c97539ddcaea |
| band/certificate.json | 1018011 | efe7b3047979a9905e59ef19f82a46fd3810e3c5772ac2ba39b80eeda89ba880 |
| band/report.json | 43104 | 16a667bd7f1357e55d6660a0f1d6edfef58c0ff3665f869d424a3e078e7633f5 |
| wide/certificate.json | 5020866 | 78fadc1e03b02509bed3995f3320d3109a8482206d348ed336b3fa6ad7b85cb4 |
| wide/report.json | 44440 | 023ddbd33ff2db42cf37966409da34452ccc25d83976e3579aa99eac85b830d4 |
| upper/certificate.json | 1902141 | 45e5c708e6b23f7184c9195555453191bc121024a22f6ad95d20b6fcf2d26958 |
| upper/report.json | 42963 | 6a49df27175e67e60d6dd22b90011fde78e2b908c1fa45735628a3d0f5e27c79 |
| low/certificate.json | 5934094 | 202ff32e9d55f7c6dddff22fe439a770974dc217c913c31bd79a8508fcd70e11 |
| low/report.json | 47700 | fe31aa5475b75d6879ed82d7f4357c30822298748412dbaabd7d51547a9d9263 |
| lowcorner/certificate.json | 5407699 | c1ff9ecb91f693c169a1340cdf28ae94874160a7f951658e1b8698e0d213f335 |
| lowcorner/report.json | 11108 | 433ac213e22329783a55e2e2573b0ff491fe0285e709a8c4d0e67399fbc70858 |
| premid/certificate.json | 7756629 | 83af444d51f9eda5ca7ddb208070b40d5dc27f66a04fa9304945b8a0b20115cf |
| premid/report.json | 10907 | 235f9c28848bf7c4813bfd5543bc130df05a4552851c91c6e73c4fa030206ddf |
| gap/certificate.json | 4790901 | 91a1f7cc8712c90879ad3016a18dfdb61eed795da0f09d8f3026f3423f12eec8 |
| gap/report.json | 10901 | 33e1b63ec319cc0a0e21e2a9d95b0a3d4522dcfc8da01bb5589a4c935902de3a |
| topmid/certificate.json | 8582671 | 686e342d398845c752e97d0c1de5a6ae46f7a8897c3efc4cdc92909d019b6a41 |
| topmid/report.json | 11101 | c1a2091b691852eab19e0165bff5eb69e6ca2007eb8e682227434ff152e5bdbe |
| union_report.json | 2853 | 1f9c815faa2efb069b021083a08b31004a8481e793482a209913a014383a971c |

The decoded six-source JSON map is 53488 bytes, SHA `35cfc6df1cb25cfbaef66cd4e9409d4c216300a3274c674da4d2908ab355e8a8`. The recovery source is 24316 bytes, SHA `fbc19ff24d8909f2bb6cb6fd8799150051a8105894aa6df11c7bf7f767a604ac`.

Convenience bundle: complete certificates, reports, all readable source units and handoff (`H5_NINE_MODULI_CERTIFIED_REGIONS_U2_V1.zip`). `HANDOFF.md` inside it also contains all six readable programs literally. The following capsule supplies their complete bytes independently of that link.


[Encoded source block omitted; the code in this passage is incomplete.]


### 8. Remaining frontier

The entire corner-quarter class is now closed, including all origin-corner locations and all positive taper. Retuning a shear, metric, taper or the formerly fixed basal coordinates **inside that class** cannot produce U1. WIDE closes additional larger-depth geometry, while the older five-domain theorem retains its separate large-p/q coverage.

A clean next positive-volume target is corner-third: all six depths at most 1/3, with the full origin-corner triangle. Elementary geometry gives A2>=2/3 and D>=5/8 there. These are volume bounds only—**no corner-third all-root exclusion is claimed**. Extending the aggregate-remainder certificate there, or finding one fully exact complete interior U1 body outside the certified union, would address a genuine remaining question rather than a raw boundary artifact or passing local port.

Any actual U1 survivor still requires its complete own-centroid true-edge census and then the literal same inverse for S/H/weak classification. None of the preserved own222 rays is such a survivor. Whole-chart and whole-E17 exclusion, and a smaller own110weak000 attainer, remain separate open objectives.
