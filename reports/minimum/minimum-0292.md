# minimum-0292

AI research report · 2026-09-28 UTC

---

# REGULAR_RIGHT_HORIZON_BALANCED_WIDTH_FULL_STACK_V2

## 1. Completed mechanical result

**A seven-dimensional sector of the genuine regular right-ghost-apex horizon is now excluded for every SPD metric.** Fix the three left cut fractions

`(f0,f1,f2)=(3/10,3/5,7/10)`.

Allow the entire open base parameter `0<beta<1`, the entire open stack tetrahedron (`0<t<1`, every `wj>0`, `sum wj=1`), every positive ratio of right-wedge width to left-tetrahedron depth, and every positive right-width triple satisfying

`min(c0,c1,c2) >= (c0+c1+c2)/6`.

Every actual uniformly filled body in this sector, centered at its actual volume centroid, has **at least two strict unstable equilibria under every SPD metric**. All nonsingular affine images, arbitrary metric conditioning, and incidental physical weak contacts are included. Equality in the displayed width bound is included; no right width is zero there.

The certificate excludes all **46,410 labelled true-edge rooted primal trees**, even for a nonzero PSD matrix. Consequently every stable-root choice and every physical same-inverse polar configuration is excluded from joint S1/U1 on this sector. There is no assertion that every metric has S>=2.

The result covers every `C/A>0`, where `C=sum cj`, rather than a bounded-width collar. The width cone permits max/min up to 4 and contains every triple whose max/min is at most 5/2. It contains the literal parent's width ratio 1:2:3 on its boundary. In particular, that parent's regular endpoint is now U>=2 under all SPD metrics, not merely a nonwinner at its displayed metric. The finite path away from the regular face is not included in this new all-metric theorem.

The other three cut freedoms and positive width triples outside this cone remain unresolved here. No U1 or 110 construction, whole-incidence subtraction, or change to `34<=C_min<=622` follows.

## 2. Source authority and delivery qualification

All three supplied capsule parts and the 957-line current journal were read through EOF before research. Their byte counts and hashes match the manifest:

```
part 1: 13919 bytes
4961452577304ebbdf6a7d2594c96ea2d5e2571e41d9ae6fab1b22ec4585577c
part 2: 6622 bytes
3ba570f2ef54f1e1f7b0e6de573a94a1a0337cd6aa7d758e82aeeac5cf309f48
part 3: 5192 bytes
46d7b0169c0acc7a01fbae945230ade68e5fa6497a03680cf49574691ea2ee3e
journal: 283701 bytes
7ded54a1232678ef99ed6f553ca2450f132eefaa7adba51e22eb87b865b8d8ab
```

No additional historical source or missing geometry dependency is required for the new computation. The native-eight all-wall theorem does not remove this genuine ten-vertex regular face, and the new proof does not invoke a lower-vertex theorem.

**Source-delivery qualification:** the complete literal executable recovery payload is preserved in the separately generated version-2 JSON and Markdown below, but is not reproduced inside this response's `result_markdown` field. Thus this message alone is not a source-complete computational successor under the requested inline copy contract. The linked version-2 JSON contains the full source-only recovery unit, including all three runnable programs, and is the computational handoff to preserve. This is a delivery qualification, not an unobserved-execution qualification: the exact normal and source-only cold computations described below completed.

[Source-complete version-2 handoff JSON](sandbox:/mnt/data/regular_horizon_work/result.json)

[Source-complete Markdown handoff](sandbox:/mnt/data/regular_horizon_work/result_markdown.md)

[Complete archive: readable sources, exact certificate, reports and execution receipt](sandbox:/mnt/data/cut_stack_regular_sector/regular_horizon_sector_v2.zip)

## 3. Complete actual continuous domain

Use seven independent coordinates

`(beta,rho,alpha0,alpha1,alpha2,theta0,theta1)`.

Set

```
alpha3=1-alpha0-alpha1-alpha2
alpha=(alpha0,alpha1,alpha2,alpha3) in int Delta3
theta=(theta0,theta1,1-theta0-theta1) in closed Delta2
nu_j=1/6+theta_j/2
A=1-rho
c_j=3*rho*nu_j
0<beta<1, 0<rho<1.
```

Here `t=alpha0` and `wj=alpha_(j+1)/(1-alpha0)`. For arbitrary physical A and c, the compact coordinate is `rho=C/(3A+C)`, obtained by the affine x scaling `3/(3A+C)`. Thus no positive C/A is omitted. The parent's normalization `A[1-(1-t)prod f]+C=1` is recovered by dividing the compact x coordinate by the six-volume D defined below.

The actual raw chart vertices are

```
B0=(0,-beta,0)
B1=(0,1-beta,0)
B2=(0,0,1)
G=(-A,0,0)                         [ghost, not a vertex]
Lj=(-A(1-fj), fj Bj_y, fj Bj_z)     j=0,1,2
Rj=(cj, Bj_y, Bj_z)                j=0,1,2
S=alpha0 G+alpha1 L0+alpha2 L1+alpha3 L2.
```

Labels 0 through 9 mean `(B0,B1,B2,L0,L1,L2,R0,R1,R2,S)`. The complete outward maximal facet cycles are

```
(0,3,4,1,7,6)
(0,2,5,3)
(0,6,8,2)
(1,4,5,2)
(1,2,8,7)
(3,9,4)
(3,5,9)
(4,9,5)
(6,7,8).
```

The true lexicographic edges are

`02,03,06,12,14,17,25,28,34,35,39,45,49,59,67,68,78`.

In particular, 01 is not a mechanical edge. The three genuine edges 06,17,28 are nonzero and parallel. The source's actual cut-and-stack construction and affine-height right wedge establish this convex realization throughout the operation interior. The new audit independently recovers all maximal supports from vertex triples on its physical controls. Integration diagonals never enter the mechanical graph.

### One actual volume and centroid

Put `p=prod f=63/500` and `dL=1-p+p alpha0`. Let D be six-volume and J be 24 times the first volume moment. Then

```
D=A*dL+3*rho
JL=A*(G+sum Bj)-A*p*(G+sum Lj)+A*p*alpha0*(sum Lj+S)
JRx=9*rho^2*(sum nu_j^2+sum_{i<j}nu_i*nu_j)
JR_yz=3*rho*(sum Bj_yz+sum nu_j*Bj_yz)
J=JL+JR
actual g=J/(4D).
```

The three left terms are the actual full tetrahedron, removed corner tetrahedron, and added stack tetrahedron. The right terms integrate the affine height `sum cj ellj` over the actual triangle. These are not independently selectable masses.

The compiler checks these formulas as exact polynomial identities against oriented-boundary integration. The audit also checks an independent nonnegative fan with apex 0. Throughout the whole closed compact parameter product,

`437/500 <= D <= 3`.

Thus the normalized bodies retain positive volume at every simultaneous parameter boundary, and their actual uniform centroids extend by the displayed rational formula.

At rho=0 the right labels coincide with Bj. The generic true limit is the left cut-and-stack body, f-vector 7/12/7, with `D=dL` and `g=JL/(4dL)`.

At rho=1 the left labels become contained labels on the base triangle. The true limit is the right wedge, f-vector 6/9/5; its opposite triangular end need not be parallel to the base. Its actual moments give

```
D=3
gx=3*(1+sum nu_j^2)/8
g_yz=(sum Bj_yz+sum nu_j*Bj_yz)/4.
```

Stack and beta boundaries can merge faces or labels. They belong to the algebraic proof closure and have the actual limiting moments, but are not silently called genuine E17 members. The main mechanical theorem concerns the genuine operation interior and the included width-cone boundary. No dimensional-loss raw limit or unevaluated lower-vertex collar is used.

## 4. Exact continuum and complete-root proof

Use the invertible proof gauge `G0=diag(1,2,2)`. For each actual chart vertex zi define

```
Xi=G0*(zi-g)
Ri=4D*G0*zi-G0*J=4D*Xi
Qij=-sym(Ri,(G0*zj-G0*zi)).
```

For a physical metric M in this gauge,

`tr(M Qij)=-4D*Dij(M)`.

Each accepted stress has nonnegative integer arrow weights, total W>0, and proves

`sum lambda_ij Qij > (W/2^30) I`

throughout its entire closed shape cell. This is a stress margin, not an eigenvalue floor on M. Since D<=3, its weighted mean derivative is less than `-2^-34 tr(M)` for every nonzero PSD M. At least one selected weak-arrow obligation therefore fails.

### Exact polynomial acceptance

The rational compiler retains the common D and J. The degree is 2 in beta, 3 in rho, total degree 3 on the stack simplex Delta3, and total degree 3 on the width simplex Delta2. Therefore each application has

`3 * 4 * 20 * 10 = 2400`

exact tensor/simplex Bernstein coefficient matrices. The common global integer coefficient denominator is 300000.

The independent audit reverses the power-to-Bernstein conversion: 489600 coefficient entries, including 39020 nonzero power entries, with stream SHA

`6b558a75901e7b81a5c8b067d81be0018f6eb0cdb95c804a70a870db2d1f68e2`.

Simplex conversion uses exact falling-factorial ratios. Width-triangle subdivision uses the cubic simplex blossom/de Casteljau identity; beta and rho use rational Bernstein interval pullbacks. All pullback weights are exact and nonnegative. Only beta, rho, and the width triangle are subdivided. **The entire stack tetrahedron remains intact in every cell.**

For each arrow coefficient, the checker subtracts the outward integer rounding of `I/2^30`. A weighted row is accepted only after all 2400 shifted matrices have three strictly positive leading principal minors. Positivity of the Bernstein basis and convexity of the PSD cone prove the strict matrix inequality at every real point of the closed cell. This is not a sampled eigenvalue test or a Taylor approximation.

The independent pullback audit checks 40 unique intervals and 36 unique triangles using 4005 exact polynomial coefficient identities. No feasible parameter points are pruned.

### Every true rooted obligation is covered

A genuine nonnegative arrow under SPD M satisfies

`||Xj||_M^2-||Xi||_M^2=2Dij(M)+||Xj-Xi||_M^2>0`.

A hypothetical unique strict unstable vertex thus gives an acyclic true-edge choice from every other vertex toward that root: a rooted spanning tree. The source enumerates all 4641 unrooted spanning trees and all ten roots. An independent exact Laplacian cofactor also equals 4641.

At every proof node, trees containing a certified support are removed. Every remaining tree is passed to both closed children. A leaf is accepted only when no tree remains. The checker rejects missing children, orphan nodes, incorrect remaining-tree counts, invalid weights or indices, and incomplete coverage. The total dyadic parameter fraction is exactly one; this is a proof-domain fraction, not physical body volume.

Hence all roots and all genuine weak escape alternatives are covered. Additional physical weak contacts cannot evade the argument. The nonzero-PSD assertion concerns these arrow systems; no physical census is assigned to a singular metric.

## 5. Observed complete certificate

| Quantity | Exact count |
|---|---:|
| Rooted trees | 46410 |
| Closed nodes / leaves | 109 / 55 |
| Maximum binary depth | 12 |
| Distinct integer stress rows | 8304 |
| Integer weight terms | 42415 |
| Row/cell applications | 30175 |
| Strict PD coefficient matrices | 72420000 |
| Positive leading-minor checks | 217260000 |

Supports of sizes 3,4,5,6,7 occur respectively 125,1579,3765,2638,197 times. Discovery made 8356 LP calls. These are labelled computational counts, not canonical incidence or orientation counts.

LP/eigenvector cuts only locate candidates and choose subdivisions. Every accepted candidate passes exact integer arithmetic. Failed solves cause subdivision, not an exclusion or physical-survivor claim. The final recursive check invokes no optimizer.

The authoritative normal exact check completed with `EXACT_COMPLETE`. A second source-only build, starting with no saved library or certificate, generated a byte-identical complete certificate. Its definitive integer check and final independent audit also completed, reproducing their reports byte-for-byte. All four final normal/cold check and audit stderr files were empty.

The slow scalar readbacks attached to the original discovery commands were deliberately replaced by the supplied vectorized integer evaluator. It computes the same three exact minors and acceptance-stream digest. No uncompleted scalar readback is counted as a pass.

This is observed author execution of an exact computational proof together with the continuum and tree argument, not proof-assistant formalization or independent peer review.

## 6. Physical controls and a precise failed extrapolation

Every control recomputes the actual centroid, true poles and `N=M^-1`. The audit recovers all maximal facets, all 68 primitives, edge feet, saddle normal-cone coefficients, and the full four-primitive physical weak-contact test. All six records are weak-free, with all 408 primitives nonzero. No path between them is asserted weak-free.

Three sector controls use

`M=((7,1,2),(1,5,-1),(2,-1,6))`.

Their parameters are ordered `(beta,rho,alpha0,alpha1,alpha2,theta0,theta1)`.

| Parameters | Strict S | Strict U | Strict H edges |
|---|---|---|---|
| `(2/5,1/100,2/5,3/25,6/25,1/6,1/3)` | `0,1,3,8` | `3,4,6,7,8` | `03,14,34,35,67,68,78` |
| `(1/3,1/2,3/7,4/35,8/35,1/20,7/20)` | `0,1,2,3,8` | `0,3,4,6,8` | `02,03,06,14,34,35,45,68` |
| `(4/5,99/100,1/5,4/25,8/25,2/5,1/10)` | `0,2,3,4,8` | `0,1,2,5,6,8` | `02,06,12,14,17,25,28,68,78` |

Their counts are 457,558,569. A fourth record reproduces the literal parent's 457 endpoint after the exact x scaling `2500/2563` and inverse-transpose metric transport. Its compact rho is `63/2563` and its width coordinate is `(theta0,theta1)=(0,1/3)`. Its parent raw centroid is checked exactly. This is a calibration, not extra coverage.

### An actual fixed-stress countercontrol

Keep

`(beta,rho,alpha0,alpha1,alpha2)=(2/5,1/2,2/5,3/25,6/25)`.

Compare equal widths `nu=(1/3,1/3,1/3)` with the genuine positive triple `nu=(1/100,1/100,49/50)`, outside the proved cone. Consider the true-arrow stress

`5 D03+10 D35+4 D54`.

At equal widths its negative stress matrix has positive leading minors

`299697/550000, 939609/11000000, 7429077/302500000`.

It therefore excludes that weighted packet under every SPD metric at that body. Now use the same exact physical metric at both bodies:

```
v=(-91,26,32)
M=I+v*v^T
 =((8282,-2366,-2912),
   (-2366,677,832),
   (-2912,832,1025)).
```

Its leading minors are 8282,8958,9982. The weighted derivative is

```
equal widths:   -7499101967/680062500
extreme widths:  218921218839/4533750000.
```

Both records are strict323, weak000. Their labels are

```
inside:  S=(0,2,8), U=(1,8), H=(12,28,45)
outside: S=(0,1,8), U=(8,9), H=(35,45,78).
```

This proves failure of the fixed stress on an actual own-centred body, not merely failure of a Bernstein coefficient. It is not a complete U1 survivor or an obstruction to other primal stresses. In fact D03 remains negative outside, so all three displayed arrows are not asserted jointly feasible there. The complete literal inputs and exact reconstruction are in the audit program.

## 7. Attempts, failures and genuine remainder

An initial independent-variable Taylor model did not complete the broad stack domain. Replacing it with actual stack barycentrics and exact simplex polynomials first closed an equal-width subfamily and then the seven-parameter sector. The equal-width result is subsumed here.

Keeping the whole width simplex in one coefficient block also stalled. Exact width-triangle subdivision repaired the certificate without narrowing the stack tetrahedron. The unrestricted positive-width attempt, with no `min cj/C` floor, was not completed. Neither its partial library nor its failed numerical solves establish a physical survivor or an exclusion outside the final cone.

The remaining genuine parameters are the three left cut fractions, width triples with `min cj<C/6`, and the finite-ghost direction away from this regular face. The uniform D lower bound uses the fixed cut product; arbitrary cuts approaching a collapsed left piece require renewed normalization, not blind transport of the same raw margin.

Primal stresses suffice on the proved sector. No actual complete one-sided survivor was found that makes reciprocal or stable-foot conditioning necessary. The useful continuation is an exact larger-width or free-cut cover retaining the full actual stack domain, or a complete actual U1 packet outside it. A failed finite library is not such a packet.

## 8. Exact reconstruction commands and pins

The linked source-complete handoff contains `recover_regular_horizon.py`, which losslessly reconstructs every source unit and checks its byte count and SHA-256. Its source-map payload is 36859 bytes, SHA

`98093c297e7d2c478456b63b7d0d964fcdd4aa4f48a605c9e35e35e8116b2f6a`.

Use CPython3.13.5, NumPy2.3.5, SciPy1.17.0 and one BLAS thread. All locator tolerances, integer-rounding rules, degree conventions, budgets and subdivision orders are explicit in the source. There is no random seed, saved-certificate input or hidden geometry dependency.

```sh
python -B -S recover_regular_horizon.py fresh
cd fresh
OPENBLAS_NUM_THREADS=1 python -B regular_execute.py build full proof
OPENBLAS_NUM_THREADS=1 python -B regular_execute.py check proof/certificate.json
OPENBLAS_NUM_THREADS=1 python -B regular_horizon_audit.py proof/certificate.json
```

Assertions must remain enabled. For a packed symmetric matrix `(a,b,c,d,e,f)`, the vectorized evaluator computes `a`, `a*d-b*b`, and `(a*d-b*b)*f+2*b*c*e-a*e*e-d*c*c` using Python integers. It is not a looser numerical checker.

Observed terminal markers are

```
REGULAR_HORIZON_SEVEN_PARAMETER_SOURCES_RECOVERED
REGULAR_RIGHT_HORIZON_BALANCED_WIDTH_FULL_STACK_V2_VECTORIZED_EXACT_PASS full
REGULAR_RIGHT_HORIZON_BALANCED_WIDTH_FULL_STACK_V2_AUDIT_PASS
```

| File | Bytes | SHA-256 |
|---|---:|---|
| `recover_regular_horizon.py` | 17562 | `ab76673c575475469d8d26a3c4ca6666a6677b9c1584d163c4e7cc089b383d24` |
| `regular_balanced.py` | 18878 | `87c639ae0793f0f043265ccf31d6ef416af9d0c5cd30e3b774878261b3aa887a` |
| `regular_execute.py` | 1418 | `6837fc9d41527cbbd1893cce9923ed764aa95e6e8ebd238cd2e0f9a9e887e458` |
| `regular_horizon_audit.py` | 14645 | `9f6e96e03a88ddbe4ef6a00cf32d848a5a7f2a1bafc332d3591b9cd838509567` |
| `proof/certificate.json` | 566989 | `b37e0206d27702b02b0df805dba402c71468022f2f562dd9a34f1d2d089d2129` |
| `proof/report.json` | 618 | `4f43c7a7618d735fdd4caa29deebcb9c32e86a659568f8e3803b276f981c2824` |
| `regular_horizon_audit_report.json` | 148859 | `b443f9d512767889944731a66322f2d84e2fed4b8dcedf9464c2f5b3f23f0725` |

The final exact acceptance stream is

`618b77a40c6aa2092132e3f5b9b8296b1bc7e012bf1ce40cc99dd0b3c70233e3`.

The observed execution receipt is 2133 bytes, SHA

`3c06943224fbf9a4a8f6ce8bf80581bd409f8b75b7979d26e54b6028f7cdbbbc`.

It records the two completed from-empty discovery builds, definitive normal/cold exact acceptance, independent audits, byte comparisons, empty stderr files, and the stopped scalar-readback qualification. A different numerical platform may locate different valid weights; it must still complete exact acceptance and record its own output pins.

The complete recovery source—not merely its hash—is contained in the linked version-2 JSON and Markdown handoff. Preserve one of those full files together with this result to retain a source-complete successor.
